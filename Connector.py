import mysql.connector

conexion = mysql.connector.connect(
    host='',
    port='3309',
    user='',
    password='',
    database='habi_db'
)

cursor = conexion.cursor(dictionary=True)

querry = """
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
"""


def get_properties():
    try:
        cursor.execute(querry)
        equal = cursor.fetchall()
        cursor.close
        conexion.close
        return equal 
    except:
        print("An exception occurred")