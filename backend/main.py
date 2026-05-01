# backend/main.py
"""
起動：
nohup uvicorn backend.main:app --reload --port 8000 > uvicorn.log 2>&1 &

FqstAPI:
htp://localhost:8000/data

停止：
kill $(lsof -t -i:8000)
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 許可（フロントが 8880 なので必要）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/data")
def get_data():
    # X-Y プロット用のダミーデータ
    return {
        "x": [1, 2, 3, 4, 5],
        "y": [10, 20, 15, 30, 25]
    }
