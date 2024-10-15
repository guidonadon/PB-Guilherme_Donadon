select 
tbvendas.cdcli,
tbvendas.nmcli,
sum(tbvendas.qtd * tbvendas.vrunt) as gasto 
from tbvendas 
where tbvendas.status = 'Concluído'
group by tbvendas.cdcli 
order by gasto desc 
limit 1 
