# PASOS A SEGUIR

## IMPORTANTE

Para empezar, en la carpeta inicial, hay que pillar el archivo docker-compose.yaml, copiarlo y pegarlo en la carpeta donde vas a crear el resto de carpetas para el resto de contenedores que vas a crear a posterior.

## PARA FLASK

- Para comenzar, hay que descargar los ficheros que tienen (flask), para, más tarde, descargar el de app.py y el de requirements.

  Luego, ponerlo todo en una carpeta separada con el comando `mkdir flask`

## PARA DEVELOPER

- Luego, con el de dev, hay que copiar el fichero Dockerfile y startup.sh

  También, como en el otro caso, crear una carpeta por separado con el comando `mkdir developer`

## PARA EJECUTAR

Una vez hecho todo, hay que ejecutar el siguiente comando:

```
docker-compose up -d --build
```

Una vez hecho, se nos crearan las 3 máquinas, postgres, developer, y flask.
