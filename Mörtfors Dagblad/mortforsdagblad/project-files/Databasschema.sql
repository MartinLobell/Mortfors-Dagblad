\c m11p3220;

CREATE TABLE artikel (
    art_id SERIAL,
    rubrik VARCHAR(60),
    ingress VARCHAR(60),
    text VARCHAR(200),
    datum DATE,
    undkat_id INT,
    PRIMARY KEY (art_id)
    FOREIGN KEY (undkat_id) REFERENCES underkategori(undkat_id)
);

CREATE TABLE journalist (
    p_nr SERIAL,
    namn VARCHAR(40),
    telefon VARCHAR(11),
    email VARCHAR(50),
    kontaktbild varchar(30),
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
    bildfil VARCHAR(30),
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
    username VARCHAR(20),
    password VARCHAR(20)
);

CREATE TABLE kategori {
    kat_id INT,
    kategorinamn VARCHAR(20),
    PRIMARY KEY (kat_id)
}

CREATE TABLE underkategori {
    undkat_id INT,
    underkategorinamn VARCHAR(20),
    kat_id INT,
    PRIMARY KEY (undkat_id),
    FOREIGN KEY (kat_id) REFERENCES kategori(kat_id)
}

INSERT INTO journalist (p_nr, namn, telefon, email, anteckning) VALUES 
(1, 'Eyvind Svensson', '0702-662244', 'eyvind_da_man@mfdb.se', 'eyvind.jpg', 'Chefredaktör på Mörtfors dagblad'),
(2, 'Karl-Alfred S. Åhs', '0709-425521', 'karlalfredahs@mfdb.se', 'karlalfred.jpg', 'Nyhetschef på Mörtfors dagblad'),
(3, 'Ann-Christine Hollandaise', '0707-998877', 'anki.holland@mfdb.se', 'annchristine.jpg', 'Afrika-korrespondent, bosatt i Khartoum'),
(4, 'Guido Bolognese', '0141-126431', 'pestopojken@mfdb.se', 'guido.jpg', 'Matskribent, strandsatt i Motala.'),
(5, 'Boonsri Sriracha', '0707-376541', 'sriracha_boonsri@mfdb.se', 'boonsri.jpg', 'Ekonomisidorna.'),
(6, 'Kent von Schnabel', '0729-313131', 'jurgen@mfdb.se', 'kent.jpg', 'Skrivit om sport sen Nacka Skoglund var blott en liten sparvel.'),
(7, 'Tza Tziki', '0729-418838', 'tza_tziki_78@mfdb.se', 'tza.jpg', 'Skriver om glesbygden och agrarsamhället.'),
(8, 'Bea R. Näs', '0701-392217', 'bearnaise@mfdb.se', 'bea.jpg', 'Förtrollad av konsten och skapandet.');

INSERT INTO admin (username, password) VALUES
('Eyvind', 'Password1')

INSERT INTO kategori (kat_id, kategorinamn) VALUES
(1, 'Inrikes'),
(2, 'Utrikes'),
(3, 'Sport'),
(4, 'Nöje'),
(5, 'Mat')

INSERT INTO underkategori (undkat_id, underkategorinamn, kat_id) VALUES
(1, 'Staden', 1),
(2, 'Landsbygden', 1),
(3, 'Europa', 2),
(4, 'Nordamerika', 2),
(5, 'Sydamerika', 2),
(6, 'Afrika', 2),
(7, 'Asien', 2),
(8, 'Oceanien', 2),
(9, 'Fotboll', 3),
(10, 'Hockey', 3),
(11, 'Tennis', 3),
(12, 'Basket', 3),
(13, 'Ridsport', 3),
(14, 'Simning', 3),
(15, 'Musik', 4),
(16, 'Konst', 4),
(17, 'Film', 4),
(18, 'Litteratur', 4),
(19, 'Teater', 4),
(20, 'Varmt', 5),
(21, 'Kallt', 5)