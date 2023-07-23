# Usa la imagen base de Python
FROM python:3


# Instala las dependencias (colorama,pillow,behave)
RUN pip install colorama
RUN pip install pillow
RUN pip install behave

# Copia el código fuente al contenedor
COPY main.py /app/main.py
# Establece el directorio de trabajo
WORKDIR /app

# Ejecuta la aplicación
CMD ["python", "main.py"]