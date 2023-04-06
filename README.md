# Deploying a machine learning model (complex scikit-learn pipeline) using Streamlit as a frontend and FastAPI as a backend.
## In this case, both FastAPI and Streamlit are wrapped in one docker container. However, despite this, port 8000 for accessing FastAPI is open for use and can be subject to additional load from any other applications, not just from Streamlit. 
### Deploying FastAPI and Streamlit in different containers is represented by the code here - https://github.com/dimacv/deployment-ML-streamlit and https://github.com/dimacv/deployment-ML-fastapi . And here is a deployment with Flask and h2o - https://github.com/dimacv/deployment-ML-api_flask_h2o
  
## Building this docker:

``` docker build -t streamlit_fastapi . ```
  
--------------------------------------------------------------------------------

## Starting a named container in daemon mode on port 8000 and 8501 :

``` docker run --rm -p 8501:8501 -p 8000:8000 --name streamlit_fastapi -d streamlit_fastapi ``` 

