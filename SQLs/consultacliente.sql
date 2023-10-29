--Constulta ultimo estado

SELECT p.city, p.address, p.price, p.description, s.name
FROM property p
JOIN (
    SELECT sh.property_id, MAX(sh.update_date) as max_update_date
    FROM status_history sh
    GROUP BY sh.property_id
) latest_sh
ON p.id = latest_sh.property_id
JOIN status_history sh
ON latest_sh.property_id = sh.property_id AND latest_sh.max_update_date = sh.update_date
JOIN status s
ON s.id = sh.status_id
WHERE p.address IS NOT NULL AND p.address <> ''
  AND p.city IS NOT NULL AND p.city <> ''
  AND p.description IS NOT NULL AND p.description <> '';


--consulta por ciudad

SELECT p.city, p.address, p.price, p.description, s.name
FROM property p
JOIN (
    SELECT sh.property_id, MAX(sh.update_date) as max_update_date
    FROM status_history sh
    GROUP BY sh.property_id
) latest_sh
ON p.id = latest_sh.property_id
JOIN status_history sh
ON latest_sh.property_id = sh.property_id AND latest_sh.max_update_date = sh.update_date
JOIN status s
ON s.id = sh.status_id
WHERE p.address IS NOT NULL AND p.address <> ''
  AND p.city IS NOT NULL AND p.city <> ''
  AND p.description IS NOT NULL AND p.description <> ''
 AND p.city=%(city)s;

 --consulta por status

 SELECT p.city, p.address, p.price, p.description, s.name
FROM property p
JOIN (
    SELECT sh.property_id, MAX(sh.update_date) as max_update_date
    FROM status_history sh
    GROUP BY sh.property_id
) latest_sh
ON p.id = latest_sh.property_id
JOIN status_history sh
ON latest_sh.property_id = sh.property_id AND latest_sh.max_update_date = sh.update_date
JOIN status s
ON s.id = sh.status_id
WHERE p.address IS NOT NULL AND p.address <> ''
  AND p.city IS NOT NULL AND p.city <> ''
  AND p.description IS NOT NULL AND p.description <> ''
 AND s.name='pre_venta';