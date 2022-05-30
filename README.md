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
- Para poder usar selenium y webdriver debemos instalar selenium y webdriver_manager: 'pip install selenium' y luego 'pip install webdriver-manager'. (o agregar los diferentes drivers directamente al PATH)
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

Los fixtures se definen en el archivo conftest.py y se pueden utilizar desde cualquier archivo en la carpeta donde se encuentre y las subcarpetas de la misma
Los fixtures pueden manejar su propio teardown, utilzando la palabra clave 'yield', todo lo que se defina después son las actividades de teardown
Los fixtures son llamados cuando son usados (como argumento de una función), por lo que definir una función dentro de un fixture permite atrasar el momento de llamado de la función interna
Un fixture puede tener los siguientes scopes:
- function: usa una unica instancia por función, sin importar cuantas veces se lo llame. Es el valor por defecto en caso de que no se defina un scope
- session: usa una unica instancia en la totalidad de la sesión de testeo
- class: corre una vez por clase
- module: corre una vez para un modulo
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

## Parametros

Podemos definir parámetros para una función de testeo con el marcador parametrize, definiendo el nombre del parametro y los posibles valores, y de esta forma la funcion se ejecutará 1 vez por cada parámetro
También podemos definir parámetros para un fixture, en ese caso se ejecutará la función que haga uso del fixture 1 vez por cada parámetro del mismo

## Tests en paralelo

Podemos usar la librería pytest-xdist: pip install pytest-xdist
De esta manera podemos definir el numero de threads a utilizar durante los tests. Por ejemplo para 4 threads: pytest tests/parallel -n4
Es importante que los tests sean modulares y no dependientes de otros tests para que no interfieran con el uso de memoria
Tambien podemos delegar la selección del número de threads de forma automática: pytest tests/parallel -nauto

## Selenium

Instalamos selenium: pip install selenium
Instalamos también los drivers de los navegadores que utilizaremos. Debemos recordar agregar el directorio en el que se encuentran los drivers al PATH 

### Automatizar desde la consola
- Entramos a la consola de python: python
- Import del webdriver: from selenium import webdriver
- Definimos un browser: browser = webdriver.Chrome()
- Accedemos a una pagina: browser.get("https://techstepacademy.com/training-ground")
- Podemos guardar el path del elemento en una variable auxiliar: input1Path = "input[id='ipt1']"
- Import del By: from selenium.webdriver.common.by import By
- Encontramos el elemento: input1Element = browser.find_element(By.CSS_SELECTOR, input1Path)
- Enviamos modificaciones: input1Element.send_keys("Automated input content")

#### Selectores CSS
- Se pueden utilizar con By.CSS_SELECTOR
- Desde la consola del inspector podemos probar selectores CSS con: $$("selector CSS")
- Selector por id: input#ipt1 ó input[id='ipt1']

#### XPATH
- Se pueden utilizar con By.XPATH
- Desde la consola del inspector podemos probar xpath con: $x("camino hacia elemento")
- Ejemplos: //button[@name='butn1'], //b[contains(text(), 'Product 1')]/../../p

#### Otros By
- ID = "id"
- XPATH = "xpath"
- LINK_TEXT = "link text"
- PARTIAL_LINK_TEXT = "partial link text"
- NAME = "name"
- TAG_NAME = "tag name"
- CLASS_NAME = "class name"
- CSS_SELECTOR = "css selector"
