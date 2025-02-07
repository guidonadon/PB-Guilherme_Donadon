# Etapas
### 1. Ingestão de Dados no AWS QuickSight
  ##### Após os processos realizados nas Sprints anteriores os datas frames agora já estavam preparados para que o Athena pudesse lê-los e então o utilizei para fazer a ingestão dos dados necessários. O método consiste em selecionar o Athena como meio de ligação, selecionar o banco de dados e a partir daí selecionar as tabelas que se deseja acidionar ao QuickSight.
![Ingestão de dados através do AWS Athena](../Evidencias/ligacao_athena.png)
### 2. Configuração dos Dados
  ##### Após realizada a ingestão de todos os dados, ao acessar a tela de conjuntos de dados a seguinte imagem foi exibida
![DataFrames adicionados](../Evidencias/conjuntos_importados.png)
  ##### Selecionei então minha tabela fato e ao clicar em Editar Dados pude adicionar para meu conjunto os outros dataframes que havia adicionado anteriormente, o processo era de somente arrastar para ligar as tabelas nas posições corretas e então uma ligação entre as tabelas foi exibida, após conferir que estava tudo correto o próximo passo foi de especificar qual seria o tipo correto de join a ser utilizado. Finalizado o processo de selecionar quais tabelas seriam ligadas, os campos que serviriam de chave primária e extrangeira e o tipo de join a ser utilizado o resultado obtido foi:
![Joins Realizados](../Evidencias/joins_dataframe.png)  
  ##### Quando encerrei todos os passos anteriores, na aba "Análises" um novo card foi exibido já com meus dados preparados para se iniciar a criação do Dashboard.
![Exibição de Análise Criada](../Evidencias/analise_criada.png)
### 3. Criação de Gráficos, Filtros e Ações
  ##### O primeiro passo para se iniciar a criação do Dashboard foi recapiular as perguntas feitas durante a Sprint 6 para garantir que todas seriam respondidas apropriadamente:
  ###### 1 - Análise de Sucesso de Filmes e Séries de Ação/Aventura com Foco nos Artistas Populares: Filmes e Séries com Artistas populares alcançam uma maior audiência e são melhor avaliados? Como a participação desses artistas afetam o desempenho do produto?
  ###### 2 - Filtrar por Ano e Análise de Tendências: Acompanhar a evolução de avaliações dos gêneros "Ação" e "Aventura" no decorrer dos anos. Houveram tempos em que um gênero foi mais popular que o outro? Isso se inverteu ou sempre caminharam juntos?
  ###### 3 - Análise de Preferência de Formato por Gênero: Algum desses dois gêneros tem um formato preferido? por exemplo, filme de "Ação" fazem mais sucesso que os de aventura? Isso se repete quando mudamos para o formato de séries ou o publico no geral tem um gosto diferente para cada formato de produção?
  ###### 4 - Conclusão sobre Preferências: Se compararmos tudo em um top 20 produções mais populares e de sucesso, filmes e séries dividem as colocações ou algum dos dois são favoritos em escolha do publico?
  ##### E então, o segundo Job
![Execução Segundo Job](../Evidencias/job2_exec.png)
### 4. Criação de Tabelas no Glue Catalog
  ##### Logo após a execução dos Jobs e a confirmação de seu sucesso no Bucket criei o Crawler que seria responsável pela correta criação das tabelas.
![Criação e Execução Crawler](../Evidencias/crawler_criado.png)
  ##### Após executado o Crawler vemos o resultado
![Resultado Tabelas Criadas](../Evidencias/tabelas_glue_catalog.png)
  ##### Rodei uma Query no AWS Athena para ter certeza da correta execução do Crawler, Criação das Tabelas e Padronização dos dados.
  ##### A Query foi
![Query Athena](../Evidencias/exemplo_query_athena.png)
  ##### E obtive o resultado:
![Resultado Athena](../Evidencias/athena_results.png)
### 5. Organização dos Buckets
  ##### Após a execução dos Jobs conferi em meu bucket os arquivos criados e como resultado tive outros como o seguinte exemplo
![Resultado Execução Jobs](../Evidencias/exemplo_execucao_sucesso.png)
  ##### Os dados foram organizados dentro do bucket para melhor visualização da seguinte forma:
![Organização Bucket](../Evidencias/estrutura_bucket.png)
  ##### E Por fim baixei um dos arquivos para ter certeza da estrutura também em outros ambientes além da AWS e executei uma query e a estruturação e consistência dos dados se mantiveram
![Exemplo Amostra Resultados](../Evidencias/exemplo_estruturacao_dados.png)

### 6. Links Úteis
  #### [Certificados](/Sprint_10/Certificados) 
  #### [Evidencias](/Sprint_10/Evidencias)
  #### [Exercícios](/Sprint_10/Exercicios)
