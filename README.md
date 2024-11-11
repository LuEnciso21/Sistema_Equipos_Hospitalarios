# Sistema Equipos Hospitalarios

Este software permite gestionar y monitorear el inventario de equipos médicos en un entorno hospitalario, integrando funcionalidades específicas para facilitar la administración y consulta de equipos y responsables asignados.

Características principales:

1. Registro de Equipos:
Permite el ingreso de equipos hospitalarios de distintas áreas como radiología, cardiología, emergencias, entre otros. Cada equipo incluye detalles clave como el tipo, modelo, número de serie, fabricante y fecha de adquisición.

2. Asignación de Responsables:
El sistema permite asociar un responsable a cada equipo, como el técnico de mantenimiento o el jefe de área, incluyendo información relevante como nombre, cargo, y datos de contacto.

3. Consulta de Equipos por Área:
Los usuarios pueden realizar búsquedas filtradas de los equipos por área específica, facilitando la localización y monitoreo de equipos en función de su ubicación o especialización.

4. Consulta de Responsables:
Los usuarios pueden consultar la lista completa de responsables asignados a los equipos, lo cual facilita la identificación rápida de la persona encargada en caso de requerir mantenimiento, reparación o inspección.

# 1. Clonar el repositorio:

`git clone https://github.com/tu-usuario/nombre-del-repo.git`

`cd nombre-del-repo`

# 2. Crear un entorno virtual (opcional pero recomendado):

`python -m venv venv`

`source venv/bin/activate`  

Para activar el ambiente virtual en Windows, se usa 

`venv\Scripts\activate`

# 3. Instalar las dependencias:

`pip install -r requirements.txt`

# 4. Configurar la base de datos:

Asegurese de tener una base de datos MySQL configurada y actualiza las configuraciones en `settings.py`:

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'nombre_base_datos',
                'USER': 'tu_usuario',
                'PASSWORD': 'tu_contraseña',
                'HOST': 'localhost',
                'PORT': '3306',
            }
        }

# 5. Realizar las migraciones:

`python manage.py migrate`


# 6. Ejecuta el servidor de desarrollo:

`python manage.py runserver`

# Integrantes

Luisa Enciso - Santiago Rivera - Mateo Quintero
