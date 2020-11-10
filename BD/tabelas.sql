mysql -u root -p
use ludo
create table jogador(
    nome varchar(30),
    pontuacao int,
    pinos_base int,
    cor varchar(30),
    primary key(cor)
);

create table pino(
    casas_restantes int,
    cor varchar(30),
    foreign key(cor)
);

create table jogo(
    cor varchar(30),
    foreign key(cor)
);

create table dado(
    numero int,
    primary key(numero)
);

create table casa(
    segura varchar(30) not null,
    primary key(segura)
);
