# DEMO: Detección de Inconsistencias Arquitectónicas con MCP

Esta guía te muestra cómo demostrar el poder de los Skills MCP integrados en tu proyecto.

## Paso 1: Reinicia los Servidores MCP

En VS Code:
1. Abre el **Copilot Chat** (Ctrl + Shift + I)
2. Busca la opción para "Reiniciar servidores MCP"
3. Espera a que se reconecten los tres servidores:
   - `arquitectura-db` ✅
   - `auditor-archivos` ✅
   - `lector-web` ✅

## Paso 2: Usa el Mega Prompt

Copia exactamente esto en Copilot Chat (asegúrate de escribir `@workspace` al principio):

```
@workspace Usa tu herramienta de base de datos para leer la tabla 'servicios'.
Usa tu herramienta de sistema de archivos para leer el archivo 'docker-compose.yml'.
Compara ambos. ¿Hay algún servicio en el docker-compose que no esté documentado en la base de datos?
Genera un diagrama Mermaid que incluya:
- Todos los servicios de la base de datos (en verde)
- Los servicios 'no documentados' del docker-compose en color rojo
- Las dependencias entre ellos
Explica las inconsistencias encontradas.
```

## Paso 3: Analiza los Resultados

El agente debería reportar:

### Servicios en la Base de Datos (arquitectura.db)
```
✅ Frontend
✅ API Gateway
✅ Auth Service (En Mantenimiento)
✅ User DB
```

### Servicios en docker-compose.yml
```
✅ frontend
✅ api-gateway
✅ auth-service
✅ user-db
🔴 redis-cache (NO DOCUMENTADO - INCONSISTENCIA)
```

### Diagrama Mermaid Esperado
Debería mostrar Redis en rojo para indicar que necesita ser documentado en la base de datos.

## Casos de Uso Avanzados

### Caso 1: Verificar Documentación Externa
```
@workspace usa tu herramienta de fetch para leer la documentación oficial de Redis en redis.io
Compáralo con nuestra configuración en docker-compose.yml
¿Estamos usando las mejores prácticas?
```

### Caso 2: Auditar Todos los Archivos
```
@workspace usa auditor-archivos para encontrar todos los archivos de configuración en el proyecto
Lista cualquier servicio mencionado en ellos
Compara con arquitectura.db
```

### Caso 3: Generar Documentación Automática
```
@workspace lee todos los servicios de arquitectura.db
Lee docker-compose.yml
Genera un documento README actualizado que liste:
- Servicios documentados vs. reales
- Versiones de imágenes
- Puertos expuestos
- Variables de entorno
```

## Por Qué Esto Es Impresionante

Este flujo demuestra:

1. **Orquestación de herramientas**: El agente usa 3 MCPs en secuencia
2. **Análisis comparativo**: Detecta automáticamente inconsistencias
3. **Generación de artefactos**: Crea diagramas Mermaid basados en datos
4. **Visión sistémica**: Entiende toda la arquitectura en contexto

## Archivos Generados Automáticamente

- `servicios_diagram.mmd` - Diagrama inicial de servicios
- `docker-compose.yml` - Configuración con servicio extra (Redis)
- `.vscode/mcp.json` - Configuración de servidores MCP

## Próximos Pasos

1. ✅ Ejecuta el Mega Prompt
2. ✅ Documenta las inconsistencias encontradas
3. ✅ Actualiza `arquitectura.db` con los servicios faltantes
4. ✅ Regenera los diagramas
5. ✅ Verifica que no hay más inconsistencias
