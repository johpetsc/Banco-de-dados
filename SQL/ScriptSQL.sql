DROP TABLE IF EXISTS MEIO_COMUNICACAO;
DROP TABLE IF EXISTS MIDIA;
DROP TABLE IF EXISTS NOTICIAS_PARTIDOS;
DROP TABLE IF EXISTS NOTICIAS_CANDIDATOS;
DROP TABLE IF EXISTS NOTICIAS_AVALIADAS;
DROP TABLE IF EXISTS AVALIADOR;
DROP TABLE IF EXISTS NOTICIA;
DROP TABLE IF EXISTS CANDIDATO;
DROP TABLE IF EXISTS PARTIDO;
DROP TABLE IF EXISTS CARGO_POLITICO;
DROP TABLE IF EXISTS ELEITOR;
DROP TABLE IF EXISTS REGIAO;
DROP TABLE IF EXISTS PESSOA;



CREATE TABLE PESSOA(
  id_pessoa INTEGER PRIMARY KEY AUTO_INCREMENT,
  cpf VARCHAR(20) NOT NULL,
  p_nome VARCHAR(15) NOT NULL,
  u_nome VARCHAR(15) NOT NULL,
  data_nascimento DATE NOT NULL,
  endereco VARCHAR(120) NOT NULL
);

CREATE TABLE REGIAO(
  id_regiao INTEGER PRIMARY KEY AUTO_INCREMENT,
  nome_regiao VARCHAR(20) NOT NULL,
  num_eleitores INTEGER,
  num_candidatos INTEGER
);

CREATE TABLE ELEITOR(
  id_eleitor INTEGER PRIMARY KEY AUTO_INCREMENT,
  id_pessoa INTEGER NOT NULL,
  id_regiao INTEGER NOT NULL,
  zona VARCHAR(50) NOT NULL,
  secao INTEGER NOT NULL,
  FOREIGN KEY(id_pessoa) REFERENCES PESSOA(id_pessoa),
  FOREIGN KEY(id_regiao) REFERENCES REGIAO(id_regiao)
);

CREATE TABLE CARGO_POLITICO (
  id_cargo INTEGER PRIMARY KEY AUTO_INCREMENT,
  num_id INTEGER NOT NULL,
  nome_cargo VARCHAR(50) NOT NULL
);

CREATE TABLE PARTIDO (
  id_partido INTEGER PRIMARY KEY AUTO_INCREMENT,
  id_regiao INTEGER NOT NULL,
  nome_partido VARCHAR(30) NOT NULL,
  sigla VARCHAR(10) NOT NULL,
  data_fundacao DATE,
  FOREIGN KEY(id_regiao) REFERENCES REGIAO(id_regiao)
);

CREATE TABLE CANDIDATO (
  num_id INTEGER PRIMARY KEY AUTO_INCREMENT,
  id_pessoa INTEGER NOT NULL,
  id_partido INTEGER NOT NULL,
  id_regiao INTEGER NOT NULL,
  id_cargo INTEGER NOT NULL,
  FOREIGN KEY(id_pessoa) REFERENCES PESSOA(id_pessoa),
  FOREIGN KEY(id_partido) REFERENCES PARTIDO(id_partido),
  FOREIGN KEY(id_regiao) REFERENCES REGIAO(id_regiao),
  FOREIGN KEY(id_cargo) REFERENCES CARGO_POLITICO(id_cargo)
);


CREATE TABLE NOTICIA (
  noticia_id INTEGER PRIMARY KEY AUTO_INCREMENT,
  data_publicacao DATE,
  titulo_noticia VARCHAR(200) NOT NULL,
  texto VARCHAR(1000) NOT NULL
);

CREATE TABLE AVALIADOR (
  id_avaliador INTEGER PRIMARY KEY AUTO_INCREMENT,
  nome_avaliador VARCHAR(50) NOT NULL
);

CREATE TABLE NOTICIAS_AVALIADAS (
  noticia_id INTEGER NOT NULL,
  id_avaliador INTEGER NOT NULL,
  avaliacao VARCHAR(15) NOT NULL,
  PRIMARY KEY(noticia_id, id_avaliador),
  FOREIGN KEY(noticia_id) REFERENCES NOTICIA(noticia_id),
  FOREIGN KEY(id_avaliador) REFERENCES AVALIADOR(id_avaliador)
);

CREATE TABLE NOTICIAS_CANDIDATOS(
  noticia_id INTEGER NOT NULL,
  num_id INTEGER NOT NULL,
  PRIMARY KEY(noticia_id, num_id),
  FOREIGN KEY(noticia_id) REFERENCES NOTICIA(noticia_id),
  FOREIGN KEY(num_id) REFERENCES CANDIDATO(num_id)
);

CREATE TABLE NOTICIAS_PARTIDOS(
  noticia_id INTEGER NOT NULL,
  id_partido INTEGER NOT NULL,
  PRIMARY KEY(noticia_id, id_partido),
  FOREIGN KEY(noticia_id) REFERENCES NOTICIA(noticia_id),
  FOREIGN KEY(id_partido) REFERENCES PARTIDO(id_partido)
);

CREATE TABLE MIDIA (
  id_midia INTEGER PRIMARY KEY AUTO_INCREMENT,
  noticia_id INTEGER NOT NULL,
  tipo_midia VARCHAR(20) NOT NULL,
  nome_arq VARCHAR(30) NOT NULL,
  tamanho_arq INTEGER NOT NULL,
  formato_arq VARCHAR(5) NOT NULL,
  FOREIGN KEY(noticia_id) REFERENCES NOTICIA(noticia_id)
);


CREATE TABLE MEIO_COMUNICACAO(
  comunicacao_id INTEGER PRIMARY KEY AUTO_INCREMENT,
  noticia_id INTEGER NOT NULL,
  tipo_meiocom VARCHAR(20) NOT NULL,
  data_postagem DATE,
  FOREIGN KEY(noticia_id) REFERENCES NOTICIA(noticia_id)
);

INSERT INTO PESSOA(id_pessoa, cpf, p_nome, u_nome, data_nascimento, endereco)
values (1, 13371337, 'Bruce', 'Wayne', '1971-2-14', 'Wayne Mansion, 010 Gotham Federal'),
       (2, 10011001, 'Thor', 'Thundergod', '516-07-04', 'City Hall, 17, Asgard de Janeiro'),
       (3, 12345678, 'Bruce', 'Banner', '1962-05-11', 'River Street, 30, Dayton, Atlantis do Norte'),
       (4, 89453845, 'Sheriff', 'Woody', '1995-12-22', 'Bed, Andy´s Bedroom, Ohio Grosso'),
       (5, 99999999, 'Faisca', 'McQueen', '2006-06-30', 'Radiator Springs, 120, California do Sul'),
       (6, 10000001, 'Aqua', 'Man', '1941-11-02', 'Aurania, 10, Atlantis do Norte'),
       (7, 19984471, 'Ron', 'Wesley', '1999-05-13', 'Downhill Abbey, 133, Asgard de Janeiro'),
       (8, 14625879, 'Albus', 'Dumbledore', '1881-04-15', 'Hogwarts School of Wizardry, Ohio Grosso'),
       (9, 66587831, 'Tony', 'Stark', '1963-01-17', 'Stark Building, 91, Atlantis do Norte'),
       (10, 14725836, 'Capitao', 'America', '1941-03-15', 'Venture Park, 32, California do Sul'),
       (11, 15947538, 'Eobard', 'Thawne', '1963-09-22', 'S.T.A.R. Labs, 154, Gotham Federal'),
       (12, 14563289, 'Diana', 'Prince', '1941-10-05', 'Central Park, 11, Ohio Grosso'),
       (13, 86248426, 'Pinguim', 'Surfista', '2007-10-26', 'Praia das Rochas, 1337, California do Sul');
	   
INSERT INTO REGIAO(id_regiao, nome_regiao, num_eleitores, num_candidatos)
values (1, 'Gotham Federal', 2, 1),
       (2, 'California do Sul', 3, 1),
       (3, 'Atlantis do Norte', 3, 1),
       (4, 'Ohio Grosso', 3, 2),
       (5, 'Asgard de Janeiro', 2, 2);
	   
INSERT INTO ELEITOR(id_eleitor, id_pessoa, id_regiao, zona, secao)
values (1, 3, 3, 'Atlantis High School', 011),
       (2, 4, 4, 'Ohio´s Law School', 120),
       (3, 5, 2, 'California Kindergarten', 084),
       (4, 9, 3, 'Atlantis High School', 009),
       (5, 10, 2, 'California Kindergarten', 051),
       (6, 11, 1, 'Gotham´s Library', 003),
       (7, 2, 5, 'Asgardian Community College', 010),
       (8, 6, 3, 'Atlantis High School', 005),
       (9, 7, 5, 'Asgardian Community College', 015),
       (10, 8, 4, 'Ohio´s Law School', 122),
       (11, 12, 4, 'Ohio´s Kids School', 012),
       (12, 13, 2, 'Californa Kindergarten', 080);

INSERT INTO CARGO_POLITICO(id_cargo, num_id, nome_cargo)
values (1, 1, 'Presidente'),
       (2, 5, 'Governador'),
       (3, 2, 'Prefeito'),
       (4, 6, 'Vereador'),
       (5, 4, 'Deputado Estadual'),
       (6, 7, 'Deputado Estadual'),
       (7, 3, 'Deputada Federal'); 

INSERT INTO PARTIDO(id_partido, id_regiao, nome_partido, sigla, data_fundacao)
values (1, 3, 'Partido da Marvel', 'PdM', '1947-06-11'),
       (2, 1, 'Partido da DC', 'PDC', '1934-08-17'),
       (3, 1, 'Partido Pixar', 'PP', '1986-02-03'),
       (4, 2, 'Partido Harry Potter', 'PHP', '2002-05-11');

INSERT INTO CANDIDATO(num_id, id_partido, id_pessoa, id_regiao, id_cargo)
values (1, 1, 1, 1, 1),
       (2, 4, 7, 5, 2),
       (3, 4, 12, 4, 3),
       (4, 1, 6, 3, 4),   
       (5, 2, 2, 5, 5),
       (6, 2, 8, 4, 6),
       (7, 3, 13, 2, 7);

INSERT INTO NOTICIA(noticia_id, data_publicacao, titulo_noticia, texto)
values (1, '2018-05-12', 'Presidente Batman promete aumento de 200 reais nos salarios', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.'),
       (2, '2018-09-28', 'Partido da DC desviou 200 milhoes em 2017', 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
       (3, '2018-10-02', 'PHP e PP formam alianca', 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.'),
       (4, '2018-11-14', 'Candidata Diana lidera a corrida por 12 milhoes de votos', 'Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?'),
       (5, '2018-05-22', 'Vereador Aquaman preso por lavagem de dinheiro', 'Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.');

INSERT INTO AVALIADOR(id_avaliador, nome_avaliador)
values (1, 'Norman Osborn'),
       (2, 'Otto Octavius');

INSERT INTO NOTICIAS_AVALIADAS(noticia_id, id_avaliador, avaliacao)
values (1, 1, 'Fake'),
       (2, 1, 'Nao Fake'),
       (3, 1, 'Nao Fake'),
       (4, 1, 'Fake'),
       (5, 1, 'Nao Fake'),
       (1, 2, 'Fake'),
       (2, 2, 'Nao Fake'),
       (3, 2, 'Nao Fake'),
       (4, 2, 'Nao Fake'),
       (5, 2, 'Fake');

INSERT INTO MIDIA(id_midia, noticia_id, tipo_midia, nome_arq, tamanho_arq, formato_arq)
values (1, 1, 'Imagem', 'batman_2017', 109, 'jpg'),
       (2, 4, 'Imagem', 'grafico_votos', 201, 'png'),
       (3, 5, 'Audio', 'aquaman_interrogatorio', 2110, 'mp3'),
       (4, 4, 'Video', 'diana_em_cs', 13490, 'avi'),
       (5, 2, 'Audio', 'prova_desvio_dc', 1600, 'mp3'),
       (6, 3, 'Imagem', 'pp_alia_php', 170, 'jpg'),
       (7, 5, 'Imagem', 'aquaman_2018', 111, 'jpg'),
       (8, 3, 'Video', 'php_pp_juntos', 9550, 'mp4');

INSERT INTO MEIO_COMUNICACAO(comunicacao_id, noticia_id, tipo_meiocom, data_postagem)
values (1, 4, 'Jornal TV', '2018-11-15'),
       (2, 1, 'Jornal Internet', '2018-05-13'),
       (3, 1, 'Jornal TV', '2018-05-13'),
       (4, 2, 'Redes Sociais', '2018-08-28'),
       (5, 3, 'Jornal Internet', '2018-10-02'),
       (6, 5, 'Jornal TV', '2018-05-22'),
       (7, 4, 'Jornal Internet', '2018-11-14');
       
/* 
	VIEW PARA SELECIONAR O ID E NOME COMPLETO
   	DE TODAS AS PESSOAS DA TABELA
*/
DROP VIEW IF EXISTS id_nomes;
CREATE VIEW id_nomes AS
SELECT id_pessoa AS ID, 
       concat(p_nome, ' ', u_nome) AS Nome_Completo
FROM PESSOA;

SELECT * FROM id_nomes;

/*
	VIEW PARA SELECIONAR ID, NOME COMPLETO,
    	CARGO E REGIAO DE CADA CANDIDATO
*/
DROP VIEW IF EXISTS cand;
CREATE VIEW cand AS
SELECT pessoa.id_pessoa AS ID,
       concat(p_nome, ' ', u_nome) AS Nome,
       nome_cargo AS Cargo,
       nome_regiao AS Regiao
FROM candidato, pessoa, regiao, cargo_politico
WHERE pessoa.id_pessoa = candidato.id_pessoa AND candidato.id_regiao = regiao.id_regiao AND candidato.id_cargo = cargo_politico.id_cargo
ORDER BY pessoa.id_pessoa ASC;

SELECT * FROM cand;

DELIMITER $$
CREATE PROCEDURE selecionar_pessoas (OUT quantidade INT)
BEGIN
    SELECT COUNT(*) INTO quantidade FROM pessoa;
END $$
DELIMITER ;

CALL selecionar_pessoas(@total);
SELECT @total;

