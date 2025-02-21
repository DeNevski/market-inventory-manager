CREATE DATABASE IF NOT EXISTS estoque;

USE estoque;

CREATE TABLE IF NOT EXISTS produtos (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    quantidade DECIMAL(6,1) NOT NULL,
    medida ENUM('Mililitro', 'Litro', 'Grama', 'Quilograma', 'Unidade') NOT NULL,
    estocado INT NOT NULL,
    unidade ENUM('Unidade', 'Par', 'Pacote', 'Caixa', 'Fardo', 'Pallet') NOT NULL,
    valor_unitario DECIMAL(6,2) NOT NULL,
    PRIMARY KEY(id)
);
