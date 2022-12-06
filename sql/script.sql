    create database projeto;

    use projeto;
    create table usuarios (
        id int primary key auto_increment,
        nome varchar(255),
        email varchar(255),
        senha varchar(255),
        tipo char
    );

    use projeto;
    create table prestadoresDeServico(
        id int primary key auto_increment,
        titulo varchar(255),
        numero varchar(255),
        email varchar(255),
        descricao varchar(255)
    );

    use projeto;
    create table ferramentas(
        id int primary key auto_increment,
        titulo varchar(255),
        descricao text(255),
        link varchar(255),
        empresa varchar(255)
    );

    use projeto;
    create table empresa(
        id int primary key auto_increment,
        titulo varchar(255),
        descricao text(255),
        cnpj varchar(255),
        endereco varchar(255)
    );