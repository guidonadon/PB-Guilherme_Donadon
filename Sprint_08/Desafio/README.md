# Etapas
### 1. Configuração Inicial
  ##### As configurações iniciais foram definir a versão do Glue, as permissões do IAM, a linguagem a ser utilizada o Worker Type e o numero de Workers, além do tempo a ser reservado para a execução do job, como mostrado em alguns exemplos a seguir!
![Tempo do job](../Evidencias/tempo_glue.png)
![Permissões IAM](../Evidencias/rules_iam.png)
### 2. Criação dos scripts
  ##### Foram criados dois scripts diferentes, um para cada job, sendo o primeiro focado em trabalhar com os arquivos CSV. O script foi responsável por iniciar a sessão Park, localizar e ler os arquivos CSV mediante o caminho so s3 fornecido, definir o tipo de esquema e separador usado nos CSVs além de fazer um leve tratamento para valores nulos em ambos os arquivos. Após isso foram transformados em formato .parquet e salvos novamente no bucket porém dessa vez na camada Trusted.
![Script Job 1 - Parte 1](../Evidencias/script_job1_part1.png)
![Script Job 1 - Parte 1](../Evidencias/script_job1_part2.png)
  ##### O segundo script tratou os arquivos em formato .json, inicialmente se fez o processe de iniciar a sessão Spark e então a definição do esquema foi um pouco mais detalhada por conter dados de diferentes formatos dentro do mesmo arquivo Json, logo depois os jsons foram lidos no caminho informado e um tratamento para preencher colunas com valores nulos ou criar esses campos e preenche-los com o tratamento correto também foi realizado, assim como anteriormente nos arquivos CSVs o arquivo foi convertido para formato .parquet e então salvo também no bucket s3 na camada Trusted
![Script Job 2 - Parte 1](../Evidencias/script_job2_part1.png)
![Script Job 2 - Parte 2](../Evidencias/script_job2_part2.png)
![Script Job 2 - Parte 3](../Evidencias/script_job2_part3.png)
![Script Job 2 - Parte 4](../Evidencias/script_job2_part4.png)
### 3. Resultados dos Buckets
  ##### Como resultado da execução dos scripts acima a camada Trusted foi criada conforme imagem a seguir
![Criação Camada Trusted](../Evidencias/trusted_folder.png)
  ##### Após a criação da camada Trusted os arquivos foram organizados da maneira que se segue:
![Organização Arquivos](../Evidencias/results_jobs.png)
### 4. Resultados do Job 1
  ##### O job foi executado e foi exibida a notificação do sucesso da execução
![Resultado Job 1 Part 1](../Evidencias/exec_job1.png)
  ##### Foi observado a criação correta dos arquivos no bucket s3 para os arquivos do CSV chamado Movies.
![Resultado Job 1 Part 2](../Evidencias/results_job1_part1.png)
  ##### O mesmo se repetiu para Series
![Resultado Job 1 Part 3](../Evidencias/results_job1_part2.png)
### 5. Resultados do Job 2
  ##### Assim como no Job 1, no Job 2 a flag de sucesso foi exibida.
![Resultado Job 2 Part 1](../Evidencias/exec_job2.png)
  ##### Nos Jsons referentes aos filmes também foram realizadas as gravações de arquivos.
![Resultado Job 2 Part 2](../Evidencias/results_job2_part1.png)
  ##### E em Series também
![Resultado Job 2 Part 3](../Evidencias/results_job2_part2.png)

### 6. Links Úteis
  #### [Certificados](/Sprint_08/Certificados) 
  #### [Evidencias](/Sprint_08/Evidencias)
  #### [Exercícios](/Sprint_08/Exercicios)
