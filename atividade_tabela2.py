#2. Crie um programa em Python que gere tabelas para uma aplicação de eventos. Elas devem compreender as seguintes funcionalidades:
#a. Eventos devem ter título, data e local, além da referência ao organizador;
#b. O organizador deve ter nome, email e cpf;
#c. As restrições/relacionamentos devem fazer sentido.

import sqlite3
conexao = sqlite3.connect('tabela_exercicios2')

cursor = conexao.cursor()
#cursor.execute ('DROP TABLE eventos')
#cursor.execute('CREATE TABLE organizador(id_organizador INT NOT NULL, nome VARCHAR(100), email VARCHAR(100), cpf VARCHAR(100), PRIMARY KEY (id_organizador));')
cursor.execute('CREATE TABLE eventos(id_eventos INT NOT NULL, titulo VARCHAR(100), data VARCHAR(20), local VARCHAR(50), id_organizador INT NOT NULL, PRIMARY KEY (id_organizador), FOREIGN KEY (id_eventos) REFERENCES organizador (id_organizador));')

conexao.commit()
conexao.close