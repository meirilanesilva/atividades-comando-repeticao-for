# Atividade 2 - Relatório de Inventário

inventario = [
    {"id": 101, "modelo": "Notebook i5", "status": "ativo"},
    {"id": 102, "modelo": "Desktop i3", "status": "manutenção"},
    {"id": 103, "modelo": "Notebook i7", "status": "ativo"},
    {"id": 104, "modelo": "Servidor Dell", "status": "ativo"}
]

print("=== Relatório de Máquinas Ativas ===")

for maquina in inventario:
    if maquina["status"] == "ativo":
        print(f"ID: {maquina['id']} | Modelo: {maquina['modelo']} | Status: {maquina['status']}")
