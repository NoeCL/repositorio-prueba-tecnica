# repositorio-prueba-tecnica

**Actividades**
- [x] Repositorio en Git
- [x] README
- [x] Servidor de Consulta
- [x] Filtros
- [x] Manejo de exepciones
- [x] Concepto de ME GUSTA diagrama ER
- [x] Concepto de ME GUSTA codigo 
- [x] Pruebas Unitarias
- [x] Propuesta de mejora


**Tecnologias utilizadas**

- Base de Datos MySQL
- Python
- - lib mysql.connector
- - httpserver python



**Concepto de "Me gusta"**

Para el concepto de “Me gusta” es necesario integrar entidades nuevas a la base de datos en las cuales se almacenen atributos con los que relacionar los valores de id_property, id_user y id_like con el fin de establecer que la relación de los clientes(customer) con el concepto “megusta” (likes) es de uno a muchos ya que los clientes pueden dar likes a una o muchas propiedades y la relación entre “me gusta” y propiedades(property) es de muchos a uno ya que una sola propiedad puede recibir likes de diferentes clientes.

![Diagrama ER](images/Diagrama%20ER1.png?raw=true "Diagrama ER")
![Diagrama ER](images/Diagrama%20ER2.png?raw=true "Diagrama ER")



```sql
--tablas para cocepto "Me_gusta"

CREATE TABLE customer (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
    created_at timestamp NOW(),
    updated_at timestamp,
    deleted_at timestamp,
);


CREATE TABLE property (
    id_property INT AUTO_INCREMENT PRIMARY KEY,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    description TEXT
    created_at timestamp NOW(),
    updated_at timestamp,
    deleted_at timestamp,
);


CREATE TABLE likes (
    id_like INT AUTO_INCREMENT PRIMARY KEY,
    id_customer INT NOT NULL,
    id_property INT NOT NULL,
    created_at timestamp NOW(),
    updated_at timestamp,
    deleted_at timestamp,
    FOREIGN KEY (id_customer) REFERENCES customer (id_user),
    FOREIGN KEY (id_property) REFERENCES property (id_property)
);

```

**Propuesta de mejora**

Como propuesta de mejora en las consultas, una manera más eficaz de realizar las búsquedas podría ser generando nuevos campos en la tabla de propiedad que permitan agregar filtros generales como el tipo de vivienda o características adicionales de la misma (medidas, antigüedad, espacios), agregar también un campo en la tabla de usuarios que permita definir dos tipos de usuario para los clientes y los brokers de esta manera usar los identificadores para establecer una relación entre los clientes y sus brokers favoritos con los cueles seguir sus búsquedas.


![Diagrama ER](images/DBpro.png?raw=true "Diagrama ER")


```sql

--Tablas
CREATE TABLE user (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    user_type ENUM ('client', 'broker', 'admin'),
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at timestamp NOW(),
    updated_at timestamp,
    deleted_at timestamp,
    FOREIGN KEY (id_type) REFERENCES user_type (id_type)
);


CREATE TABLE favorite (
    id_customer INT,
    id_property INT,
    created_at timestamp NOW(),
    updated_at timestamp,
    deleted_at timestamp,
    FOREIGN KEY (id_customer) REFERENCES user (id_user),
    FOREIGN KEY (id_property) REFERENCES property (id_property)
);


CREATE TABLE property (
    id_property INT AUTO_INCREMENT PRIMARY KEY,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2),
    year INT,
    spc_num INT,
    m2 DECIMAL(10, 2),
    user_id INT,
    created_at timestamp NOW(),
    updated_at timestamp,
    deleted_at timestamp,
    FOREIGN KEY (user_id) REFERENCES user (id_user)
);
```
**Evidencia de pruebas**

Prueba realizada en postman sin aplicar ningun filtro

![evidencia1](images/Evidence1.png?raw=true "prueba sin filtro")

Prueba realizada en postman aplicando la llave "city" con el valor "bogota"

![evidenciaw](images/Evidence2.png?raw=true "prueba con filtro")