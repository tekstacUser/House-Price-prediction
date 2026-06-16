#!/bin/bash
uvicorn app:app --host 0.0.0.0 --port 8000 &
streamlit run streamit_app.py --server.address 0.0.0.0 --server.port 8501
