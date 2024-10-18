SELECT DISTINCT autor.codautor, autor.nome, COUNT(livro.cod) as quantidade_publicacoes
from livro
LEFT JOIN autor
on livro.autor = autor.codautor
group by autor.codautor, autor.nome
ORDER by quantidade_publicacoes DESC
limit 1
