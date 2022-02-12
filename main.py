from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

#处理静态文件
app.mount("/static", StaticFiles(directory="static"), name="static")


#解决跨域问题
origins = [
    "http://localhost:25565",
    "https://localhost:25565"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"博客API"}
