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
        <h1></h1>
        </center>
        <hr>
        <p>
        <h3></h3>
        基本的なタグをいくつか知っているだけでも最低限の<B>簡単なHTML文書</B>が作れます。
         これにリンクというものをつければ立派なホームページを作ることができます。<BR>
        <h4>さらに応用タグを使うといろいろなことができます。</h4>
        <hr align=center size=10 width=420 color="#20ff00">
        <center><marquee width=300 bgcolor="#ffffff">
        Welcome to My Page
        </marquee></center>
        </body>
</html> 
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/present")
async def give_present(present):
    return {"response": f"サーバです。メリークリスマス！ {present}ありがとう。お返しはキャンディーです。"}  # f文字列というPythonの機能を使っている