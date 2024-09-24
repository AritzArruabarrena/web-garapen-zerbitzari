def tablak(conectar):
    kurtzorea = conectar.cursor()
    
    clientes_tabla = """
    CREATE TABLE IF NOT EXISTS clientes (
        CodCliente INT,
        Nombre TEXT,
        Empresa TEXT,
        Puesto TEXT,
        CP INT,
        Provincia TEXT,
        Telefono INT,
        FechaNacimiento DATE,
        PRIMARY KEY(CodCliente)
    )"""
    
    articulos_tabla = """
    CREATE TABLE IF NOT EXISTS articulos (
        CodArticulo INT,
        Nombre TEXT,
        Descripcion TEXT,
        PrecioUnidad FLOAT,
        UnidadesEnStock INT,
        StockSeguridad INT,
        Imagen TEXT,
        PRIMARY KEY(CodArticulo)
    )"""
    
    
    compra_tabla = """
    CREATE TABLE IF NOT EXISTS compra (
        CodCliente INT,
        CodArticulo INT,
        Fecha DATE,
        Unidades INT,
        PRIMARY KEY (CodCliente, CodArticulo, Fecha),
        FOREIGN KEY (CodCliente) REFERENCES clientes(CodCliente),
        FOREIGN KEY (CodArticulo) REFERENCES articulos(CodArticulo)
    )"""
    
    kurtzorea.execute(clientes_tabla)
    kurtzorea.execute(articulos_tabla)
    kurtzorea.execute(compra_tabla)
    
    conectar.commit()
    kurtzorea.close()
    

def datuak_bete(conectar):
    kurtzorea = conectar.cursor()
    
    clientes_datuak = "INSERT INTO clientes VALUES('1','José','Fernández Ruiz','Estudio Cero','Gerente','41400','Sevilla','656789043','13/06/1968') , ('2','Luis','Fernández Chacon','Beep','Dependiente','41400','Sevilla','675894566','24/05/1982'), ('3','José','Fernández Ruiz','Estudio Cero','Gerente','41400','Sevilla','656789043','13/06/1968')"
    
    articulos_datuak = "INSERT INTO articulos VALUES('','','','','','','')"