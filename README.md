# ibge-sidra
Este projeto tem como objetivo a implementação de um pipeline de dados analítico ponta a ponta, utilizando dados públicos da API SIDRA do IBGE, especificamente a tabela 6579. A solução foi desenvolvida com foco em consumo analítico, seguindo o padrão de arquitetura medalhão (Bronze, Silver e Gold). Especificamente para o processo seletivo CNI

A ingestão dos dados é realizada diretamente a partir da API pública do IBGE, com a implementação de mecanismos de retry e failover, garantindo maior resiliência em caso de indisponibilidade da fonte. Os dados brutos são persistidos na camada Bronze utilizando Delta Lake, preservando o formato original e permitindo reprocessamentos futuros.

Nas camadas subsequentes (Silver e Gold), os dados são tratados, padronizados e agregados, tornando-se adequados para análises exploratórias, consultas analíticas e integração com ferramentas de visualização. A solução foi implementada no Databricks Free Edition, respeitando suas limitações operacionais

## Arquitetura da Solução

### Bronze – Dados Brutos

### Silver – Dados Tratados

### Gold – Consumo Analítico
