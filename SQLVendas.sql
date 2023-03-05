#Banco de Dados desenvolvido por: @programmerantunes
#LinkedIn: www.linkedin.com/in/matheus-barboza-798b901b3/
#GitHub: www.github.com/Matheus-A-Barboza
#Feedback's através das redes sociais

create database sistemavendas;

use sistemavendas;

create table alimentos(
id_alimentos int primary key not null auto_increment,
nome_alimento varchar(20) not null,
tipo_produto varchar(9) not null,
qnt_alimento varchar(20) not null
);

create table limpeza(
id_limpeza int primary key not null auto_increment,
nome_produto varchar(40) not null,
tipo_produto varchar(7) not null,
qnt_produto varchar(20) not null
);

create table higiene(
id_alimento int primary key not null auto_increment,
nome_alimento varchar(30) not null,
tipo_produto varchar(7) not null,
qnt_alimento varchar(20) not null
);

create table cadastrarprodutos(
id_produto int primary key not null auto_increment,
nome_produto varchar(40) not null,
tipo_produto varchar(9) not null,
qnt_produto varchar(20) not null
);

create table consultaprodutos(
id_produto int primary key not null auto_increment,
nome_produto varchar(40) not null,
qnt_produto varchar(20) not null
);

create table deposito(
id_deposito int primary key not null auto_increment,
nome_produto varchar(40) not null,
tipo_produto varchar(9) not null,
qnt_produto varchar(20) not null
);

#Obrigado por utilizar meu Sistema!
