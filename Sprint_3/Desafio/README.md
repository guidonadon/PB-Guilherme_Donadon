# Etapas
### 1. Organização das Tasks
  ##### Após baixar o banco de dados, e fazer a ligação com meu intepretador, comecei a estruturar como eu resolveria o desafio.
  ##### Os arquivos de entrega do desafio foram alocados na pasta de mesmo nome conforme instruções.

### 2. Importação de bibliotecas
  ##### Primeiramente importei as bibliotecas que usaria no desafio, inicialmente foram apenas pandas e matplotlib porém ao final acabei importando mais ficando da seguinte maneira. 
![Importação de biblioteca](/Sprint_3/Evidencias/importe_bibliotecas.png)
  ##### Após, comecei a importar o arquivo CSV que seria usado no desafio já se atentando ao tratamento de linhas duplicadas conforme imagem: 
![Remoção de linhas duplicadas](/Sprint_3/Evidencias/remocao_duplicados.png) 
  ##### Por fim, para finalizar o processo da criação das tabelas criei a tabela "locacao" e referenciei todas as chaves estrangeiras das tabelas que seriam ligadas a ela posteriormente. Na tabela "Carros" uma chave estrangeira para a tabela "Combustivel" também foi criada.

### 3. Inserção de Dados
  ##### Após criadas as tabelas houve o início da alocação dos dados da tabela "tb_locacao" para suas novas respectivas tabelas. No geral o processo se deu pelos comandos *INSERT INTO* juntamente com o nome da tabela e as colunas a serem inseridos os dados e *SELECT DISTINCT* para copiar os dados evitando disparidades de dados duplicados.
  ##### Para as tabelas "Carro" e "Locacao" o processo foi levemente diferente
   ###### a) Tabela Carro: Ao buscar os dados a serem inseridos se apresentou a necessiadade de adicionar os carro de mesmo ID com os dados de Kilometragem mais atualizados para maior relevância, para esta situação o comando "SELECT" foi utilizado e na coluna "kmCarro" o modificador *"MAX"* tendo o resultado "MAX(kmCarro)".
   ###### b) Tabela Locacao: Como essa tabela seria preenchida apenas com as chaves primárias de outras tabelas que aqui se transformaram em chaves estrangeiras, nenhuma se repetiria por conta dos comandos utilizados anteriormente, sendo assim, apenas um comando *"SELECT"* se fez necessário.

### 4. Correção idCombustivel
  ##### As informações contidas na coluna "idCombustivel" da tabela "Combustivel" eram necessárias na tabela locacao, mas ao fazer a ligação diretamente pela chave primária para uma outra tabela, essa chave já estava ligada à tabela "Carros", poderia acarretar problemas de rudundância de informações, fazendo a ligação indireta é uma forma mais segura. 
  ##### Para a ligação, após todas criações já terem sido feitas, inclusive a coluna "idCombustivel" na tabela "locacao", porém sem definição e referenciamento de chaves estrangeiras como foi feito nos outros casos, utilizei o comando *UPDATE* na tabela "locacao", e então SET na coluna "idCombustivel" selecionei de onde viria as informações com os comandos *SELECT, FROM e WHERE* e então os dados foram adicionados.

### 5. Ajuste de Datas
  ##### Ao finalizar a estruturação das tabelas que no caso foram arranjadas em modelo "SnowFlake Schema" foi verificados que as datas foram exibidas no aplicativo "DBeaver" em formato diferente ao que deveria ser exibidas as datas, um exemplo disso era a primeira data da View em questão que exibia para a data "2015/01/10" os valores "20.150.110".
  ##### A formatação dessas informações foi feita através do uso do comando *UPDATE* juntamente com *SET* e *SUBSTRING* assim como exibido na área de evidências.

### 6. Views
  ##### Após todos os processos citados acima uma View contendo alguns registros de locação dos veículos foi criada e adicionada às evidências.

