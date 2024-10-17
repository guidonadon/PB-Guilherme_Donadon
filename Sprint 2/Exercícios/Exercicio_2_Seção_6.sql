SELECT 
    editora.codeditora,
    editora.nome, 
    COUNT(livro.titulo) AS quantidade
FROM 
    livro
LEFT JOIN 
    editora ON livro.editora = editora.codeditora
LEFT JOIN 
    endereco ON editora.endereco = endereco.codendereco
GROUP BY 
    editora.codeditora, editora.nome
order by quantidade desc
LIMIT 5;
