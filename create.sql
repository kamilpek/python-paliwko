CREATE TABLE tankowanie(przebieg int not null, ilosc float not null, koszt float not null, cena float);


INSERT INTO tankowanie(przebieg, ilosc, koszt) VALUES(1,250321,21,99.98);


cur.execute("INSERT INTO tankowanie(przebieg, ilosc, koszt) VALUES(250321,21,99);")


def czyszczenie(self):
	cur.execute("DROP TABLE tankowanie;")
	cur.execute("CREATE TABLE tankowanie(przebieg int not null, ilosc float not null, koszt float not null, cena float);")
