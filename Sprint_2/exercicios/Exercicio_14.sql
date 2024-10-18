select tbvendas.estado,
ROUND(ROUND(SUM(tbvendas.vrunt * tbvendas.qtd) ,2) / COUNT(tbvendas.qtd) ,2) as gastomedio
from tbvendas
where tbvendas.status = 'Concluído'
group BY tbvendas.estado
ORDER BY gastomedio desc 
