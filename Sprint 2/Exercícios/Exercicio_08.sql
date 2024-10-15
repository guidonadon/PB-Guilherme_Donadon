SELECT cdvdd,nmvdd
from tbvendedor
where cdvdd = (select cdvdd
               from tbvendas
               WHERE status = 'Concluído'
               group by cdvdd
               order by count (cdvdd) DESC
               limit 1)
