# deployment ML -> Streamlit + FastAPI
  
### Сборка докера:
docker build -t streamlit_fastapi .  
  
### Запуск контейнера: 
docker run -p 8501:8501 -p 8000:8000 --name streamlit_fastapi streamlit_fastapi 

