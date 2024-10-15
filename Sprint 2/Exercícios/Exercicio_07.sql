SELECT nome
from autor
where autor.codautor not in (select autor from livro)
order by nome
