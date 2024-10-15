select tbvendas.cdpro,
tbvendas.nmcanalvendas,
tbvendas.nmpro,
SUM(qtd) as quantidade_vendas
from tbvendas
where (tbvendas.nmcanalvendas = 'Ecommerce' or tbvendas.nmcanalvendas = 'Matriz')
and tbvendas.status = 'Concluído'
group by tbvendas.cdpro, tbvendas.nmcanalvendas, tbvendas.nmpro
order by quantidade_vendas
LIMIT 10
