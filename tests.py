##PRUEBA SERVER

import unittest
import json
from unittest.mock import patch
from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus

# Importa la función que maneja las solicitudes HTTP
from Connector import get_properties

class TestHttpServer(unittest.TestCase):
    def setUp(self):
        self.server = HTTPServer(('localhost', 8080), BaseHTTPRequestHandler)

    def tearDown(self):
        self.server.server_close()

    @patch('http.server.HTTPServer')
    def test_handle_get_request(self, mock_http_server):
        # Define una solicitud GET simulada
        request = unittest.mock.Mock()
        request.method = 'GET'

        # Define el servidor HTTP
        server_instance = mock_http_server.return_value
        server_instance.socket.getsockname.return_value = ('localhost', 8080)

        # Llama a la función que maneja las solicitudes GET
        response = handle_get_request(request)

        # Verifica que la respuesta sea la esperada
        expected_content = json.dumps(get_properties())
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.headers['content-type'], 'application/json')
        self.assertEqual(response.content.decode('UTF-8'), expected_content)

if __name__ == '__main__':
    unittest.main()

##PRUEBA CONNECTOR QUERRY

import unittest
from unittest.mock import patch
from Connector import get_properties

class TestGetProperties(unittest.TestCase):
    @patch('mysql.connector.connect')
    def test_get_properties(self, mock_connect):
        # Simulamos la conexión a la base de datos
        mock_cursor = mock_connect.return_value.cursor.return_value
        expected_result = [{'city': 'City1', 'address': 'Address1', 'price': 100000, 'description': 'Description1', 'name': 'Status1'}]

        # Simulamos la ejecución de la consulta
        mock_cursor.fetchall.return_value = expected_result

        # Llamamos a la función que queremos probar
        result = get_properties()

        # Verificamos que la función devuelva el resultado esperado
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
