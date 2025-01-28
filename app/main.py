from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from routes.router import router as email_router

app = FastAPI()

# Configure Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Register routes
app.include_router(email_router, prefix="/api", tags=["Email"])

# Root endpoint to serve the HTML template
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Render the index.html template when accessing the root endpoint.
    """
    return templates.TemplateResponse("index.html", {"request": request})
