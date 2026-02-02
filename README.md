# ibge-sidra
Este projeto tem como objetivo a implementação de um pipeline de dados analítico ponta a ponta, utilizando dados públicos da API SIDRA do IBGE, especificamente a tabela 6579. A solução foi desenvolvida com foco em consumo analítico, seguindo o padrão de arquitetura medalhão (Bronze, Silver e Gold). Especificamente para o processo seletivo CNI

A ingestão dos dados é realizada diretamente a partir da API pública do IBGE, com a implementação de mecanismos de retry e failover, garantindo maior resiliência em caso de indisponibilidade da fonte. Os dados brutos são persistidos na camada Bronze utilizando Delta Lake, preservando o formato original e permitindo reprocessamentos futuros.

Nas camadas subsequentes (Silver e Gold), os dados são tratados, padronizados e agregados, tornando-se adequados para análises exploratórias, consultas analíticas e integração com ferramentas de visualização. A solução foi implementada no Databricks Free Edition, respeitando suas limitações operacionais

## Arquitetura da Solução

### Bronze – Dados Brutos

A camada Bronze é responsável pela ingestão dos dados brutos diretamente da API SIDRA do IBGE (tabela 6579).
Nesta etapa:

- Os dados são coletados no formato original, sem transformações estruturais nos dados de negócio

- É aplicado um mecanismo de `retry` para lidar com falhas temporárias da API

- Em caso de indisponibilidade da fonte, é utilizado como failover o último snapshot persistido na própria camada Bronze
- Remoção do registro de cabeçalho( primeira linha) retornado pela API, que contém apenas descrições das dimensões e não representa uma observação válida
- Durante a ingestão, são adicionados metadados técnicos de controle, incluindo:
  -     ingestion_timestamp: data e hora da ingestão dos dados
  -     ingestion_source: identificação da origem da carga (API ou fallback)

  

- Os dados são armazenados em tabelas Delta gerenciadas, garantindo persistência e possibilidade de reprocessamento.Nenhuma regra de negócio ou agregação é aplicada na camada Bronze.

Essa camada tem como objetivo preservar a fidelidade dos dados de origem e permitir auditoria e reaproveitamento futuro.

### Silver – Tratamento e Padronização dos Dados

A camada Silver é responsável por transformar os dados brutos ingeridos da API SIDRA (IBGE) em um conjunto de dados estruturado, confiável e pronto para análises exploratórias e agregações.

Nesta etapa, os dados provenientes da camada Bronze passam por processos de limpeza, padronização e enriquecimento semântico, mantendo rastreabilidade por meio de metadados de ingestão.

#### Tratamentos Aplicados
1- ***Seleção de colunas relevantes***
  
  Foram selecionados apenas os campos necessários para consumo analítico, descartando metadados técnicos não utilizados.

2- ***Renomeação semântica de campos***

  Os nomes originais retornados pela API (ex.: D3N, D2N, V) foram renomeados para nomes mais descritivos, como:

    > localidade

    > periodo
    
    > valor

    > unidade_medida
    
3- ***Manutenção de metadados de ingestão***
  
   Os campos **ingestion_source** e **ingestion_timestamp** foram preservados, permitindo rastreabilidade e auditoria do processo de ingestão.
   
4- ***Conversão de tipos de dados***
  
  O campo de valor numérico, originalmente representado como texto, foi convertido para o tipo DOUBLE, permitindo cálculos e agregações.

5- ***Tratamento de registros malformados***
  
  Durante a conversão de tipos, foi utilizado `try_cast` para tolerar registros inválidos ou malformados (ex.: textos ou símbolos), convertendo-os para NULL sem interromper o pipeline.

6- ***Validação básica de qualidade***
  
  Registros com valores numéricos inválidos foram identificados e filtrados, garantindo consistência dos dados disponíveis para análise.

#### Persistência dos Dados

Os dados tratados são armazenados como tabelas Delta gerenciadas, garantindo:

- Persistência confiável

- Compatibilidade com o Databricks Free Edition

- Facilidade de reprocessamento e evolução do pipeline

#### Objetivo da Camada Silver

O resultado da camada Silver é um conjunto de dados:

- Estruturado

- Tipado corretamente

- Consistente

- Pronto para uso em agregações e análises na camada Gold

### Gold – Consumo Analítico

## Organização da Solução

A separação das camadas é refletida tanto:

- Na organização dos notebooks no Databricks (Bronze, Silver e Gold)

- Quanto nas tabelas Delta criadas para cada camada

Facilitando a manutenção, evolução do pipeline e a compreensão da arquitetura por diferentes perfis técnicos.

## Observação sobre o ambiente

Devido às restrições do *Databricks Free Edition*, o armazenamento e o controle de versões dos dados são realizados exclusivamente por meio de tabelas *Delta gerenciadas*, sem dependência de acesso direto ao filesystem (DBFS). Essa decisão garante compatibilidade com o ambiente e mantém as boas práticas de engenharia de dados.
