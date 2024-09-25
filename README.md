# Sistema de Recomendações de Cuidados com Plantas

Este projeto apresenta um sistema desenvolvido em Python que fornece recomendações práticas para o cuidado de plantas, adaptadas às condições ambientais específicas em que elas estão inseridas. Com a crescente popularidade da jardinagem e a necessidade de cuidados adequados para garantir a saúde das plantas, um sistema que auxilia os usuários a entender as necessidades de suas plantas é de suma importância.

## Objetivo do Sistema

O objetivo deste sistema é facilitar o manejo das plantas, fornecendo dicas de rega e cuidados com base em variáveis ambientais como temperatura, umidade do solo, tipo de solo e exposição solar. O sistema visa apoiar tanto jardineiros iniciantes quanto experientes na manutenção saudável de suas plantas.

## Funcionalidades do Sistema

### Função `recomendar_cuidados`

O sistema possui a função `recomendar_cuidados`, que pega detalhes da planta e devolve duas listas: uma para dicas de cuidados e outra para opções de irrigação. As recomendações são formadas avaliando determinadas condições ambientais.

#### Detalhamento das Regras de Cuidados

- **Temperatura:**
  - Menor que 15°C: Evitar rega e utilizar coberturas para proteger as plantas do frio.
  - Maior que 30°C: Aumentar a frequência da rega e verificar a necessidade de sombreamento.

- **Umidade do Solo:**
  - Seco: Regar levemente e utilizar mulch para reter a umidade no solo.
  - Úmido: Evitar regar e certificar-se de que a drenagem está adequada.

- **Exposição Solar:**
  - Mais de 6 horas: Mover para uma área com sombra parcial e monitorar a umidade do solo.
  - Menos de 4 horas: Mover a planta para um local com mais exposição à luz e verificar sinais de estiolamento.

- **Tipo de Solo:**
  - Arenoso: Aumentar a frequência da rega e adicionar matéria orgânica para melhorar a retenção de água.
  - Argiloso: Evitar regar e certificar-se de que a planta não fique encharcada.
  - Siltoso: Regar moderadamente, monitorando a umidade.
  - Rochoso: Regar levemente e verificar drenagem, utilizando pedras para ajudar na drenagem.

- **Umidade do Ar:**
  - Menor que 40%: Regar levemente e considerar o uso de um umidificador.
  - Maior que 70%: Evitar regar e certificar-se de que a ventilação está adequada.

- **Estação do Ano:**
  - Inverno: Reduzir o uso de fertilizantes e proteger as plantas do frio.
  - Primavera: Aumentar o uso de fertilizantes e monitorar o crescimento das plantas.
  - Verão: Aumentar o uso de fertilizantes e verificar a necessidade de mais água.
  - Outono: Começar a reduzir o uso de fertilizantes e preparar as plantas para o inverno.

- **Poda:**
  - Recomenda-se a poda de folhas ou galhos secos durante a primavera e verão para estimular o crescimento de novos brotos.

### Função `decidir_rega`

Em seguida, o sistema fornece os melhores conselhos de rega com base na decisão mais frequente e em seu peso.

### Função `processar_dados`

Responsável por ler os dados inseridos, chama as funções de recomendação e decisão, e exibe os resultados ao usuário. Em caso de erros na conversão dos dados, uma mensagem de erro apropriada é exibida para orientação do usuário.
