# Projeto de Estatística Aplicada

## 🧑‍💻 Autores  
- Maria Eduarda Pereira de Souza Melo (202111250025) - melo.eduarda@academico.ifpb.edu.br
- Gislany Dias (202111250037) - gislany.dias@academico.ifpb.edu.br

## 🎯 Tema e Motivação  
Nosso projeto busca explorar o desempenho dos modelos de carros autônomos utilizados em pistas simuladas por meio dos dados coletados em corridas da comunidade AWS DeepRacer. A motivação principal surgiu a partir da nossa recente participação em um desafio do AWS DeepRacer, onde tivemos contato direto com os conceitos de simulação, inteligência artificial e otimização de trajetórias.
Percebemos que esses dados oferecem uma rica oportunidade de análise estatística, pois contêm informações sobre tempos de volta, comportamento dos modelos, características das pistas e condições das corridas. Isso nos instigou a investigar padrões e possíveis fatores que influenciam diretamente o desempenho dos agentes, permitindo uma aplicação prática da estatística em um contexto de aprendizado de máquina e robótica.

## 📊 Conjunto de Dados Selecionado  
- **Nome do conjunto de dados:**  
 AWS DeepRacer Community Race Data


- **Fonte:**  
 https://github.com/aws-deepracer-community/deepracer-race-data

- **Descrição breve:**  
O conjunto de dados reúne informações de corridas realizadas pela comunidade do AWS DeepRacer. Ele abrange múltiplas temporadas e pistas, com variáveis como tempo de volta, nome da pista, data da corrida, nome dos participantes, entre outras. O escopo é global e cobre diferentes momentos entre 2019 e 2023. A base é composta por arquivos CSV organizados por temporada, refletindo o desempenho de modelos de carros autônomos em simulações baseadas em reforço.

- **Justificativa para a escolha:**  
Escolhemos essa base por seu potencial de gerar análises estatísticas descritivas e inferenciais interessantes, como a variação do tempo médio por pista, consistência dos participantes ao longo do tempo, e comparações entre temporadas. Além disso, é uma base com relevância prática para quem estuda inteligência artificial, controle autônomo e análise de desempenho em sistemas de simulação. O projeto também nos permite conectar conhecimentos técnicos de engenharia com métodos quantitativos.
---

## ❓ Perguntas ou Hipóteses  
- Qual é o tempo médio das voltas (AvgLapTime) por pista e como ele varia entre os participantes?
Objetivo: Identificar diferenças de desempenho médio entre participantes e pistas.

- Participantes com menos colisões (CollisionCount) tendem a ter melhores tempos de volta (BestLapTime)?
Hipótese: Existe uma correlação negativa entre número de colisões e o melhor tempo de volta.

- O número médio de resets (AvgResets) influencia negativamente o ranking final (Rank)?
Hipótese: Um maior número médio de resets está associado a posições mais baixas no ranking.

- Qual é a distribuição do tempo total de corrida (TotalLapTime) e existem outliers?
Objetivo: Explorar possíveis exceções ou desempenhos fora do padrão.

- Existe uma tendência de melhoria nos tempos médios (AvgLapTime) conforme o número de submissões aumenta (SubmissionCount)?
Hipótese: Participantes com mais submissões tendem a ter melhor desempenho médio.

- Qual é a relação entre o número total de voltas (LapCount) e a posição no ranking (Rank)?
Objetivo: Investigar se participantes que completaram mais voltas se saíram melhor.

- Participantes com maior quantidade de saídas da pista (OffTrackCount) têm pior pontuação de ranking (RankingScore)?
Hipótese: Maior quantidade de saídas da pista está relacionada a pior desempenho no ranking.

## 🔍 Metodologia  
*A preencher na próxima etapa.*  
Indique quais técnicas estatísticas serão utilizadas (análise exploratória, testes, correlações, modelos, etc.).

## 🛠️ Ferramentas Utilizadas  
*A preencher na próxima etapa.*  
Quais linguagens, bibliotecas ou softwares serão utilizados no projeto.

## 📈 Resultados  
*A preencher após as análises.*  
Resumo visual e interpretativo dos principais achados.

## 📌 Conclusões  
*A preencher no final do projeto.*  
Síntese dos aprendizados e implicações das análises realizadas.

## ⚠️ Limitações e Trabalhos Futuros  
*A preencher no final do projeto.*  
Quais foram as limitações do estudo e o que poderia ser feito com mais tempo ou dados adicionais.

---

