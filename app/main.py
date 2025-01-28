from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.routes.router import router as email_router

app = FastAPI()

# Configure Jinja2 templates
templates = Jinja2Templates(directory="app/templates")

# Register routes
app.include_router(email_router, prefix="/api", tags=["Email"])

# Root endpoint to serve the HTML template
@app.get("/home", response_class=HTMLResponse)
async def render_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
