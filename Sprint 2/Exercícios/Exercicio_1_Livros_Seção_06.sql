SELECT 
    livro.cod as CodLivro, 
    livro.titulo as Titulo, 
    autor.codautor as CodAutor, 
    autor.nome AS NomeAutor, 
    livro.valor as Valor, 
    editora.codeditora AS CodeEditora, 
    editora.nome AS NomeEditora
FROM 
    livro
INNER JOIN 
    autor ON autor.codautor = livro.autor -- unindo pela chave estrangeira de autor
LEFT JOIN 
    editora ON editora.codeditora = livro.editora -- unindo pela chave estrangeira de editora
ORDER BY 
    livro.valor DESC
LIMIT 10;
