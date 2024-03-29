INSERT INTO RNR_CLIENTES VALUES (1,'Levi Pietro Paulo Silva','710.355.598-20','(11) 98117-3557','09041-070',
'Travessa Jo�o Rodrigues','975','Santo Andr�','SP');

INSERT INTO RNR_CLIENTES VALUES (2,'Bento Leandro Anthony da Cunha','751.738.628-07','(11) 98703-3817','09160-420',
'Rua Astorga','572','Santo Andr�','SP');

INSERT INTO RNR_CLIENTES VALUES (3,'Kau� Rodrigo Vinicius Vieira','105.274.858-96','(11) 99864-3475','09162-400',
'Rua S�o Diogo','492','Santo Andr�','SP');

INSERT INTO RNR_CLIENTES VALUES (4,'S�rgio Felipe Moura','111.002.548-38','(11) 98297-8609','09250-540',
'Rua Medina','438','Santo Andr�','SP');

INSERT INTO RNR_ENTREGA VALUES ('9D332',1,12,135,'23/01/2023');
INSERT INTO RNR_ENTREGA VALUES ('O4VNK',2,13,136,'28/01/2023');
INSERT INTO RNR_ENTREGA VALUES ('A0TG7',3,14,137,'30/01/2023');
INSERT INTO RNR_ENTREGA VALUES ('WBI74',4,15,138,'27/12/2022');

INSERT INTO RNR_PRODUTOS VALUES (12,'CAMISETA','OAKLEY ANIVERS�RIO','PRETO');
INSERT INTO RNR_PRODUTOS VALUES (13,'CAL�A','ZARA JEANS','BRANCO');
INSERT INTO RNR_PRODUTOS VALUES (14,'TENIS','OAKLEY STRATUS','PRETO');
INSERT INTO RNR_PRODUTOS VALUES (15,'SHORTS','TOMMY HILFIGER JEANS','VERMLHO');

INSERT INTO RNR_DEP VALUES (135,'03527-900','Avenida Aricanduva, 5555','CAMISETA','5000');
INSERT INTO RNR_DEP VALUES (136,'09726-252','Avenida Kennedy, 700 - 323','CAL�A','2500');
INSERT INTO RNR_DEP VALUES (137,'09750-700','Pra�a Samuel Sabatini, 200','TENIS','1250');
INSERT INTO RNR_DEP VALUES (138,'08220-000','Avenida Jos� Pinheiro Borges','SHORTS','525');

INSERT INTO RNR_LOJA VALUES (1381,'09171-828','Rua Tipuana,525');
INSERT INTO RNR_LOJA VALUES (1482,'09175-370','Travessa General Klinger,231');
INSERT INTO RNR_LOJA VALUES (1583,'09071-030','Rua G�meos,439');
INSERT INTO RNR_LOJA VALUES (1684,'09210-820','Pra�a Dos Esportes,195');

INSERT INTO RNR_VENDEDOR VALUES ('JBX',1381,'Jota Glesber Santana');
INSERT INTO RNR_VENDEDOR VALUES ('AVX',1482,'Ana Vit�ria Sanzinni');
INSERT INTO RNR_VENDEDOR VALUES ('CLX',1583,'Claudinei Lopes');
INSERT INTO RNR_VENDEDOR VALUES ('TSX',1684,'Tico Santana Cruz');

INSERT INTO RNR_VENDAS VALUES (1423,1381,'JBX',1,12,1,259,'9D332',15,'15/01/2023');
INSERT INTO RNR_VENDAS VALUES (1523,1583,'CLX',2,13,2,858,'O4VNK',25,'05/01/2023');
INSERT INTO RNR_VENDAS VALUES (1623,1684,'TSX',3,14,4,369,'A0TG7',15,'24/01/2023');
INSERT INTO RNR_VENDAS VALUES (1723,1482,'AVX',4,15,6,86,'WBI74',32,'20/12/2022');

SELECT * FROM RNR_ENTREGA;
COMMIT;