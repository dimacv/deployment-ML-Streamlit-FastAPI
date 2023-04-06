# Deploying a machine learning model (complex scikit-learn pipeline) using Streamlit as a frontend and FastAPI as a backend.
## In this case, both FastAPI and Streamlit are wrapped in one docker container. However, despite this, the port 8000 for accessing FastAPI is open for use and additional load can be created on it from any other applications besides Streamlit.
  
## Docker build:

``` docker build -t streamlit_fastapi . ```
  
--------------------------------------------------------------------------------

## Starting a named container in daemon mode on port 8000 and 8501 :

``` docker run --rm -p 8501:8501 -p 8000:8000 --name streamlit_fastapi -d streamlit_fastapi ``` 

