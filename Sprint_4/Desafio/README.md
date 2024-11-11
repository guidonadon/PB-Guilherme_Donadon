# Etapas
### 1. CSV Carguru
  ##### Primeiramente movi para a pasta do desafio o arquivo carguru.py que seria usado no mesmo, e então ao primeiro teste para observar quais seriam os resultados obtive:
![Teste Carguru](../Evidencias/Teste_carguru.py)
  ##### Após, comecei a importar o arquivo CSV que seria usado no desafio já se atentando ao tratamento de linhas duplicadas conforme imagem: 
![Remoção de linhas duplicadas](../Evidencias/remocao_duplicados.png) 

### 2. Importação de bibliotecas
  ##### Primeiramente importei as bibliotecas que usaria no desafio, inicialmente foram apenas pandas e matplotlib porém ao final acabei importando mais ficando da seguinte maneira. 
![Importação de biblioteca](../Evidencias/importe_bibliotecas.png)
  ##### Após, comecei a importar o arquivo CSV que seria usado no desafio já se atentando ao tratamento de linhas duplicadas conforme imagem: 
![Remoção de linhas duplicadas](../Evidencias/remocao_duplicados.png) 

### 3. Criação dos cálculos
  ##### O processo de criação se divergiu em alguns pontos a depender do que se era proposto em cada Etapa do desafio:
  ###### Etapa 4 - Ao desenvolver o cálculo que retornaria o app mais caro do DataSet primeiro fiz um tratamento para retirar caracteres monetários e espaços em branco logo converti para tipo float e então busquei na coluna o valor mais alto, tendo retornado o resultado: 
![App Mais Caro](../Evidencias/cod_app_mais_caro.png) 
  ###### Etapa 5 - O processo na etapa cinco foi mais simples que o anterior, ao criar uma variável "classificação_app" e filtrar aos que eram iguais ao termo "Mature 17+" o resultado retorno porém com valor acima do esperado, então fiz um filtro para remover entradas duplicadas mas dessa vez filtrando pela coluna "App" que erá onde se encontravam os nomes do app garantindo assim que o código retornaria exatamente uma entrada para cada aplicativo, mesmo que fossem de versões de updates diferentes. 
![App Mature 17+](../Evidencias/cod_app_mature.png) 
  ###### Etapa 6 - Durante o cálculo dos apps com mais Reviews foi necessário o uso da biblioteca Pandas, assim transformei tudo para valores númericos, fiz um leve tratamento de erros e retirei novamente os apps duplicados e defini como 10 o número de entradas a serem listadas.
![Apps com Mais Reviews](../Evidencias/cod_app_mais_reviews.png) 

### 7. Links Úteis
  #### [Certificados](/Sprint_3/Certificados) 
  #### [Evidencias](/Sprint_3/Evidencias)
  #### [Exercícios](/Sprint_3/Exercicios)
