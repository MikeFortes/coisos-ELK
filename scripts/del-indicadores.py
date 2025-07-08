# Script criado para deletar todo documentos do índice ".ds-winlogbeat-9.0.1-2025.06.03-000001" que tenham um campo @timestamp anterior a 5 dias atrás.

import requests
from datetime import datetime, timedelta

# Configurações
ELASTIC_URL = "http://localhost:9200"
INDEX = ".ds-winlogbeat-9.0.1-2025.06.03-000001"
auth = ("usuario", "senha")

# Calcular data de corte (5 dias atrás em formato ISO)
data_corte = (datetime.utcnow() - timedelta(days=5)).isoformat() + "Z"

# Query para deletar documentos com @timestamp < 5 dias atrás
query = {
  "query": {
    "range": {
      "@timestamp": {
        "lt": data_corte
      }
    }
  }
}

# Enviar requisição
resp = requests.post(
    f"{ELASTIC_URL}/{INDEX}/_delete_by_query",
    json=query,
    auth=auth,
    headers={"Content-Type": "application/json"}
)

print(f"Status: {resp.status_code}")
print(f"Resposta: {resp.text}")

