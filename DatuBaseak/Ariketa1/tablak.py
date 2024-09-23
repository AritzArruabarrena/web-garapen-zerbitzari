def tablak(conectar):
    kurtzorea = conectar.cursor()
    
    Ikasleak_tabla = "CREATE TABLE ikasleak (ikasle_kodea int, izena text, abizena text, PRIMARY KEY(ikasle_kodea))"
    Ikasgaiak_tabla = "CREATE TABLE ikasgaiak (ikasgai_kodea int, izena text, maila text, hizkuntza text, PRIMARY KEY(ikasgai_kodea))"
    
    notak_tabla = (
        "CREATE TABLE notak ("
        "notak int, "
        "oharra text, "
        "ikasle_kodea int, "
        "ikasgai_kodea int, "
        "FOREIGN KEY (ikasgai_kodea) REFERENCES ikasgaiak(ikasgai_kodea), "
        "FOREIGN KEY (ikasle_kodea) REFERENCES ikasleak(ikasle_kodea)"
        ")"
    )
    
    kurtzorea.execute(Ikasleak_tabla)
    kurtzorea.execute(Ikasgaiak_tabla)
    kurtzorea.execute(notak_tabla)
    
    conectar.commit()
    kurtzorea.close()


def datuak_bete(conectar):
    kurtzorea = conectar.cursor()
    
    Ikasleak_datuak = "INSERT INTO ikasleak VALUES(123, 'aritz', 'Arruabarrena'), (143, 'Jon', 'Telleria')"
    
    Ikasgai_datuak = "INSERT INTO ikasgaiak VALUES(321, 'Matematika', '1.maila', 'Euskera'), (532, 'Historia', '2.maila', 'Gaztelera')"
    
    notak_datuak = "INSERT INTO notak (notak, oharra, ikasle_kodea, ikasgai_kodea) VALUES (85, 'Oso ondo', 123, 321), (75, 'Ongi', 143, 532)"
    
    kurtzorea.execute(Ikasleak_datuak)
    kurtzorea.execute(Ikasgai_datuak)
    kurtzorea.execute(notak_datuak)
    
    conectar.commit()
    kurtzorea.close()


def taulak_ezabatu(conectar):
    kurtzorea = conectar.cursor()
    
    kurtzorea.execute("SET FOREIGN_KEY_CHECKS = 0")  
    kurtzorea.execute("DROP TABLE IF EXISTS notak")
    kurtzorea.execute("DROP TABLE IF EXISTS ikasleak")
    kurtzorea.execute("DROP TABLE IF EXISTS ikasgaiak")
    kurtzorea.execute("SET FOREIGN_KEY_CHECKS = 1")  
    
    conectar.commit()
    kurtzorea.close()
    

def datuak_ezabatu(conectar):
    kurtzorea = conectar.cursor()
    
    Ikasleak_ezabatu = "DELETE FROM ikasleak WHERE ikasle_kodea = 123"
    
    Ikasgai_ezabatu = "DELETE FROM ikasgaiak WHERE ikasgai_kodea = 321"
    
    notak_ezabatu = "DELETE FROM notak WHERE ikasle_kodea = 123 && ikasgai_kodea = 321"
    
    kurtzorea.execute(Ikasleak_ezabatu)
    kurtzorea.execute(Ikasgai_ezabatu)
    kurtzorea.execute(notak_ezabatu)
    
    conectar.commit()
    kurtzorea.close()
    

def ikaslea_sortu(conectar,kodea,izena,abizena):
    
    kurtzorea = conectar.cursor()
    
    Ikaslea_gehitu = "INSERT INTO ikasleak VALUES(%s, %s, %s)"
    
    datuak = (kodea,izena,abizena)
    
    kurtzorea.execute(Ikaslea_gehitu,datuak)
    
    conectar.commit()
    kurtzorea.close()
    

def nota_sartu(conectar,notak,oharra,ikasle_kodea,ikasgai_kodea):
    
    kurtzorea = conectar.cursor()
    
    nota_sartu = "INSERT INTO notak VALUES(%s, %s, %s, %s)"
    
    datuak = (notak,oharra,ikasle_kodea,ikasgai_kodea)
    

    
    kurtzorea.execute(nota_sartu,datuak)
    
    conectar.commit()
    kurtzorea.close()


def nota_aldatu(conectar,notak,ikasle_kodea, ikasgai_kodea):
    
    kurtzorea = conectar.cursor()
    
    nota_aktualizatu = "UPDATE notak SET notak =  %s WHERE ikasle_kodea = %s OR ikasgai_kodea = %s"
    
    datuak = (notak,ikasle_kodea,ikasgai_kodea)
    
    kurtzorea.execute(nota_aktualizatu,datuak)
    
    conectar.commit()
    kurtzorea.close()
    

def gehitu_ikasgaia(conectar,ikasgai_kodea,izena,maila,hizkuntza):
    
    kurtzorea = conectar.cursor()
    
    ikasgaia_gehitu = "INSERT INTO ikasgaiak VALUES(%s, %s, %s,%s)"
    
    datuak = (ikasgai_kodea,izena,maila,hizkuntza)
    
    kurtzorea.execute(ikasgaia_gehitu,datuak)
    
    conectar.commit()
    kurtzorea.close()
    

def ezabatu_ikaslea(conectar,ikasle_kodea):
    
    kurtzorea = conectar.cursor()
    
    ikaslea_ezabatu = "DELETE FROM ikasleak WHERE ikasle_kodea = %s"
    
    datuak = (ikasle_kodea,)
    
    kurtzorea.execute(ikaslea_ezabatu,datuak)
    
    conectar.commit()
    kurtzorea.close()
