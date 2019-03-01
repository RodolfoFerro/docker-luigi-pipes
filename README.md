![header](assets/docker-luigi.png)

Repositorio de la charla **"Crea un pipeline con Docker y Luigi"**, el cual ilustra la creación de un flujo de tareas que se ejecutan para la ejecución de un OCR que crea archivos de texto en un contenedor virtual de Docker.

## 🐳 Instalación

Deberás tener [Docker](https://www.docker.com/) instalado en tu máquina.

Para crear la imagen, sólo ejecuta lo siguiente:
```bash
$ docker build --no-cache -t pipe:latest .
```

Esto instalará los requerimientos necesarios con Anaconda. Una vez instalados, puedes acceder a terminal del contenedor mediante:
```bash
$ docker run -it pipe
```

Esto te permitirá correr las pruebas y ejecutar los scripts.


## 👾 Contenido

Para correr el archivo de prueba, desde la terminal de docker ejecuta lo siguiente:
```bash
$ python dev/utils.py -p morph -i "assets/test.png" > "assets/out.txt"
```

Para correr las tareas de prueba, basta ejecutar desde la terminal de Docker:
```bash
$ cd dev
$ python basic_pipeline.py --local-scheduler ApplyOCR
```

***

### SOBRE EL USO DE INFORMACIÓN TOTAL O PARCIAL: 🔐
* Estos documentos fueron originalmente creados por el autor.
* Cualquier uso de estos documentos o sus contenidos están permitidos a través de la licencia provista y sus condiciones.
* Para cualquier aclaración, puedes contactar al autor: https://rodolfoferro.xyz/

**Copyright (c) 2019 Rodolfo Ferro**
