# ibge-sidra
Este projeto tem como objetivo a implementação de um pipeline de dados analítico ponta a ponta, utilizando dados públicos da API SIDRA do IBGE, especificamente a tabela 6579. A solução foi desenvolvida com foco em consumo analítico, seguindo o padrão de arquitetura medalhão (Bronze, Silver e Gold). Especificamente para o processo seletivo CNI

A ingestão dos dados é realizada diretamente a partir da API pública do IBGE, com a implementação de mecanismos de retry e failover, garantindo maior resiliência em caso de indisponibilidade da fonte. Os dados brutos são persistidos na camada Bronze utilizando Delta Lake, preservando o formato original e permitindo reprocessamentos futuros.

Nas camadas subsequentes (Silver e Gold), os dados são tratados, padronizados e agregados, tornando-se adequados para análises exploratórias, consultas analíticas e integração com ferramentas de visualização. A solução foi implementada no Databricks Free Edition, respeitando suas limitações operacionais

## Arquitetura da Solução

### Bronze – Dados Brutos

A camada Bronze é responsável pela ingestão dos dados brutos diretamente da API SIDRA do IBGE (tabela 6579).
Nesta etapa:

- Os dados são coletados no formato original, sem transformações estruturais

- É aplicado um mecanismo de retry para lidar com falhas temporárias da API

- Em caso de indisponibilidade da fonte, é utilizado como failover o último snapshot persistido na própria camada Bronze

- Os dados são armazenados em tabelas Delta gerenciadas, garantindo persistência e possibilidade de reprocessamento

Essa camada tem como objetivo preservar a fidelidade dos dados de origem e permitir auditoria e reaproveitamento futuro.

### Silver – Dados Tratados

### Gold – Consumo Analítico

## Organização da Solução

A separação das camadas é refletida tanto:

- Na organização dos notebooks no Databricks (Bronze, Silver e Gold)

- Quanto nas tabelas Delta criadas para cada camada

Facilitando a manutenção, evolução do pipeline e a compreensão da arquitetura por diferentes perfis técnicos.

## Observação sobre o ambiente

Devido às restrições do *Databricks Free Edition*, o armazenamento e o controle de versões dos dados são realizados exclusivamente por meio de tabelas *Delta gerenciadas*, sem dependência de acesso direto ao filesystem (DBFS). Essa decisão garante compatibilidade com o ambiente e mantém as boas práticas de engenharia de dados.
