

# 🚀 AgroRisk-AI

## 📊 Estruturação dos Dados

### 📌 Definição dos Dados

Foi desenvolvido um conjunto de dados simulado representando condições reais de operação de máquinas agrícolas, com foco na previsão de risco de atolamento em áreas próximas a corpos d’água após períodos de chuva.

As variáveis foram definidas com base em fatores ambientais e operacionais que influenciam diretamente esse risco, permitindo representar diferentes cenários de operação.

---

### 🧠 Organização das Variáveis

As variáveis foram organizadas em cinco categorias principais:

- **Clima**: chuva acumulada e temperatura  
- **Solo**: tipo e umidade do solo  
- **Localização**: distância até corpos d’água  
- **Operação**: peso do equipamento, tipo de pneu e horário da operação  
- **Histórico**: ocorrências anteriores de atolamento  

---

### 🧾 Tabela de Variáveis

| Variável | Tipo | Unidade | Descrição | Faixa Esperada |
|----------|------|--------|----------|----------------|
| chuva_72h | Numérico | mm | Chuva acumulada nas últimas 72 horas | 0 – 120 |
| tipo_solo | Categórico | - | Tipo de solo (argiloso, arenoso, franco, misto) | - |
| umidade_solo | Numérico | % | Umidade estimada do solo | 20 – 100 |
| declividade | Numérico | % | Inclinação do terreno | 0 – 15 |
| distancia_agua | Numérico | m | Distância até corpo d’água mais próximo | 1 – 300 |
| peso_equipamento | Numérico | kg | Peso da máquina agrícola | 5000 – 15000 |
| tipo_pneu | Categórico | - | Tipo de pneu (esteira, padrão, alta flutuação) | - |
| hora_operacao | Numérico | hora | Hora do dia da operação | 0 – 23 |
| historico_atolamentos | Numérico | contagem | Ocorrências nos últimos 12 meses | 0 – 10 |
| temperatura | Numérico | °C | Temperatura ambiente | 10 – 40 |
| ocorrencia_atolamento | Binário | - | 0 = não atolou / 1 = atolou | - |

---

### 📄 Exemplo de Dataset Simulado

📁 Exemplo de dataset: [dataset_exemplo.csv](data/dataset_exemplo.csv)

---

### 🧠 Lógica dos Dados

Os dados foram simulados com base em relações plausíveis observadas no contexto agrícola:

- Maior volume de chuva → aumento da umidade do solo → maior risco  
- Solos argilosos → maior retenção de água → maior risco  
- Menor distância de corpos d’água → maior instabilidade do solo  
- Maior declividade do terreno → aumento do risco de instabilidade e atolamento  
- Maior peso da máquina → maior pressão sobre o solo  
- Tipo de pneu influencia diretamente a tração e estabilidade  
- Temperatura influencia indiretamente a umidade do solo  

A variável **ocorrencia_atolamento** representa o resultado final, sendo utilizada como variável alvo para um problema de **classificação de risco em IA supervisionada**.

---

### 📈 Cenários de Risco

Com base nas relações definidas no dataset, alguns cenários apresentam maior probabilidade de atolamento:

- Se **chuva_72h alta** e **umidade_solo elevada** → maior risco  
- Se **tipo_solo = argiloso** → maior retenção de água  
- Se **distancia_agua baixa** → solo mais saturado  
- Se **declividade elevada** → maior instabilidade do terreno  
- Se **peso_equipamento alto** em solo úmido → maior pressão  

Essas condições não são regras fixas, mas representam padrões que aumentam a probabilidade de ocorrência de atolamento.

---

## 🔎 Origem dos Dados Simulados

Os dados são simulados, mas baseados em padrões plausíveis do mundo real.

Foram considerados:

- volumes de chuva típicos de dados meteorológicos  
- comportamento de diferentes tipos de solo  
- características operacionais de máquinas agrícolas  

As faixas foram definidas para representar condições realistas de operação, garantindo coerência para análise e modelagem.
