CREATE DATABASE IF NOT EXISTS global_solution_db;

USE global_solution_db;

CREATE TABLE IF NOT EXISTS pontos_abastecimento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    rua VARCHAR(255) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    estado VARCHAR(100) NOT NULL,
    tipo_carregador VARCHAR(50) NOT NULL,
    capacidade INT NOT NULL
);

-- Insere alguns registros iniciais para teste
INSERT INTO pontos_abastecimento (nome, rua, cidade, estado, tipo_carregador, capacidade) VALUES
('Ponto 1', 'Rua A', 'São Paulo', 'SP', 'Carregador Rápido', 50),
('Ponto 2', 'Rua B', 'Rio de Janeiro', 'RJ', 'Carregador Normal', 22),
('Ponto 3', 'Avenida C', 'Curitiba', 'PR', 'Carregador Ultra-rápido', 150);
