import requests

# Configurações
ELASTIC_URL = "http://localhost:9200"  # Altere se necessário
INDEX_NAME = ".ds-winlogbeat-9.0.1-2025.06.03-000001"

# Endpoint de forcemerge
url = f"{ELASTIC_URL}/{INDEX_NAME}/_forcemerge?max_num_segments=1"

# (opcional) Autenticação básica
auth = ("usuario", "senha")  # Altere se seu cluster exigir login
# Se não precisar de autenticação, use: auth = None

# Envio da requisição POST
response = requests.post(url, auth=auth)

# Exibir resultado
print(f"Status: {response.status_code}")
print(f"Resposta: {response.text}")

