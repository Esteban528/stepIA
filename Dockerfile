# Usa una imagen base con soporte para Python
FROM python:3.9

# Establece el directorio de trabajo en la raíz del contenedor
WORKDIR /app


COPY ./requirements.txt .

# Instala las dependencias necesarias
RUN pip install -r requirements.txt

# Comando para iniciar la aplicación
CMD [ "python", "app.py" ]
