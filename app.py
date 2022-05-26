from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

# task 3.1


@app.get("/start", response_class=HTMLResponse)
def root():
    html_content = "<h1>The unix epoch started at 1970-01-01</h1>"
    
    return HTMLResponse(content=html_content, status_code=200)
