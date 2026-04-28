

# AgroRisk AI

## 1. Descrição do Problema

A operação de equipamentos agrícolas pesados (colheitadeiras, tratores, pulverizadores) está sujeita a riscos operacionais que hoje são tratados de forma reativa: o problema acontece, gera prejuízo, e só então há aprendizado. Uma colheitadeira atolada em solo encharcado pode gerar dezenas de milhares de reais em despesas de resgate, atrasar a janela de colheita e, em casos extremos, resultar em perda total do equipamento.

O cenário escolhido como foco é o de atolamento ou tombamento de colheitadeira em operação próxima a corpos d'água após períodos de chuva. Esse cenário concentra os fatores de risco mais relevantes do desafio: condição climática recente, tipo e umidade do solo, proximidade de água, declividade do terreno e características do equipamento.
Hoje o operador decide se entra ou não na lavoura com base em experiência e observação visual. Isso funciona em condições óbvias (solo claramente alagado), mas falha nos casos limítrofes — solo aparentemente firme na superfície mas instável em profundidade. É nesses casos que mora a maior parte das ocorrências evitáveis.

Impactos:

- Custos de resgate e reparo 
- Atraso na janela operacional, impactando produtividade da safra
- Aumento de sinistralidade para a seguradora, refletindo em prêmios mais altos
- Risco à segurança do operador em tombamentos

---

## 2. Solução Proposta

Um score de risco operacional de 0 a 100 entregue ao operador antes do início da operação, calculado a partir de variáveis ambientais, características da gleba e perfil do equipamento. O score vem acompanhado de classificação (Baixo / Médio / Alto) e de uma recomendação objetiva (proceder, ajustar rota, adiar).

O que o sistema entrega:

- **Para o operador**: alerta no app antes de iniciar a operação, com score, nível e recomendação
- **Para o gestor**: visão consolidada de todas as glebas e equipamentos, permitindo priorizar áreas de menor risco
- **Para a seguradora**: dados agregados e anonimizados para refinar cálculo de prêmio e identificar padrões de sinistralidade

Tipo de saída:

- Score numérico de 0 a 100
- Classificação categórica (Baixo / Médio / Alto)
- Recomendação textual (ex.: "Risco alto — recomenda-se adiar 48h ou redirecionar para gleba norte")
- Lista dos fatores que mais contribuíram para o score (explicabilidade)

---

## 3. Personas

### Persona 1 - Operador de Colheitadeira

Profissional que opera o equipamento em campo. Experiência prática consolidada, decisões de curto prazo sob pressão de janela operacional. Precisa de informação rápida e clara antes de entrar na lavoura, recomendação objetiva (vai / não vai / ajusta rota), e confiança de que o sistema considera as condições reais do dia. A solução entrega um alerta visual simples no app antes de ligar o equipamento, reduzindo a chance de entrar em área de risco que não estava óbvia visualmente.

### Persona 2 - Gestor da Fazenda

Responsável pelo planejamento operacional da propriedade. Coordena múltiplos equipamentos, operadores e glebas. Pensa na janela de colheita, custo e cronograma. Precisa de visão consolidada do risco em todas as glebas, capacidade de priorizar quais áreas operar primeiro, e histórico de eventos para aprender padrões da propriedade. A solução entrega um dashboard com mapa de risco da fazenda, filtros por equipamento e gleba, permitindo replanejar a ordem das operações.

### Persona 3 - Analista de Risco da Seguradora

Profissional da Sompo, responsável por avaliar exposição ao risco e calcular prêmios. Trabalha com dados agregados. Precisa de dados anonimizados sobre padrões de risco por região, tipo de solo e equipamento, indicadores de sinistralidade preditiva, e evidência de que clientes que usam a solução têm menor sinistralidade. A solução entrega relatórios agregados e um painel analítico para cruzar fatores de risco com sinistralidade real.

---

## 4. Estruturação dos Dados

### 4.1 - Definição dos Dados

Foi desenvolvido um conjunto de dados simulado representando condições reais de operação de máquinas agrícolas, com foco na previsão de risco de atolamento em áreas próximas a corpos d’água após períodos de chuva.

As variáveis foram definidas com base em fatores ambientais e operacionais que influenciam diretamente esse risco, permitindo representar diferentes cenários de operação.

---

### 4.2 - Organização das Variáveis:

As variáveis foram organizadas em cinco categorias principais:

- **Clima**: chuva acumulada e temperatura  
- **Solo**: tipo e umidade do solo  
- **Localização**: distância até corpos d’água  
- **Operação**: peso do equipamento, tipo de pneu e horário da operação  
- **Histórico**: ocorrências anteriores de atolamento
  
---

### 4.3 - Tabela das Variáveis

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

### 4.4 - Exemplo de Dataset Simulado

Exemplo de dataset: data/dataset_exemplo.csv

---

### 4.5 - Lógica dos Dados

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

### 4.6 - Cenários de Risco

Com base nas relações definidas no dataset, alguns cenários apresentam maior probabilidade de atolamento:

- Se **chuva_72h alta** e **umidade_solo elevada** → maior risco  
- Se **tipo_solo = argiloso** → maior retenção de água  
- Se **distancia_agua baixa** → solo mais saturado  
- Se **declividade elevada** → maior instabilidade do terreno  
- Se **peso_equipamento alto** em solo úmido → maior pressão  

Essas condições não são regras fixas, mas representam padrões que aumentam a probabilidade de ocorrência de atolamento.

---

### 4. 7 - Origem dos Dados Simulados

Os dados são simulados, mas baseados em padrões plausíveis do mundo real.

Foram considerados:

- volumes de chuva típicos de dados meteorológicos  
- comportamento de diferentes tipos de solo  
- características operacionais de máquinas agrícolas  

As faixas foram definidas para representar condições realistas de operação, garantindo coerência para análise e modelagem.

---

## 5. Arquitetura da Solução

Fluxo simples do sistema (precisa da arquitetura pronta)

Diagrama disponível em: `docs/architecture.png`

---

## 6. Proposta do Modelo Preditivo

classificação de risco (precisa do modelo preditivo pronto) 

---

## 7. Interface da Solução

O sistema contará com um dashboard que apresenta:

- Score de risco em tempo real
- Indicadores visuais por cores
- Alertas automáticos
- Recomendações operacionais

  
🔍 Exemplo de visualização (wireframe simples)


|      AgroRisk AI Dashboard      |
|---------------------------------|
| 🔴 Risco: 82 (ALTO)             |
| 🌧 Clima: Chuva forte           |
| 🌱 Solo: Muito úmido            |
| 🚜 Operação: Colheita           |

| ⚠️ Recomendação: NÃO OPERAR     |


Esse exemplo ilustra como o usuário (operador ou gestor) visualizaria as informações e tomaria decisões com base nos alertas gerados pelo sistema.


---

## 8. Segurança

* Controle de acesso por perfil de usuário
* Proteção de dados em ambiente seguro
* Registro de logs de operação
* Garantia de integridade dos dados

---

## 9. Planejamento das Próximas Etapas

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

## 10. Divisão de Tarefas

* Pessoa 1: Documentação e personas
* Pessoa 2: Dados e dataset
* Pessoa 3: Modelo preditivo
* Pessoa 4: Arquitetura e segurança
* Pessoa 5: Repositório, README, vídeo e gestão

---

## 11. Estrutura do Projeto

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

## 12. Vídeo de Apresentação

📌 Link do vídeo: (adicionar link aqui)

---

## Conclusão

O AgroRisk AI propõe uma abordagem inovadora para o setor agrícola, utilizando dados e Inteligência Artificial para antecipar riscos e melhorar a tomada de decisão.

A solução contribui para a redução de prejuízos, aumento da eficiência operacional e maior segurança no uso de equipamentos agrícolas.

