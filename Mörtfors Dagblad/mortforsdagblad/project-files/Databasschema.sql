\c m11p3220;

CREATE TABLE artikel (
    art_id SERIAL,
    rubrik VARCHAR(60),
    ingress VARCHAR(60),
    brödtext VARCHAR(200),
    datum DATE,
    PRIMARY KEY (art_id)
);

CREATE TABLE journalist (
    p_nr SERIAL,
    namn VARCHAR(40),
    telefon VARCHAR(11),
    email VARCHAR(50),
    kontaktbild BYTEA,
    anteckning VARCHAR(100),
    PRIMARY KEY (p_nr)
);

CREATE TABLE skriven_av (
    art_id INT,
    journalist INT,
    PRIMARY KEY (art_id, journalist),
    FOREIGN KEY (art_id) REFERENCES artikel(art_id),
    FOREIGN KEY (journalist) REFERENCES journalist(p_nr)
);

CREATE TABLE bild (
    bild_id SERIAL,
    bildfil bytea,
    alt_text VARCHAR(20),
    PRIMARY KEY (bild_id)
);

CREATE TABLE artikel_bild (
    bildtext VARCHAR(50),
    art_id INT,
    bild_id INT,
    PRIMARY KEY (art_id, bild_id),
    FOREIGN KEY (art_id) REFERENCES artikel(art_id),
    FOREIGN KEY (bild_id) REFERENCES bild(bild_id)
);

CREATE TABLE kommentar (
    kom_id SERIAL,
    art_id INT,
    namn VARCHAR(30),
    kommentar VARCHAR(100),
    tid_datum TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (kom_id),
    FOREIGN KEY (art_id) REFERENCES artikel(art_id)
);

CREATE TABLE admin (
    username varchar(20),
    password varchar(20)
);

INSERT INTO journalist (p_nr, namn, telefon, email, anteckning) VALUES 
(1, 'Eyvind Svensson', '0702-662244', 'eyvind_da_man@mfdb.se', 'Chefredaktör på Mörtfors dagblad'),
(2, 'Karl-Alfred S. Åhs', '0709-425521', 'karlalfredahs@mfdb.se', 'Nyhetschef på Mörtfors dagblad'),
(3, 'Ann-Christine Hollandaise', '0707-998877', 'anki.holland@mfdb.se', 'Afrika-korrespondent, bosatt i Khartoum'),
(4, 'Guido Bolognese', '0141-126431', 'pestopojken@mfdb.se', 'Matskribent, strandsatt i Motala.'),
(5, 'Boonsri Sriracha', '0707-376541', 'sriracha_boonsri@mfdb.se', 'Ekonomisidorna.');