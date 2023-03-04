# Зададим имидж на основании которого мы делаем свой имидж
FROM python:3.9

# назначим рабочую папку
WORKDIR /app

# скопируем необходимые для работы файлы
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY streamlit.py streamlit.py
COPY cloudpickle_for_deployment.pkl cloudpickle_for_deployment.pkl
COPY run.sh run.sh

# установим нужные пакеты python
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# запустим uvicorn и Streamlit
CMD /app/run.sh

