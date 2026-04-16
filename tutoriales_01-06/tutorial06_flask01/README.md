# Tutorial 06 - Flask 101 (Strangler Pattern)

Este proyecto implementa el estrangulamiento del flujo de compras:

- `GET /api/v1/productos/` se atiende desde Django (`web_django`).
- `POST /api/v2/comprar` se atiende desde Flask (`pagos_flask`).
- Nginx enruta por versión de API.

## Estructura clave

- `docker-compose.yml`: Orquesta `db`, `web_django`, `pagos_flask`, `nginx`.
- `nginx/nginx.conf`: Reglas de ruteo v1/v2.
- `microservicio_pagos/app.py`: Endpoint Flask v2.
- `tienda_app/api/views.py`: Endpoint Django v1 de productos.

## Levantar en local / EC2

```bash
docker compose up -d --build
```

## Pruebas requeridas

### 1) Coexistencia (v1 en Django)

```bash
curl http://<IP-AWS>/api/v1/productos/
```

Debe responder un JSON de productos desde Django.

### 2) Estrangulamiento (v2 en Flask)

```bash
curl -X POST http://<IP-AWS>/api/v2/comprar \
  -H "Content-Type: application/json" \
  -d '{"producto_id": 1, "cantidad": 2}'
```

Debe responder con el mensaje:

`Compra procesada exitosamente por el Microservicio Flask (v2)`

### 3) Logs de orquestación

```bash
docker compose logs nginx
```

## Dependencias

`requirements.txt` del servicio Django fue limpiado a dependencias mínimas para despliegue estable en Docker.
El microservicio Flask instala `flask` y `gunicorn` en su propio Dockerfile.
