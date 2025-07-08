# Esse script realiza uma otimização de espaço em disco no Elasticsearch para o índice, usando compressão avançada e merge de segmentos.

import requests
import time

# Configurações
ELASTIC_URL = "http://localhost:9200"
INDEX_NAME = ".ds-winlogbeat-9.0.1-2025.06.03-000001"
auth = ("usuario", "senha")  # Substitua se necessário

headers = {"Content-Type": "application/json"}

# 1. Fecha o índice
print("Fechando o índice...")
resp_close = requests.post(f"{ELASTIC_URL}/{INDEX_NAME}/_close", auth=auth)
print(f"Fechamento: {resp_close.status_code} - {resp_close.text}")

# 2. Altera para best_compression
print("Alterando codec para 'best_compression'...")
settings_payload = {
    "settings": {
        "index.codec": "best_compression"
    }
}
resp_settings = requests.put(f"{ELASTIC_URL}/{INDEX_NAME}/_settings", json=settings_payload, auth=auth, headers=headers)
print(f"Settings: {resp_settings.status_code} - {resp_settings.text}")

# 3. Reabre o índice
print("Reabrindo o índice...")
resp_open = requests.post(f"{ELASTIC_URL}/{INDEX_NAME}/_open", auth=auth)
print(f"Abertura: {resp_open.status_code} - {resp_open.text}")

# (opcional) Espera um pouco antes do forcemerge
time.sleep(2)

# 4. Executa forcemerge
print("Executando forcemerge...")
resp_merge = requests.post(f"{ELASTIC_URL}/{INDEX_NAME}/_forcemerge?max_num_segments=1", auth=auth)
print(f"Forcemerge: {resp_merge.status_code} - {resp_merge.text}")
