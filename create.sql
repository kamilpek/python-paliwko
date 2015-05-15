CREATE TABLE tankowanie(przebieg int not null, ilosc int not null, koszt int not null, cena int);


INSERT INTO tankowanie(przebieg, ilosc, koszt) VALUES(1,250321,21,99.98);


cur.execute("INSERT INTO tankowanie(przebieg, ilosc, koszt) VALUES(250321,21,99);")
