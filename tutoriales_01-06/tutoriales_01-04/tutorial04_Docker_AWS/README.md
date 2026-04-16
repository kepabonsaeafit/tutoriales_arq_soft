# Tutorial 04 - Docker y AWS

## Objetivo
Dockerizar la app del tutorial 03 y dejarla lista para despliegue en AWS EC2.

## Cambios aplicados
- `settings.py` configurado para usar variables de entorno de PostgreSQL.
- `Dockerfile` y `docker-compose.yml` creados en la raiz del proyecto.
- `requirements.txt` ajustado para instalar Django 5.2.x + DRF sin errores en Python 3.11.
- `ALLOWED_HOSTS` actualizado para habilitar acceso por IP publica de EC2.

## Proyecto
- Codigo: `tutorial04_Docker_AWS\tutorial04_Docker_AWS`

## Verificacion ejecutada
1. Construccion y arranque en AWS con `docker-compose up -d --build`.
2. Contenedores activos verificados con `docker ps`:
- `tutorial04_docker_aws-web-1` (puerto `8000` publicado)
- `tutorial04_docker_aws-db-1` (PostgreSQL)
3. Endpoint validado en navegador:
- `http://18.207.238.33:8000/api/v1/comprar/`
- Respuesta observada: interfaz DRF de `Compra Api` (GET responde `405 Method Not Allowed`, esperado porque el endpoint opera por POST).

## Evidencia
- Captura: `captura_tutorial04.png`
- Ruta: `C:\Users\Kevin´s University\Desktop\SEM-2026-1\ARQ. SOFT\TUTORIALES\tutoriales_01-04\tutorial04_Docker_AWS\captura_tutorial04.png`
