#!/bin/bash
# запустим FastAPI
uvicorn app:app --host 0.0.0.0 --port 8000 &
# запустим Streamlit
streamlit run streamlit.py --server.port=8501 --server.address=0.0.0.0
