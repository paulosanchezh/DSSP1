# Diseño de Sistemas Software - Arquitectura de Servicios

Este proyecto es la práctica correspondiente a la asignatura de Diseño de Sistemas Software (DSS). Consiste en el desarrollo y aplicación de principios de diseño de software, incluyendo modelado, arquitectura y patrones de diseño, para resolver problemas prácticos en el ámbito de la ingeniería de software.

## Descripción Detallada

A través de este proyecto se abordan conceptos fundamentales del diseño de sistemas software tales como:

- **Arquitectura de Software**: Diseño de la estructura general del sistema, componentes y sus relaciones.
- **Patrones de Diseño**: Aplicación de soluciones reutilizables a problemas comunes.
- **Modelado UML**: Creación de diagramas de clases, casos de uso y secuencia.
- **Principios SOLID**: Desarrollo de código mantenible, escalable y flexible.
- **Análisis y Especificación de Requisitos**: Definición clara de lo que debe hacer el sistema.

El objetivo es que el estudiante desarrolle habilidades para diseñar sistemas software robustos, mantenibles y escalables siguiendo buenas prácticas de ingeniería.

## Logros Alcanzados con Copilot y MCP

### 🎯 Análisis de Arquitectura de Servicios

Con la integración de **GitHub Copilot** y **Model Context Protocol (MCP)**, hemos logrado:

1. **Gestión de Base de Datos de Servicios**
   - Consulta automática de base de datos SQLite (`arquitectura.db`)
   - Extracción de metadatos de servicios y dependencias
   - Análisis de estados de operación (Activo/Mantenimiento)

2. **Generación Automática de Diagramas Mermaid**
   - Creación de diagramas de flujo en formato `graph TD`
   - Visualización de dependencias entre servicios
   - Representación visual de riesgos y puntos críticos

3. **Análisis de Riesgo de Impacto**
   - **Identificación visual**: Servicios críticos en Mantenimiento (coloreados en rojo)
   - **Evaluación de cascadas de fallos**: Cómo falla de un servicio afecta a otros
   - **Mapeo de dependencias**: Comprensión clara de relaciones entre componentes
   - Archivo: [servicios_diagram.mmd](servicios_diagram.mmd)

### 📊 Arquitectura Actual de Servicios

El sistema consta de 4 servicios con la siguiente estructura:

- **Frontend** → Capa de presentación del usuario
- **API Gateway** → Punto de entrada centralizado (Activo)
- **Auth Service** → Gestión de autenticación y usuarios (🔴 En Mantenimiento)
- **User DB** → Base de datos de usuarios (Activo)

**Hallazgos Críticos:**
- El Auth Service es un **punto de fallo crítico** mientras esté en Mantenimiento
- Bloquea el flujo completo de autenticación
- Afecta tanto al API Gateway como al Frontend

## Skills MCP Integradas

### Skill 1: Auditor de Código (Filesystem MCP) 🔍

**Problema Real**: La base de datos de arquitectura dice una cosa, pero el código fuente (docker-compose.yml) dice otra. Esto se llama **"deriva arquitectónica"** (architectural drift).

**Utilidad**: El agente puede leer archivos locales del proyecto y compararlos con la base de datos para detectar inconsistencias automáticamente.

**Servidor Configurado**: `auditor-archivos`

### Skill 2: Investigador Externo (Fetch MCP) 🌐

**Problema Real**: A veces la documentación necesita nutrirse de fuentes externas, como status pages de proveedores o estándares publicados.

**Utilidad**: El agente puede hacer peticiones web para leer contenido de internet e incorporarlo al análisis.

**Servidor Configurado**: `lector-web`

## Configuración de Servidores MCP

El archivo [.vscode/mcp.json](.vscode/mcp.json) está configurado con tres servidores:

```json
{
  "servers": {
    "arquitectura-db": "@modelcontextprotocol/server-sqlite",
    "auditor-archivos": "@modelcontextprotocol/server-filesystem",
    "lector-web": "@modelcontextprotocol/server-fetch"
  }
}
```

**Después de guardar, reinicia los servidores MCP desde el chat de Copilot.**

## Caso de Uso: Detección de Inconsistencias + Diagrama

Se ha creado un archivo de prueba [docker-compose.yml](docker-compose.yml) que incluye un servicio **Redis** que **NO está documentado en la base de datos**. Esto demuestra la "deriva arquitectónica".

### El "Mega Prompt" para Demostración

Copia y pega esto en el chat de Copilot con `@workspace`:

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

### Resultado Esperado

El agente debería:
1. ✅ Consultar `arquitectura.db` y obtener: Frontend, API Gateway, Auth Service, User DB
2. ✅ Leer `docker-compose.yml` y obtener: frontend, api-gateway, auth-service, user-db, **redis-cache**
3. ✅ Detectar que **Redis** no está en la BD
4. ✅ Generar un diagrama Mermaid con Redis en rojo para revisión

### ¿Por qué esto impresiona?

Esto demuestra **orquestación de herramientas avanzada**:
- ✅ Consulta SQL (base de datos)
- ✅ Lectura de archivos locales (sistema de archivos)
- ✅ Análisis lógico y comparación
- ✅ Generación de visualizaciones (Mermaid)

No es solo "autocompletar código", es un **agente inteligente que usa múltiples herramientas en secuencia** para resolver problemas reales.

## Instalación

Instrucciones para instalar y configurar el proyecto. Por ejemplo:

```bash
git clone https://github.com/usuario/repositorio.git
cd repositorio
npm install
```

## Uso

Ejemplos de cómo usar el proyecto. Incluye comandos o código de ejemplo.

```bash
npm start
```

## Tecnologías y Herramientas Utilizadas

- **GitHub Copilot**: Asistente de IA para análisis automático de arquitectura
- **Model Context Protocol (MCP)**: Integración de capacidades avanzadas de procesamiento
- **SQLite**: Base de datos de servicios (`arquitectura.db`)
- **Mermaid**: Generación de diagramas visuales (`graph TD`)
- **Python**: Scripts de consulta y análisis de datos
- **VS Code**: Editor y entorno de desarrollo

## Contribución

Cómo contribuir al proyecto. Por ejemplo, abre issues o pull requests.

## Licencia

Especifica la licencia bajo la cual se distribuye el proyecto (ej. MIT).
