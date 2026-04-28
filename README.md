

# 🌾 AgroRisk AI

## 📌 Descrição do Problema

O setor agrícola enfrenta desafios significativos relacionados à previsibilidade de riscos operacionais no uso de equipamentos. Atualmente, muitas decisões ainda são tomadas de forma reativa, ou seja, após a ocorrência de falhas, acidentes ou danos.

Situações como operação em solo instável após períodos de chuva, proximidade com corpos d’água e transporte em terrenos irregulares aumentam significativamente o risco de:

* Atolamento de máquinas
* Danos mecânicos
* Acidentes operacionais
* Perda total de equipamentos

A ausência de sistemas inteligentes que integrem dados ambientais e operacionais dificulta a prevenção desses riscos, gerando prejuízos financeiros, operacionais e até impactos ambientais.

---

## 💡 Solução Proposta

O **AgroRisk AI** é uma solução baseada em dados e Inteligência Artificial que tem como objetivo prever riscos operacionais antes da execução de atividades agrícolas.

O sistema analisa variáveis ambientais e operacionais para gerar um **Risk Score (0 a 100)** e classificar o nível de risco em:

* 🟢 Baixo risco
* 🟡 Médio risco
* 🔴 Alto risco

Além disso, o sistema fornece recomendações como:

* Adiar operação
* Alterar rota
* Reduzir carga da máquina

Essa abordagem permite transformar decisões reativas em ações preventivas, reduzindo custos e aumentando a eficiência operacional.

---

## 👤 Personas

### 👨‍🌾 Operador

* Precisa saber se é seguro operar o equipamento
* Recebe alertas antes da execução da atividade
* Toma decisões rápidas em campo

### 👨‍💼 Gestor Agrícola

* Planeja operações e alocação de máquinas
* Busca reduzir custos com manutenção e falhas
* Precisa de visão estratégica dos riscos

### 🏢 Seguradora (Sompo)

* Interesse em prever sinistros
* Avalia riscos para precificação de seguros
* Busca reduzir prejuízos com indenizações

---

## 📊 Estruturação dos Dados

O sistema utiliza dados simulados que representam condições reais de operação agrícola.

### Principais variáveis:

| Variável          | Descrição                                   |
| ----------------- | ------------------------------------------- |
| rainfall          | Volume de chuva recente (mm)                |
| soil_moisture     | Umidade do solo (%)                         |
| slope             | Inclinação do terreno                       |
| distance_to_water | Distância de rios ou lagos (m)              |
| machine_age       | Idade do equipamento (anos)                 |
| operation_type    | Tipo de operação (colheita/transporte)      |
| risk              | Classificação de risco (baixo, médio, alto) |

📁 Dataset disponível em: `data/sample_dataset.csv`

---

## 🏗️ Arquitetura da Solução

O sistema segue o seguinte fluxo de dados:

1. Coleta de dados

   * APIs de clima
   * Sensores (simulados)
   * Histórico de operações

2. Processamento

   * Limpeza e organização dos dados

3. Modelo de IA

   * Análise das variáveis
   * Geração de score de risco

4. Saída

   * Dashboard
   * Alertas e recomendações

📊 Diagrama disponível em: `docs/architecture.png`

---

## 🤖 Proposta do Modelo Preditivo

O modelo proposto é baseado em **classificação de risco**.

### Entrada:

* Dados ambientais (clima, solo)
* Dados operacionais (tipo de operação)
* Histórico do equipamento

### Saída:

* Classificação: Baixo / Médio / Alto
  OU
* Score de risco (0 a 100)

### Justificativa:

A classificação permite decisões rápidas e intuitivas para operadores e gestores, facilitando a prevenção de riscos.

---

## 🖥️ Interface da Solução

O sistema contará com um dashboard que apresenta:

* Score de risco em tempo real
* Indicadores visuais por cores
* Alertas automáticos
* Recomendações operacionais

---

## 🔐 Segurança

* Controle de acesso por perfil de usuário
* Proteção de dados em ambiente seguro
* Registro de logs de operação
* Garantia de integridade dos dados

---

## 📅 Planejamento das Próximas Etapas

### Sprint 2:

* Criação do dataset completo
* Implementação inicial do modelo de IA

### Sprint 3:

* Desenvolvimento do dashboard
* Integração dos dados

### Sprint Final:

* Protótipo funcional
* Testes e validação

---

## 👥 Divisão de Tarefas

* Pessoa 1: Documentação e personas
* Pessoa 2: Dados e dataset
* Pessoa 3: Modelo preditivo
* Pessoa 4: Arquitetura e segurança
* Pessoa 5: Repositório, README, vídeo e gestão

---

## 📂 Estrutura do Projeto

```
AgroRisk-AI/
│
├── README.md
├── data/
├── docs/
├── presentation/
└── video/
```

---

## 🎥 Vídeo de Apresentação

📌 Link do vídeo: (adicionar link aqui)

---

## 🚀 Conclusão

O AgroRisk AI propõe uma abordagem inovadora para o setor agrícola, utilizando dados e Inteligência Artificial para antecipar riscos e melhorar a tomada de decisão.

A solução contribui para a redução de prejuízos, aumento da eficiência operacional e maior segurança no uso de equipamentos agrícolas.

