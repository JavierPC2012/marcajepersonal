# marcajepersonal
aplicacion de ejemplo para marcaje de empleados

La aplicacion esta desarrollada en python utilizando como framework Django, para poder ejecutar el docker correctamente sigue estos pasos:

1. Ejecuta: docker-compose run app python3 manage.py collectstatic
2. Ejecuta: docker-compose run app python3 manage.py migrate
3. Ejecuta: docker-compose up

Accede a la aplicacion desde tu navegador con la URL: http://localhost:8000/
