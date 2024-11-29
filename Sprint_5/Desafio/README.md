# Etapas
### 1. CSV Carguru
  ##### Primeiramente movi para a pasta do desafio o arquivo carguru.py que seria usado no mesmo, e então ao primeiro teste para observar quais seriam os resultados obtive:
![Teste Carguru](../Evidencias/Teste_carguru.png)
  ##### Após constatar os resultados trabalhei em meu arquivo Dockerfile determinando que seriam executados python e o arquivo carguru.py: 
![Dockerfile Etapa 1](../Evidencias/etapa1_dockerfile.png) 
  ##### Todas as execuções tais como, criação do container e leitura e execução do código foram feitos e foi retornado os resultados a seguir, constando também as informações do container: 
![Dockerfile Etapa 1](../Evidencias/criacao_container_carguru.png) 

### 2. É possível reutilizar um container?
  ##### Sim! Para responder a essa pergunta o comando `Docker start -i {nome do container}` foi utilizado tal como demonstrado na imagem:
![Reativação de Container](../Evidencias/reativacao_container.png)

### 3. Criação do container com Hash
  ##### O primeiro passo foi a criação do código python que utilizaria a biblioteca Hashlib para com um input, neste caso optei por nomes, gerar um output com o código hash da informação inserida:
![Código Python](../Evidencias/hash_py.png) 
  ##### Assim como anteriormente um arquivo dockerfile foi criado e as configurações foram quase as mesmas da etapa 1 exceto pela mudança do nome do arquivo .py a ser executado: 
![Arquivo Dockerfile](../Evidencias/etapa3_dockerfile.png) 
  ##### O container foi criado utilizando o argumento *-t* para renomear o container e durante a execução o argumento *-it* foi usado para que o container fosse executado em modo interativo com um terminal para que comandos possam ser executados em tempo real.
![Container Hash](../Evidencias/criacao_container_img_hash.png) 
  ##### Após a correta execução dos comandos e script .py observei o resultado:
![Resultado nomes com hash](../Evidencias/resultado_hash.png) 

### 7. Links Úteis
  #### [Certificados](/Sprint_5/Certificados) 
  #### [Evidencias](/Sprint_5/Evidencias)
  #### [Exercícios](/Sprint_5/Exercicios)
