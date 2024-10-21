-- Tabela Clientes
CREATE TABLE IF NOT EXISTS Clientes (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(40),
    estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40)
);

-- Tabela Combustivel
CREATE TABLE IF NOT EXISTS Combustivel (
    idcombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(20)
);

-- Tabela Carro
CREATE TABLE IF NOT EXISTS Carro (
    idCarro INT PRIMARY KEY,
    kmCarro INT,
    classiCarro VARCHAR(50),
    marcaCarro VARCHAR(80),
    modeloCarro VARCHAR(80),
    anoCarro INT,
    idcombustivel INT,
    FOREIGN KEY (idcombustivel) REFERENCES Combustivel(idcombustivel)
);

-- Tabela Vendedor
CREATE TABLE IF NOT EXISTS Vendedor (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(15),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(40)
);

-- Tabela Fato Locacao
CREATE TABLE IF NOT EXISTS Locacao (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    idVendedor INT,
    dataLocacao DATETIME,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL(18,2),
    dataEntrega DATE,
    horaEntrega TIME,
    idCombustivel INT,
    FOREIGN KEY (idCliente) REFERENCES Clientes(idCliente),
    FOREIGN KEY (idCarro) REFERENCES Carro(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor)
);

-- Inserção de Dados Tabela Clientes
INSERT INTO Clientes (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao;

-- Inserção de Dados Tabela Combustivel
INSERT INTO Combustivel (idcombustivel, tipoCombustivel)
SELECT DISTINCT idcombustivel, tipoCombustivel
FROM tb_locacao;

-- Inserção de Dados Tabela Carro
INSERT INTO Carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel)
SELECT idCarro, MAX(kmCarro), classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel
FROM tb_locacao
GROUP BY idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel;

-- Inserção de Dados Tabela Vendedor
INSERT INTO Vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;

-- Inserção de Dados Tabela Vendedor
INSERT INTO Locacao (idLocacao, idCliente, idCarro, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega)
SELECT idLocacao, idCliente, idCarro, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega
FROM tb_locacao;

-- Adição Dados Coluna Combustivel na Tabela Locação
UPDATE Locacao 
SET idCombustivel = (
	SELECT Carro.idcombustivel
	FROM Carro
	WHERE Carro.idCarro = Locacao.idCarro
	);

-- Ajuste de Datas
UPDATE Locacao
SET dataLocacao= CONCAT(
  SUBSTRING(dataLocacao. 1, 4),
  SUBSTRING(dataLocacao. 5, 2),
  SUBSTRING(dataLocacao. 7, 2)
);

UPDATE Locacao
SET dataEntrega= CONCAT(
  SUBSTRING(dataEntrega. 1, 4),
  SUBSTRING(dataEntrega. 5, 2),
  SUBSTRING(dataEntrega. 7, 2)
);

-- Para a Criação das tabelas do modelo Dimensional e Relacional foram seguidos os mesmos passos
