import sqlite3
import json

conn = sqlite3.connect('arquitectura.db')
cursor = conn.cursor()

# Obtener nombres de tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [t[0] for t in cursor.fetchall()]
print("Tablas disponibles:", tables)
print()

# Consultar cada tabla
for table in tables:
    cursor.execute(f"SELECT * FROM {table}")
    columns = [description[0] for description in cursor.description]
    rows = cursor.fetchall()
    print(f"=== Tabla: {table} ===")
    print(f"Columnas: {columns}")
    for row in rows:
        print(row)
    print()

conn.close()
