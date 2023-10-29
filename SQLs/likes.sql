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