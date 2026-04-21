# Tutorial 05 - Strangler Pattern con Nginx y Gunicorn

## Objetivo

Implementar arquitectura de produccion con Nginx (proxy inverso) + Gunicorn, aislando Django del exterior y preparando el Strangler Pattern.

## Cambios aplicados

- Se agrega `gunicorn` a `requirements.txt`.
- Se crea `nginx/nginx.conf` con proxy inverso hacia `web:8000`.
- `docker-compose.yml` actualizado a 3 servicios (`db`, `web`, `nginx`).
- `web` ya no expone puerto al host; solo Nginx publica `80`.

## Codigo

- Proyecto completo incluido en: `tutorial05_Strangler_Nginx\tutorial05_Strangler_Nginx`

## Verificacion en AWS

1. `docker-compose up -d --build`
2. `docker ps` con `nginx`, `web`, `db` en `Up`.
3. Navegador: `http://18.207.238.33/api/v1/comprar/` (sin puerto) funciona.
4. Navegador: `http://18.207.238.33:8000` falla (aislamiento correcto).

## Evidencias

- `captura1_tutorial05.png` (API por Nginx sin puerto)
- `captura2_tutorial05.png` (timeout en puerto 8000)
- `captura3_tutorial05.png` (docker ps con 3 contenedores)
