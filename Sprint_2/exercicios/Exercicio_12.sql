select tbdependente.cddep,
tbdependente.nmdep,
tbdependente.dtnasc,
SUM(tbvendas.qtd * tbvendas.vrunt) as valor_total_vendas
from tbdependente
LEFT JOIN tbvendedor
on tbdependente.cdvdd = tbvendedor.cdvdd
LEFT JOIN tbvendas
on tbvendedor.cdvdd = tbvendas.cdvdd
WHERE tbvendas.status = 'Concluído'
GROUP BY tbdependente.cddep, tbdependente.nmdep, tbdependente.dtnasc
having SUM(tbvendas.qtd * tbvendas.vrunt) > 0
ORDER BY SUM(tbvendas.qtd * tbvendas.vrunt)
limit 1
