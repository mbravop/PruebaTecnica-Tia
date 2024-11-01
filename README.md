# PruebaTecnica-Tia

Repositorio para Prueba Técnica V5. Realizado por Mauricio Bravo.

Este proyecto consiste en un sistema de gestión de reservas de vuelos, permite el registro e inicio de sesión de usuarios, crear/cancelar reservas de vuelos y filtrar vuelos reservados por el usuario.

Se utilizó Django y MySQL. La aplicación corre en servidor local.

## Requisitos previos

### Instalación dependencias

Para la instalación de las dependencias utilizadas:

- asgiref == 3.8.1
- Django == 5.1.2
- djangorestframework == 3.15.2
- djangorestframework-simplejwt == 5.3.1
- PyJWT == 2.9.0
- PyMySQL == 1.1.1
- sqlparse == 0.5.1

Para evitar conflictos con dependencias, se recomienda crear un nuevo entorno virtual:

```bash
python -m venv <nombre_venv>
```

Activar entorno:

- Windows: `<nombre_venv>\Scripts\activate`
- MacOS/Linux: `source <nombre_venv>/bin/activate`

Ejecutar el comando para la instalación

```bash
pip install -r requirements.txt
```

Acceder a carpeta de backEnd:

```bash
cd sistemaVuelos_backend
```

### Configuración base de datos MySQL

1. **Crear base de datos**:

- Abrir cliente MySQL:
- Ejecutar comando:

```sql
CREATE DATABASE <nombreBDD>;
```

2. **Configurar settings.py**:

   En el archivo sistemaVuelos_backend/sistemaVuelos_backend/settings.py modificar los campos según tu configuración:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<nombreBDD>',
        'USER':'<usuarioSQL>',
        'PASSWORD':'<contraseña>',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
```

### Realizar migraciones

Para crear las tablas necesarias en el sistema, ejecutar el siguiente comando:

```bash
python manage.py migrate
```

### Cargar datos de vuelos iniciales

Para la base de datos de vuelos se ha utilizado el siguiente dataset: https://www.kaggle.com/datasets/mahoora00135/flights?resource=download, los datos se encuentran en datos/flights.csv

Ejecutar el siguiente comando para automatizar la carga de datos:

```bash
python manage.py importarVuelos datos/flights.csv
```

## Levantar servidor

De manera predeterminada el servidor se alojará en el puerto 8000.

```bash
python manage.py runserver
```

## Instrucciones de uso

La documentación de la API se encuentra en <a href="https://documenter.getpostman.com/view/27610987/2sAY4xA1nD">Postman</a>.
