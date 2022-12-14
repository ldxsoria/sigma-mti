# SIGMA MIT

# INTRODUCCIÓN
Sigma MIT (Módulo de tecnologías de la información)
Es una aplicación desarrollada en Django, que utiliza las siguientes tecnologías:
* Docker y Docker-compose
* Git
* Python ,gunicorn y el framework Django
* Nginx
* Postgresql

Cuya única finalidad es ayudar a los departamentos de TI a dejar de usar excel o muchos programas para registrar sus tickets, inventario, topología de red y configuraciones, etc. Y tener todo en un solo lugar.

# 1) CONFIGURACIONES INICIALES

## Primero clonamos el projecto
```bash
git clone https://github.com/ldxsoria/sigma-mti.git
```

## Creamos los contenedores y los inicializamos
```bash
cd sigma-mti
docker-compose up -d
```
## Creamos el archivo con las variables de entorno
Es importante editar .env con los datos del correo que usaremos para enviar los notificaciones, en caso sea uno de google, recuerden activar el uso de aplicaciones de terceros.
LA APLICACION NO INICIARA SI NO EXITE EL .env
```bash
docker-compose exec django_app cp docker_django/.env.editme docker_django/.env
docker-compose exec django_app vim docker_django/.env
```

## Iniciamos la aplicación
```bash
docker-compose restart django_app
```

## Configuramos django
```bash
docker-compose exec django_app python docker_django/manage.py makemigrations
docker-compose exec django_app python docker_django/manage.py migrate
docker-compose exec django_app python docker_django/manage.py collectstatic
```
# Configuramos el superusuario de django
```bash
docker-compose exec django_app python docker_django/manage.py createsuperuser
```

# Una vez echo todo lo anterior, realizamos lo siguiente:
1) Ingresamos al {{dominio}}/admin con la cuenta de superusuario
2) Ingresamos a {{dominio}}/ y importamos lo siguiente desde un .csv:
* Estados de los tickets de atención => (int:estado, str:desc)
* Usuarios => (username,first_name,last_name,email,password)
* Areas =>  (str:cod_area, str: descr   pition, str:siglas)

# 2) HABILITAR/CONFIGURAR COMPLEMENTOS ADICIONALES
## Iniciar CRONJOBS
Por defecto los cronjobs estan desactivados y para activalos tienes que:
1) Ingresar a settings.py y cambiar en CRONJOBS '.stop' a '.start'
2) Reiniciar el servicio de cron con el siguiente comando
```bash
docker-compose exec django_app service cron restart
```

## CRONs actualmente configurados
* alert_five_days => Éste cron permite enviar una notificación cuando 1 o más tickets tengan más de 5 días sin ser marcados y completados.
Es necesario ingresar a myapp/crontab/alert_five_days y agregar los correos que recibirán la notificación.

