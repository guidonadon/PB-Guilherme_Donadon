select tbvendedor.nmvdd as vendedor,
SUM(tbvendas.qtd * tbvendas.vrunt) as 'valor_total_vendas',
ROUND(((SUM(tbvendas.qtd * tbvendas.vrunt)) * (tbvendedor.perccomissao)) / 100,2) as comissao
from tbvendedor
LEFT JOIN tbvendas
on tbvendedor.cdvdd = tbvendas.cdvdd
where tbvendas.status = 'Concluído'
group by tbvendedor.nmvdd
order by comissao desc 
