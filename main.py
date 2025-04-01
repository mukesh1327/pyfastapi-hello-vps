from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

# Load the title from an environment variable (similar to application.properties)
APP_TITLE = os.getenv("APP_TITLE", "Value Point Systems Demo - Openshift CI CD")

@app.get("/hello")
async def hello_world():
    return {"message": "Hello, World!"}

@app.get("/vpsdemo/{image_name}", response_class=HTMLResponse)
async def get_image_html(image_name: str):
    image_url = f"/images/{image_name}"
    html_content = f"""
    <html>
        <head><title>Image Viewer</title></head>
        <body>
            <h1>{APP_TITLE}</h1>
            <h2>App modernization</h2>
            <img src='{image_url}' alt='Image' width='500'/>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
