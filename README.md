# Pytest-Framework


## Pasos

Crear un virtual environment: python3.10 -m venv ~/venvs/frameworkenv

Acceder al framework: ​​cd ~/venvs/frameworkenv/bin

Activar framework: source activate

Desactivar framework: deactivate

Dentro del framework se debe acceder a la carpeta donde se tienen los archivos de pruebas

Para correr pruebas, instalamos pytest: pip install pytest

Corremos pytest para correr las pruebas: pytest

Para obtener información más detallada: pytest -v

Para correr los tests de un directorio en particular: pytest directory/subdirectory


## Notas

- Para que pytest reconozca funciones como casos de prueba, deben tener un nombre que comience con "test_"
- Para configurar pytest se puede utilizar el archivo pytest.ini

### Marcadores

Se pueden configurar marcadores en pytest.ini y utilizar en las diferentes pruebas.
Para listar todos los marcadores registrados: pytest --markers
Para correr solo las pruebas de un marcador: pytest -m marker_name
Para correr las pruebas de varios marcadores: pytest -m "marker_name or another_marker"
Para correr las pruebas que tienen varios marcadores a la vez: pytest -m "marker_name and another_marker"
Para correr todas las pruebas excepto las de un marcador: pytest -m "not marker_name"

### Clases

Se pueden marcar las clases, lo que implicará que todos los métodos de esas clases tendrán el mismo marcador