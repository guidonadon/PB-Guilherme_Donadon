select autor.codautor, autor.nome, autor.nascimento, COUNT(livro.cod) as quantidade
from autor
left join livro
on autor.codautor = livro.autor
group by autor.nome
order by autor.nome
