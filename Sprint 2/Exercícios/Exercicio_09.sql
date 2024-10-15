SELECT tabvendas.cdpro,
tabvendas.nmpro
from tbvendas as tabvendas
where tabvendas.dtven BETWEEN '2014-02-03' AND '2018-02-02'
and tabvendas.status = 'Concluído'
group by tabvendas.cdpro, tabvendas.nmpro
order by SUM(tabvendas.qtd) DESC
limit 1
