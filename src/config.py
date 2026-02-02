# =========================
# CONFIGURAÇÕES GERAIS
# =========================

# Fonte de dados
IBGE_URL_TABELA_6579 = "https://apisidra.ibge.gov.br/values/t/6579/n3/all/p/all/v/all"

# Retry / Timeout
MAX_RETRIES = 3
TIMEOUT = 10


# =========================
# CAMADA BRONZE
# =========================
BRONZE_TABLE_6579 = "bronze_tabela_6579"


# =========================
# CAMADA SILVER
# =========================
SILVER_TABLE_6579 = "silver_tabela_6579"


# =========================
# CAMADA GOLD
# =========================
GOLD_TABLE_6579 = "gold_tabela_6579"
