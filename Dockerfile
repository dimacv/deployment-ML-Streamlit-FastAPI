# Зададим имидж на основании которого мы делаем свой имидж
FROM python:3.9

# назначим рабочую папку
WORKDIR /app

# скопируем необходимые для работы файлы
COPY . .

# установим нужные пакеты python
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# запустим uvicorn и Streamlit
CMD /app/run.sh

