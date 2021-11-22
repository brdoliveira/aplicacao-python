create database banco_filmes;
use banco_filmes;

create table dados(
	idFilme int primary key auto_increment,
    titulo varchar(50),
    lancamento varchar(50),
    duracao varchar(50),
    genero varchar(50),
    diretor varchar(50),
    linguagem varchar(50)
);

select * from dados;

-- drop database banco_filmes;
