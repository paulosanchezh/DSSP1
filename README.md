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
