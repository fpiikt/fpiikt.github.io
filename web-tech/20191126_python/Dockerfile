# FROM Возьми базовый образ (image) с таким названием

FROM python:alpine

# WORKDIR объявляет каталог внутри образа, где будет развернуто приложение 
WORKDIR /usr/src/app

# Скопируем файл requirements.txt внутрь WORKDIR
COPY requirements.txt ./

# Установка зависимостей для проекта, указанных в requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Скопируем файл(ы) из текущего каталога на компьютере (где запускается этот Dockerfile) в каталог внутри образа, который мы установили как текущий WORKDIR
COPY . .


ENTRYPOINT [ "python" ]

CMD [ "app.py" ]

# CMD [ "python", "app.py" ]

# python app.py



# Для сборки образа в папке 20191126_python
# запустите: 
# docker build -t flask-app-demo:latest .

# Для запуска контейнера: 

# docker run -d -p -rm 4321:4321 flask-app-demo