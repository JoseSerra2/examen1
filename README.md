José Antonio Serra Castillo -202208030

Iniciando el proyecto:
python -m venv venv

Activar el venv:
.\venv\Scripts\activate

Cambiar carpeta:

cd EXAMEN1

Instalar dependencias:
bash pip install -r requirements.txt

Crear app:
python manage.py startapp hr

Crear .env con los datos:
DB_NAME = examen
DB_USER = usuario
DB_PASSWORD= contraseña
DB_HOST = host
DB_PORT = puerto

Migrar base de datos:
bash python manage.py migrate

Iniciar el proyecto:
python manage.py runserver
