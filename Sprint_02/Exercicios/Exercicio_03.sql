SELECT 
count(livro.titulo) quantidade, 
editora.nome, 
endereco.estado, 
endereco.cidade
from livro
left join editora
on livro.editora = editora.codeditora
LEFT JOIN endereco
on editora.endereco = endereco.codendereco
group by editora.nome
limit 5
