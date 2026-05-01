# backend/main.py
"""
起動：
uvicorn backend.main:app --reload --port 8000 &
FqstAPI:
 htp://localhost:8000/data
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
