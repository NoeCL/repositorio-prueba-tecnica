import mysql.connector ##importa libreria de mysql

conexion = mysql.connector.connect( ##informacion de acceso a la DB
    host='',
    port='',
    user='',
    password='',
    database=''
)

cursor = conexion.cursor(dictionary=True)

query = """
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
query_by_city = '''
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
'''

def get_properties():
    try:
        cursor.execute(query)
        equal = cursor.fetchall()
        cursor.close
        conexion.close
        return equal 
    except:
        print("An exception occurred")

def get_propertie_by_city(city):
    try:
        cursor.execute(query_by_city,{"city": city})
        equal = cursor.fetchall()
        cursor.close
        conexion.close
        return equal
    except:
        print("An exeption ocurred")