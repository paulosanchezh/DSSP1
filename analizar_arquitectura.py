import sqlite3
import json
import yaml
from pathlib import Path

# ============================================
# SKILL 1: Auditor de Código - Leer BD
# ============================================
print("=" * 60)
print("🔍 SKILL 1: AUDITOR DE CÓDIGO - BASE DE DATOS")
print("=" * 60)

conn = sqlite3.connect('arquitectura.db')
cursor = conn.cursor()

cursor.execute("SELECT id, nombre, depende_de, estado FROM servicios")
servicios_db = cursor.fetchall()
conn.close()

print("\n📊 Servicios en ARQUITECTURA.DB:")
servicios_dict = {}
for sid, nombre, depende_de, estado in servicios_db:
    servicios_dict[nombre.lower()] = {
        'nombre': nombre,
        'depende_de': depende_de,
        'estado': estado,
        'id': sid
    }
    emoji = "✅" if estado == "Activo" else "🔴"
    print(f"  {emoji} {nombre:20} | Estado: {estado:15} | Depende de: {depende_de}")

# ============================================
# SKILL 2: Auditor de Código - Leer Archivos Locales
# ============================================
print("\n" + "=" * 60)
print("📁 SKILL 1 (Cont.): AUDITOR DE ARCHIVOS - DOCKER-COMPOSE.YML")
print("=" * 60)

with open('docker-compose.yml', 'r') as f:
    docker_config = yaml.safe_load(f)

servicios_docker = list(docker_config['services'].keys())
print("\n🐳 Servicios en DOCKER-COMPOSE.YML:")
for svc in servicios_docker:
    print(f"  ✓ {svc}")

# ============================================
# ANÁLISIS COMPARATIVO
# ============================================
print("\n" + "=" * 60)
print("⚖️ ANÁLISIS COMPARATIVO: BD vs DOCKER-COMPOSE")
print("=" * 60)

# Normalizar nombres para comparación
servicios_db_names = [s['nombre'].lower().replace(' ', '-') for s in servicios_dict.values()]
servicios_docker_lower = [s.lower() for s in servicios_docker]

print(f"\nServicios en BD: {servicios_db_names}")
print(f"Servicios en Docker: {servicios_docker_lower}")

# Encontrar inconsistencias
inconsistencias = []
servicios_no_documentados = []

for svc_docker in servicios_docker_lower:
    # Buscar coincidencia
    encontrado = False
    for svc_db in servicios_db_names:
        if svc_docker in svc_db or svc_db in svc_docker:
            encontrado = True
            break

    if not encontrado:
        inconsistencias.append(svc_docker)
        servicios_no_documentados.append(svc_docker)
        print(f"\n🚨 INCONSISTENCIA DETECTADA:")
        print(f"   ❌ '{svc_docker}' está en docker-compose.yml pero NO en arquitectura.db")

if not inconsistencias:
    print("\n✅ No hay inconsistencias. Todos los servicios están documentados.")

# ============================================
# GENERAR DIAGRAMA MERMAID
# ============================================
print("\n" + "=" * 60)
print("📈 GENERANDO DIAGRAMA MERMAID")
print("=" * 60)

mermaid_code = "graph TD\n"

# Agregar nodos de BD
for nombre, datos in servicios_dict.items():
    node_id = nombre.upper().replace(' ', '_')
    mermaid_code += f'    {node_id}["{datos["nombre"]}"]\n'

# Agregar nodos de servicios no documentados
for svc in servicios_no_documentados:
    node_id = svc.upper().replace('-', '_').replace(' ', '_')
    display_name = svc.replace('-', ' ').title()
    mermaid_code += f'    {node_id}["{display_name}"]\n'

mermaid_code += "\n"

# Agregar dependencias de BD
for nombre, datos in servicios_dict.items():
    if datos['depende_de'] and datos['depende_de'] != 'Ninguno':
        node_id = nombre.upper().replace(' ', '_')
        deps = [d.strip().lower().replace(' ', '_').upper() for d in datos['depende_de'].split(',')]
        for dep in deps:
            mermaid_code += f'    {node_id} --> {dep}\n'

mermaid_code += "\n"

# Colorear servicios según estado
for nombre, datos in servicios_dict.items():
    node_id = nombre.upper().replace(' ', '_')
    if datos['estado'] == 'Mantenimiento':
        mermaid_code += f'    style {node_id} fill:#ff6b6b,stroke:#c92a2a,color:#fff\n'
    else:
        mermaid_code += f'    style {node_id} fill:#51cf66,stroke:#2f9e44,color:#fff\n'

# Colorear servicios no documentados en amarillo
for svc in servicios_no_documentados:
    node_id = svc.upper().replace('-', '_').replace(' ', '_')
    mermaid_code += f'    style {node_id} fill:#ffd43b,stroke:#f08c00,color:#000\n'

# Guardar diagrama
with open('arquitectura_completa.mmd', 'w') as f:
    f.write(mermaid_code)

print("\n✅ Diagrama generado: arquitectura_completa.mmd")
print("\n" + "=" * 60)
print("📊 CÓDIGO MERMAID GENERADO:")
print("=" * 60)
print(mermaid_code)

# ============================================
# RESUMEN FINAL
# ============================================
print("\n" + "=" * 60)
print("📋 RESUMEN DE RESULTADOS")
print("=" * 60)
print(f"\n✅ Servicios Documentados (en BD):     {len(servicios_dict)}")
print(f"✅ Servicios en docker-compose.yml:   {len(servicios_docker)}")
print(f"⚠️  Servicios No Documentados:        {len(inconsistencias)}")

if inconsistencias:
    print(f"\n🚨 SERVICIOS QUE REQUIEREN DOCUMENTACIÓN:")
    for svc in inconsistencias:
        print(f"   - {svc}")
    print("\n💡 ACCIÓN RECOMENDADA:")
    print("   Actualiza arquitectura.db para incluir estos servicios")
else:
    print("\n✅ ¡Arquitectura consistente! No hay servicios no documentados.")

print("\n" + "=" * 60)
