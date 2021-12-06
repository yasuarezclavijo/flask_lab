# Arquitectura Flask Proyectos APPS.CO

Esta documentación tiene como objetivo dar guia de uso a la arquitectura de una webapp escalable y con altos coheficientes de rendimiento con el uso del framework FLASK-PYTHON.
## Descripción
Este ha sido un scaffolding (andamiaje) diseñado y creado por Yeison Andrés Suárez buscando satisfacer la mayor parte de necesidades encontradas durante las etapas de asesoría con el programa APPS.CO en las cuales emprendedores decidieron como
stack de desarrollo abordar el universo del framework Flask (Python)

En este documento se entregara una detallada forma de ponerlo en ejecución, algunas reglas que seguir y 2 apps (módulos) de ejemplo (Versión monolítica y manejo de API's para sitios desacoplados)

En ambos casos se han implementado los paquetes más estables y conocidos en el mercado basado en un patrón factory y con una
arquitectura de aplicaciónes web escalables de alto rendimiento.

## Paquetes relevantes
- **flask:** Core framework principal
- **flask-wtf:** Libreria para manejo de formularios a traves de clases.
- **bootstrap-flask**: Templates, tags y funcionalidades propias de bootstrap para incluirlas nativamente en flask.
- **sqlalchemy**: ORM para manejo de base de datos como Objetos.
- **wtforms-sqlalchemy**: Inclusión de clases y funcionalidades propias para formularios y  manejo de ModelForm, enlanzando el ORM con los formularios.
- **alembic:** Manejador de migraciones (Migración: Capacidad de progresivamente ir causando cambios DDL en la base de datos.)
- **Flask-RESTful:** Libreria de arquitectura para manejo de API's tipor RESTful.
- **flask-marshmallow:** Manejador de serializadores enlazados con los modelos de ORM Alchemy.
- **Flask-SQLAlchemy:** Una extensión de Flask que agrega soporte para SQLAlchemy, un mapeador relacional de objetos que nos facilita la interacción con bases de datos SQL.
## Arquitectura
Como ya se menciono esta arquitectura ha sido diseñada buscando satisfacer los problemas mas comunes de rendimiento y buenas practicas en el desarrollo apoyado del framework FLASK motivo por el cual se causa una arquitectura modular apoyado en PATRONES DE DISEÑO como factory y singleton como primera instancia para mantener el principio de granularidad y división de responsabilidades dentro de nuestro proyecto.

**Directorios:**
- *Alembic:* Directorio creado a partir del comando `alembic init alembic` manejo de migraciones con alembic.
- *app:* Carpeta contenedora de módulos escalares para la aplicación.
- *core:* Carpeta con factory.py y archivos necesarios para mantener dividido la lógica de implementación y sistema módular.
- *config.py:* Archivo con datos de configuración.
- *requirements.txt:*Archivos de librerias y versiones instaladas dentro del virtual enviroment para el correcto funcionamiento.
- *run.py:* Archivo que inicia objeto Flask e inicia app en modo `__main__`
- *services.py:* Archivo encargado de iniciar los servicios de base de datos, logging y marshallow, lo ideal seria que cualquier instanciación de objetos deberia hacerse en este archivo (module)
- *settings.py:* Archivo para cargar constantes usadas tranversalmente el programa.
## INSTALACIÓN
1. Crear su entorno virtual
2. Correr el comando `pip install -r requirements.txt`
3. Cree una base de datos en blanco en su motor
4. Configurar variables de entorno bien sea en su `.env` o dentro de su entorno virtual.
    Funciona con POSTGRESQL si requiere otro motor de base de datos debera alterar el archivo config.py con la URL de acceso a su respectivo motor, *IMPORTANTE* siga usando variables de entorno nunca directo en el código.
5. Una vez completada esta configuración, ejecute `alembic upgrade head` este comando recreara las migraciones ya creadas para este demo.

## Uso para sus proyectos

En el archivo settings puede borrar los elementos de la lista *INSTALLED_APPS* para que el demo no se active, lo que debera proceder de aqui en adelante es SIEMPRE sus módulos deberan estar en la carpeta *app/* y ser incluidos en dicha lista bajo el nombre `app.nombre_carpeta_su_modulo` esto lo incluira como blueprint de su proyecto.

Cada módulo que cree siempre debera contener unas lineas similares a estas en su archivo *__init__.py*

`
from flask import Blueprint
api_bp = Blueprint('api', __name__)
from . import archivo_rutas
`
Si desea guiarse en el camino monolítico apoyese por favor en el módulo *example* si por el contrario requiere exponer API's RestFul la carpeta guia a seguir sera *api*

Una vez creado el nuevo módulo debera dirigirse a la ubicación *alembic/env.py* ubicar las lineas donde se ubica la variable *target_metadata* realizar la importación desde app.nombre_carpeta ipmort models as alias_model y adicionarlo a la lista de target_metadata

`
from app.example import models as example_models
from app.api import models as api_models
target_metadata = [example_models.Base.metadata, api_models.Base.metadata]
`

Destacar que sea cual sea el caso, el archivo *models.py* contendra las clases capaces de manipular y gestar su base de datos, una vez se hagan alteraciones en estos archivos (adición de campo, nuevos módelos, cambios tipo de dato) SIEMPRE se debera causar una nueva migración con el comando `alembic revision --autogenerate -m "Message for migrate"` en la instrucción -m se pondra un mensaje de seguimiento de alembic (Similar a los mensajes commit de GIT) esto para tener un control adecuado de los momentos de corte para actualización de base de datos. Una vez generado se causara un nuevo archivo en la carpeta *alembic/versions* y finalmente llevarlo hacia la base de datos con el comando `alembic upgrade head`