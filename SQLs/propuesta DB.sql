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