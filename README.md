# Pytest-Framework


## Pasos

Crear un virtual environment: python3.10 -m venv ~/venvs/frameworkenv

Acceder al framework: ​​cd ~/venvs/frameworkenv/bin

Activar framework: source activate

Desactivar framework: deactivate

Dentro del framework se debe acceder a la carpeta donde se tienen los archivos de pruebas

Para poder correr pruebas, instalamos pytest: pip install pytest

Corremos pytest para correr las pruebas: pytest


## Notas

- Para que pytest reconozca funciones como casos de prueba, deben tener un nombre que comience con "test_"
- Para correr los tests de un directorio en particular: pytest directory/subdirectory
- Para obtener información más detallada utilizamos verbose: pytest -v
- Para mostrar los standard out por linea de consola incluso en casos de éxito, se debe agregar -s al comando para correr los tests: pytest -s
- Para poder usar selenium y webdriver debemos instalar selenium y webdriver_manager: 'pip install selenium' y luego 'pip install webdriver-manager'
- Cuando una función de caso de prueba pasa con éxito, suele identificarlo con un punto .
- Cuando una función de caso de prueba falla, suele identificarlo con la letra F
- Para poder ver que paquetes tengo instalado en un ambiente: pip list

## Configuraciones

- Para configurar pytest se puede utilizar el archivo pytest.ini
- Para configurar el proyecto para usar diferentes environments se puede utilizar el archivo config.py con funciones inicializadoras que luego utilizamos desde el archivo conftest.py con el uso de 'parser'
- Si se definen textos de help, las opciones customizadas se mostrarán en pytest -h


## Marcadores

Se pueden configurar marcadores en pytest.ini y utilizar en las diferentes pruebas.
Para listar todos los marcadores registrados: pytest --markers
Para correr solo las pruebas de un marcador: pytest -m marker_name
Para correr las pruebas de varios marcadores: pytest -m "marker_name or another_marker"
Para correr las pruebas que tienen varios marcadores a la vez: pytest -m "marker_name and another_marker"
Para correr todas las pruebas excepto las de un marcador: pytest -m "not marker_name"

## Clases

Se pueden marcar las clases, lo que implicará que todos los métodos de esas clases tendrán el mismo marcador

## Fixtures

Los fixtures se definen en el archivo conftest.py y se pueden utilizar desde cualquier archivo en la carpeta dondese encuentre y las subcarpetas de la misma
Los fixtures pueden manejar su propio teardown, utilzando la palabra clave 'yield', todo lo que se defina después son las actividades de teardown
Un fixture puede tener los siguientes scopes:
- function: usa una unica instancia por función, sin importar cuantas veces se lo llame. Es el valor por defecto en caso de que no se defina un scope
- session: usa una unica instancia en la totalidad de la sesión de testeo
- class
- module
- package

## Reportes

### Reportes html con pytest-html

Para generar reportes en un archivo html instalamos pytest-html: pip install pytest-html
Para generar un reporte corremos las pruebas indicando el nombre del archivos a generar: pytest --html="results.html"

### Reportes xml con pytest core

Para generar reportes xml corremos las pruebas indicando el nombre del archivo a generar: pytest --junitxml="results.xml"


## Integración con Jenkins
 -- To Do --

## Skip de tests

Se puede usar el marcador skip para saltar una prueba: @mark.skip
Se puede definir una razón para skipear una prueba: @mark.skip(reason="XX") y se puede leer con las opciones '-rs' para leer (read) los skips

## Fallas esperadas

Para definir un caso de prueba que se espera que falle, se usa el marcador xfail: @mark.xfail
Se puede definir una razón para esperar una falla: @mark.xfail(reason="XX") y se puede leer con '-rx'