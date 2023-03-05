# Deploying a machine learning model (complex pipeline) using Streamlit as a frontend and FastAPI as a backend.
## In this case, both FastAPI and Streamlit are wrapped in one docker container. However, despite this, the port 8000 for accessing FastAPI is open for use and additional load can be created on it from any other applications besides Streamlit.
  
### Сборка докера:
docker build -t streamlit_fastapi .  
  
### Запуск контейнера: 
docker run -p 8501:8501 -p 8000:8000 --name streamlit_fastapi streamlit_fastapi 

