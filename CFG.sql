USE CFG;

CREATE TABLE Rep
(RepNum CHAR(2) PRIMARY KEY,
LastName CHAR(15),
FirstName CHAR(15),
Street CHAR(15),
City CHAR(15),
State CHAR(2),
PostalCode CHAR(5),
Commission DECIMAL(7,2),
Rate DECIMAL(3,2) );

CREATE TABLE Customer
(CustomerNum CHAR(3) PRIMARY KEY,
CustomerName CHAR(35) NOT NULL,
Street CHAR(20),
City CHAR(15),
State CHAR(2),
PostalCode CHAR(5),
Balance DECIMAL(8,2),
CreditLimit DECIMAL(8,2),
RepNum CHAR(2) );

CREATE TABLE Orders
(OrderNum CHAR(5) PRIMARY KEY,
OrderDate DATE,
CustomerNum CHAR(3) );

CREATE TABLE Item
(ItemNum CHAR(4) PRIMARY KEY,
Description CHAR(30),
OnHand DECIMAL(4,0),
Category CHAR(3),
Storehouse CHAR(1),
Price DECIMAL(6,2) );

CREATE TABLE OrderLine
(orderNum CHAR(5),
ItemNum CHAR(4),
NumOrdered DECIMAL(3,0),
QuotedPrice DECIMAL(6,2),
PRIMARY KEY (OrderNum, ItemNum) );

CREATE TABLE User
(username VARCHAR(32) UNIQUE,
passwordHash CHAR(97),
PRIMARY KEY (username, passwordHash) );

CREATE TABLE Logins
(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(32),
loginTime DATETIME );

CREATE TABLE Logouts
(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(32),
loginTime DATETIME );

INSERT INTO REP
VALUES
('15','Campos','Rafael','724 Vinca Dr.','Grove','CA','90092',23457.50,0.06);
INSERT INTO REP
VALUES
('30','Gradey','Megan','632 Liatris St.','Fullton','CA','90085',41317.00,0.08);
INSERT INTO REP
VALUES
('45','Tian','Hui','1785 Tyler Ave.','Northfield','CA','90098',27789.25,0.06);
INSERT INTO REP
VALUES
('60','Sefton','Janet','267 Oakley St.','Congaree','CA','90097',0.00,0.06);
INSERT INTO CUSTOMER
VALUES
('126','Toys Galore','28 Laketon St.','Fullton','CA','90085',1210.25,7500.00,'15');
INSERT INTO CUSTOMER
VALUES
('260','Brookings Direct','452 Columbus Dr.','Grove','CA','90092',575.00,10000.00,'30');
INSERT INTO CUSTOMER
VALUES
('334','The Everything Shop','342 Magee St.','Congaree','CA','90097',2345.75,7500.00,'45');
INSERT INTO CUSTOMER
VALUES
('386','Johnson''s Department Store','124 Main St.','Northfield','CA','90098',879.25,7500.00,'30');
INSERT INTO CUSTOMER
VALUES
('440','Grove Historical Museum Store','3456 Central Ave.','Fullton','CA','90085',345.00,5000.00,'45');
INSERT INTO CUSTOMER
VALUES
('502','Cards and More','167 Hale St.','Mesa','CA','90104',5025.75,5000.00,'15');
INSERT INTO CUSTOMER
VALUES
('586','Almondton General Store','3345 Devon Ave.','Almondton','CA','90125',3456.75,15000.00,'45');
INSERT INTO CUSTOMER
VALUES
('665','Cricket Gift Shop','372 Oxford St.','Grove','CA','90092',678.90,7500.00,'30');
INSERT INTO CUSTOMER
VALUES
('713','Cress Store','12 Rising Sun Ave.','Congaree','CA','90097',4234.60,10000.00,'15');
INSERT INTO CUSTOMER
VALUES
('796','Unique Gifts','786 Passmore St.','Northfield','CA','90098',124.75,7500.00,'45');
INSERT INTO CUSTOMER
VALUES
('824','Kline''s','945 Gilham St.','Mesa','CA','90104',2475.99,15000.00,'30');
INSERT INTO CUSTOMER
VALUES
('893','All Season Gifts','382 Wildwood Ave.','Fullton','CA','90085',935.75,7500.00,'15');
INSERT INTO ORDERS
VALUES
('51608','2015-10-12','126');
INSERT INTO ORDERS
VALUES
('51610','2015-10-12','334');
INSERT INTO ORDERS
VALUES
('51613','2015-10-13','386');
INSERT INTO ORDERS
VALUES
('51614','2015-10-13','260');
INSERT INTO ORDERS
VALUES
('51617','2015-10-15','586');
INSERT INTO ORDERS
VALUES
('51619','2015-10-15','126');
INSERT INTO ORDERS
VALUES
('51623','2015-10-15','586');
INSERT INTO ORDERS
VALUES
('51625','2015-10-16','796');
INSERT INTO ITEM
VALUES
('AH74','Patience',9.00,'GME','3',22.99);
INSERT INTO ITEM
VALUES
('BR23','Skittles',21.00,'GME','2',29.99);
INSERT INTO ITEM
VALUES
('CD33','Wood Block Set (48 piece)',36.00,'TOY','1',89.49);
INSERT INTO ITEM
VALUES
('DL51','Classic Railway Set',12.00,'TOY','3',107.95);
INSERT INTO ITEM
VALUES
('DR67','Giant Star Brain Teaser',24.00,'PZL','2',31.95);
INSERT INTO ITEM
VALUES
('DW23','Mancala',40.00,'GME','3',50.00);
INSERT INTO ITEM
VALUES
('FD11','Rocking Horse',8.00,'TOY','3',124.95);
INSERT INTO ITEM
VALUES
('FH24','Puzzle Gift Set',65.00,'PZL','1',38.95);
INSERT INTO ITEM
VALUES
('KA12','Cribbage Set',56.00,'GME','3',75.00);
INSERT INTO ITEM
VALUES
('KD34','Pentominoes Brain Teaser',60.00,'PZL','2',14.95);
INSERT INTO ITEM
VALUES
('KL78','Pick Up Sticks',110.00,'GME','1',10.95);
INSERT INTO ITEM
VALUES
('MT03','Zauberkasten Brain Teaser',45.00,'PZL','1',45.79);
INSERT INTO ITEM
VALUES
('NL89','Wood Block Set (62 piece)',32.00,'TOY','3',119.75);
INSERT INTO ITEM
VALUES
('TR40','Tic Tac Toe',75.00,'GME','2',13.99);
INSERT INTO ITEM
VALUES
('TW35','Fire Engine',30.00,'TOY','2',118.95);
INSERT INTO OrderLine
VALUES
('51608','CD33',5.00,86.99);
INSERT INTO OrderLine
VALUES
('51610','KL78',25.00,10.95);
INSERT INTO OrderLine
VALUES
('51610','TR40',10.00,13.99);
INSERT INTO OrderLine
VALUES
('51613','DL51',5.00,104.95);
INSERT INTO OrderLine
VALUES
('51614','FD11',1.00,124.95);
INSERT INTO OrderLine
VALUES
('51617','NL89',4.00,115.99);
INSERT INTO OrderLine
VALUES
('51617','TW35',3.00,116.95);
INSERT INTO OrderLine
VALUES
('51619','FD11',2.00,121.95);
INSERT INTO OrderLine
VALUES
('51623','DR67',5.00,29.95);
INSERT INTO OrderLine
VALUES
('51623','FH24',12.00,36.95);
INSERT INTO OrderLine
VALUES
('51623','KD34',10.00,13.10);
INSERT INTO OrderLine
VALUES
('51625','MT03',8.00,45.79);

