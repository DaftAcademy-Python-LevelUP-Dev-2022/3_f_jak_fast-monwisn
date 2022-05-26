from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/start", response_class=HTMLResponse)
async def root():
    html_content = """
    <html>
        <body>
            <h1>The unix epoch started at 1970-01-01</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
