SELECT DISTINCT autor.nome
from livro
LEFT JOIN autor
on livro.autor = autor.codautor
LEFT JOIN editora
on livro.editora = editora.codeditora
LEFT JOIN endereco
on editora.endereco = endereco.codendereco
where LOWER (endereco.estado) not like '%RIO GRANDE DO SUL %' and lower(endereco.estado) not like '%PARANÁ%'
ORDER by autor.nome
