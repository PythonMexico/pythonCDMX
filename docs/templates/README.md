# 🐍 Sistema de Generación Automática de Meetups PythonCDMX

> ⚠️ **NOTA**: Este directorio ya no se usa. El sistema de templates ha sido reemplazado por un sistema JSON más eficiente.

## 🚀 Nuevo Sistema JSON

El sistema de templates con variables `{{ VARIABLE }}` ha sido reemplazado por un sistema más moderno y eficiente basado en JSON.

### 📁 Archivos del Nuevo Sistema

- `meetup-data.json` - Base de datos JSON con información de meetups
- `generate_meetup.py` - Script que genera archivos markdown desde JSON
- `create_meetup.py` - Script interactivo para crear nuevos meetups
- `README-MEETUP-SYSTEM.md` - Documentación completa del nuevo sistema

### 🎯 Ventajas del Nuevo Sistema

- ✅ **Automatización completa**: No más variables sin procesar
- ✅ **Consistencia garantizada**: Todos los meetups tienen el mismo formato
- ✅ **Facilidad de uso**: Scripts interactivos que guían el proceso
- ✅ **Mantenibilidad**: Datos separados de la presentación
- ✅ **Flexibilidad**: Campos opcionales y personalizables

## 📋 Cómo Usar el Nuevo Sistema

### 1. Crear un Nuevo Meetup (Recomendado)
```bash
python create_meetup.py
```

### 2. Generar Archivos Markdown
```bash
python generate_meetup.py
```

### 3. Ver Documentación Completa
Consulta `README-MEETUP-SYSTEM.md` en el directorio raíz para instrucciones detalladas.

## 🔄 Migración desde el Sistema Anterior

Si tienes meetups creados con el sistema de templates:

1. **Extrae la información** de los archivos markdown existentes
2. **Agrega los datos** al archivo `meetup-data.json`
3. **Regenera los archivos** con `python generate_meetup.py`

## 📞 Soporte

Para dudas sobre el nuevo sistema:
1. Consulta `README-MEETUP-SYSTEM.md`
2. Revisa el archivo `meetup-data.json` como ejemplo
3. Usa `python create_meetup.py` para crear meetups paso a paso

---

**El nuevo sistema es mucho más eficiente y fácil de usar. ¡Pruébalo!** 🎉
