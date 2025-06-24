# Política de Seguridad 🔒

## Versiones Soportadas

Usa esta sección para decirle a las personas qué versiones de tu proyecto están actualmente siendo soportadas con actualizaciones de seguridad.

| Versión | Soportada          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reportar una Vulnerabilidad

Agradecemos que reportes vulnerabilidades de seguridad. Para reportar una vulnerabilidad, por favor:

### Método Preferido: Email Privado

1. **No crees un issue público** - Las vulnerabilidades de seguridad deben ser reportadas de forma privada
2. **Envía un email a:** info@pythoncdmx.org
3. **Incluye en el asunto:** `[SECURITY]` seguido de una descripción breve
4. **Proporciona detalles completos** en el cuerpo del email

### Información Requerida

Para ayudarnos a entender y resolver la vulnerabilidad rápidamente, incluye:

- **Descripción detallada** de la vulnerabilidad
- **Pasos para reproducir** el problema
- **Impacto potencial** de la vulnerabilidad
- **Sugerencias** para la solución (si las tienes)
- **Información del sistema** donde se encontró

### Ejemplo de Email

```
Asunto: [SECURITY] Vulnerabilidad XSS en formulario de contacto

Hola equipo de Python CDMX Charlas,

He encontrado una vulnerabilidad XSS en el formulario de contacto del sitio web.

Descripción:
[Descripción detallada]

Pasos para reproducir:
1. Ve a la página de contacto
2. Inyecta el siguiente código: <script>alert('XSS')</script>
3. El script se ejecuta en el navegador

Impacto:
Los atacantes podrían ejecutar código malicioso en el navegador de los usuarios.

Sugerencias:
Implementar validación y sanitización de entrada en el lado del servidor.

Saludos,
[Tu nombre]
```

## Proceso de Respuesta

1. **Confirmación** - Recibirás una confirmación de que tu reporte fue recibido (dentro de 48 horas)
2. **Investigación** - Nuestro equipo investigará la vulnerabilidad
3. **Actualización** - Te mantendremos informado sobre el progreso
4. **Resolución** - Una vez resuelta, te notificaremos y publicaremos los detalles apropiados

## Timeline

- **48 horas** - Confirmación inicial
- **7 días** - Evaluación inicial y plan de acción
- **30 días** - Resolución o actualización de estado
- **90 días** - Divulgación pública (si es apropiado)

## Divulgación Responsable

Seguimos las mejores prácticas de divulgación responsable:

- **No divulgaremos** vulnerabilidades hasta que estén resueltas
- **Te daremos crédito** por el descubrimiento (si lo deseas)
- **Publicaremos** un advisory cuando sea apropiado
- **Actualizaremos** la documentación de seguridad

## Recompensas

Actualmente no ofrecemos recompensas monetarias por reportes de seguridad, pero:

- **Reconocimiento público** en nuestros canales oficiales
- **Agradecimiento especial** en la documentación del proyecto
- **Credenciales** para la comunidad Python CDMX

## Mejores Prácticas de Seguridad

Para contribuidores y usuarios:

### Para Desarrolladores

- **Revisa el código** antes de hacer commit
- **Usa herramientas** de análisis estático
- **Mantén dependencias** actualizadas
- **Sigue** las mejores prácticas de OWASP

### Para Usuarios

- **Mantén tu navegador** actualizado
- **Usa HTTPS** siempre que sea posible
- **Reporta** comportamientos sospechosos
- **No compartas** información sensible en issues públicos

## Recursos de Seguridad

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [GitHub Security Lab](https://securitylab.github.com/)
- [Python Security](https://python-security.readthedocs.io/)
- [MkDocs Security](https://www.mkdocs.org/user-guide/security/)

## Contacto

- **Email de seguridad:** info@pythoncdmx.org
- **Telegram:** [@PythonCDMX](https://t.me/PythonCDMX)
- **GPG Key:** [Disponible bajo solicitud]

## Historial de Vulnerabilidades

| Fecha | Vulnerabilidad | Severidad | Estado |
|-------|----------------|-----------|--------|
| - | - | - | - |

---

*Esta política está basada en las mejores prácticas de la comunidad open source. Última actualización: Enero 2024*
