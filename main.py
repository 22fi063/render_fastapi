from typing import Optional

from fastapi import FastAPI

from fastapi.responses import HTMLResponse #インポート

import random  # randomライブラリを追加

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return omikuji_list[random.randrange(10)]

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>kadai9-A</title>
        </head>
        <body bgcolor="#0060ff">
        <center>
        <h1>自己紹介</h1>
        </center>
        <hr>
        <p>
        <div>
            <h2>基本情報</h2>
            <p>年齢: 20歳</p>
            <p>職業: 学生</p>
            <p>所在地: 東京都</p>
        </div>
        <div>
            <h2>興味・趣味</h2>
            <p>ゲーム　YouTube　アニメ　漫画</p>
        </div>
        <hr align=center size=10 width=420 color="#20ff00">
        <center><marquee width=300 bgcolor="#ffffff">
        Welcome to My Page
        </marquee></center>
        </body>
</html> 
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/present")
async def give_present(present: Present):
    if present.content == "キャンディー":
        response = f"サーバです。トリックオアトリート！ {present.content}ありがとう！"
    else:
        response = "サーバです。トリックオアトリート！ お菓子じゃなかったのでいたずらします！"
    return {"response": response}