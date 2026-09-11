from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 📝 These are the values your browser agent will target and scrape
exam_data = {
    "exam_name": "Politican Ke Exam",
    "reg_date": "September 15, 2026",
    "exam_date": "October 10, 2026",
    "deadline": "October 05, 2026"
}

@app.get("/", response_class=HTMLResponse)
async def read_dashboard(request: Request):
    return templates.TemplateResponse(
        request,
        "webpage.html", 
        {"data": exam_data}
    )