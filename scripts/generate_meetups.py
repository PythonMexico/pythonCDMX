import json
import locale

from pathlib import Path
from datetime import datetime
from tqdm import tqdm
from dataclasses import asdict, dataclass

from argparse import ArgumentParser
from typing import Any, Callable, TypeVar
from jinja2 import Environment, FileSystemLoader

locale.setlocale(locale.LC_ALL, 'es_MX.UTF-8')

@dataclass
class Speaker:
    name: str
    job_title: str
    company: str | None
    bio: str
    photo: str | None

@dataclass
class TalkDescription:
    header: str | None
    content: list[str]
    footnotes: list[str]
    
@dataclass
class Talk:
    title: str
    subtitle: str | None
    description: TalkDescription
    speaker: Speaker
    video_url: str | None 

@dataclass
class MeetupLocation:
    venue: str
    address: str

@dataclass
class MeetupMetadata:
    id: str
    start_date: datetime
    end_date: datetime
    title: str
    subtitle: str | None
    location: MeetupLocation
    talks: list[Talk]
    tags: list[str]
    storytelling: list[str] # Cada linea es un parrafo en el render final (Soporta Markdown)

def parse_speaker(speaker: dict[str, Any]) -> Speaker:
    return Speaker(
        name=speaker['name'],
        job_title=speaker['title'],
        company=speaker.get('company'),
        bio=speaker['bio'],
        photo=speaker.get('photo', '/images/ponentes/default.jpg')
    )

def parse_description(description: dict[str, Any]) -> TalkDescription:
    print(f'{description=}')
    return TalkDescription(
        header=description.get('header'),
        content=description['content'],
        footnotes=description.get('footnotes', [])
    )

def parse_talk(talk: dict[str, Any]) -> Talk:
    return Talk(
        title=talk['title'],
        subtitle=talk.get('subtitle', ''),
        description=parse_description(talk['description']),
        speaker=parse_speaker(talk['speaker']),
        video_url=talk.get('video_url')
    )

def parse_location(location: dict[str, Any]) -> MeetupLocation:
    return MeetupLocation(
        venue=location['venue'],
        address=location.get('address', ''),
    )
    
def metadata_parser(metadata: dict[str, Any]) -> MeetupMetadata:
    print(f'New Parser {metadata}')
    id = metadata['id']
    start_date = datetime.strptime(metadata['start_date'], '%Y-%m-%d %H:%M')
    end_date = datetime.strptime(metadata['end_date'], '%Y-%m-%d %H:%M')
    location = parse_location(metadata['location'])
    tags = metadata.get('tags', [])
    # Si talks no está definido, el parser fallará con KeyException
    talks = [parse_talk(talk) for talk in metadata['talks']]
    print(f'Procesando {len(talks)} charlas')
    first_talk = talks[0]
    storytelling = metadata.get('storytelling', [])
    # Si solo hay una charla, podemos heredar los campos de su metadata,
    # si hay más de una charla, es mandatorio definir los campos en raiz.
    if len(talks) == 1:
        title = metadata.get('title', first_talk.title)
        subtitle = metadata.get('subtitle', first_talk.subtitle)

        return MeetupMetadata(
            id=id,
            start_date=start_date,
            end_date=end_date,
            title=title,
            subtitle=subtitle,
            location=location,
            talks=talks,
            tags=tags,
            storytelling=storytelling
        )
    else:
        title = metadata['title']
        subtitle = metadata.get('subtitle', '')

        return MeetupMetadata(
            id=id,
            start_date=start_date,
            end_date=end_date,
            title=title,
            subtitle=subtitle,
            location=location,
            talks=talks,
            tags=tags,
            storytelling=storytelling
        )

T = TypeVar('T')
def parse_json(filename: str, parser: Callable[[dict[str, Any]], T]) -> T:
    with open(filename, 'r') as file:
        file_content = json.load(file)
        return parser(file_content)

def confirm_action(message: str) -> bool:
    confirmation = input(message + ' [Y/n]')
    if confirmation not in ('y', 'n', 'Y', 'N'):
        print('El valor ingresado no es válido, intente nuevamente.')
        return confirm_action(message)
    return confirmation in ('y', 'Y')
        
def parse_path(filename: str) -> Path | None:
    path_obj = Path(filename)
    if path_obj.exists():
        return path_obj
    
    confirmation = confirm_action('La ruta especificada no existe, deseas crearla?')
    if confirmation:
        path_obj.mkdir()
        return path_obj
    return None
    
        
def main(metadata: MeetupMetadata, templates_dir: Path, template_name: str, output_dir: Path):
    print(metadata)
    jinja_env = Environment(loader=FileSystemLoader(templates_dir))
    template = jinja_env.get_template(template_name)
    output = template.render(**asdict(metadata))
    output_filename = f'{output_dir}/{metadata.start_date:%Y}/{metadata.id}.md'
    with open(output_filename, 'w') as rendered_markdown:
        rendered_markdown.writelines(output)

if __name__ == "__main__":
    parser = ArgumentParser(description='Este script transforma un archivo de metadata (JSON) a un archivo Markdown listo para ser desplegado en nuestro sitio.')
    parser.add_argument('--metadata', '-m', type=str, required=True, nargs='+', help='Archivos de metadata con la configuración del evento.')
    parser.add_argument('--output-dir', '-o', default='docs/meetups', help='Directorio de salida donde se guardará el Markdown generado. Si el valor se omite, estará bajo el directorio meetups')
    parser.add_argument('--templates-dir', '-t', default='templates', help='Directorio de plantillas donde se lee la plantilla base usada para renderizar las páginas.')

    args = parser.parse_args()
    print(args.metadata)

    templates_dir = parse_path(args.templates_dir)
    if not templates_dir:
        raise FileNotFoundError('El directorio de plantillas no existe!')
    output_dir = parse_path(args.output_dir)
    if not output_dir:
        raise FileNotFoundError('El directorio de salida no existe!')

    template = 'meetup.md.j2'

    for metadata_json in tqdm(args.metadata):
        parsed_metadata = parse_json(metadata_json, metadata_parser)
        main(parsed_metadata, templates_dir, template, output_dir)
       
