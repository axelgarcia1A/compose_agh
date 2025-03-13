# DOCKER COMPOSE

## PASOS A HACER:

1. Hacer: `mkdir flask` y `mkdir developer`
2. Copiar todos los archivos de la carpeta flask
3. Copiar todos los archivos de la carpeta developer
4. Ejecutar `docker-compose up -d --build`

## IMPORTANTE A RECALCAR

Es importante que el docker-compose.yaml esté en la carpeta previa a la de developer y flask, es decir, que quede asi:

```
main/
├── developer
│   ├── Dockerfile
│   └── startup.sh
├── docker-compose.yaml
└── flask
    ├── app.py
    ├── Dockerfile
    ├── gestio_participants.py
    ├── gestio_partides.py
    ├── participants.json
    ├── puntuacions.json
    ├── puntuacions.py
    ├── requirements.txt
    ├── start.sh
    ├── templates
    │   ├── index.html
    │   ├── participants.html
    │   ├── partides.html
    │   ├── puntuacions.html
    │   └── ranking.html
    └── utils.py
```

## SSH

### SSH a Flask:

- ssh -p 2222 root@localhost
    - password: `password`

### SSG a Developer:

- ssh -p 2223 developer@localhost
      - password: developer
