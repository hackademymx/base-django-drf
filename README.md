# Plantilla básica de un proyecto de Django con Django Rest Framework

El objetivo de este repositorio es usarlo como una plantilla, esqueleto o también llamado `boilerplate` inicial para cualquier proyecto de API REST que use Django.

La finalidad es que sirva de guía y permita al desarrollador enfocarse en escribir código y no en invertir demasiado tiempo en la inicialización y configuración del proyecto.

## Tecnologías incluidas:
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
- [Python decouple](https://pypi.org/project/python-decouple/)
- [Django-cors-headers](https://pypi.org/project/django-cors-headers/)
- [Gunicorn](https://pypi.org/project/gunicorn/)

## Para levantar el proyecto

- Crear un archivo de configuración `.env` con las variables de entorno necesarias a partir del archivo `_.env`.

        $ cp _.env .env

- Crear el entorno virtual. En este caso se está usando la herramienta incluida de Python

        $ python -m venv env

- Activar el entorno virtual

        $ source env/bin/activate

- Instalar las dependencias del `requirements.txt` existente

        $ python -m pip install -r requirements.txt

- Levantar el servidor

        $ cd api

        $ python manage.py runserver

- Para desactivar el entorno virtual

        $ deactivate


⌨️ con ❤️ por Gabriella Martínez 😊


**Referencias:**

Documentación oficial de venv. https://docs.python.org/3/library/venv.html
