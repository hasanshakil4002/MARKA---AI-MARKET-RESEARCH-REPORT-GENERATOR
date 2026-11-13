from datetime import datetime

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from markdown_it import MarkdownIt

from crew import MarketResearchAi

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
md = MarkdownIt("js-default")  # raw HTML disabled, so AI output can't inject markup


def generate_report(product: str, region: str, country: str) -> str:
    result = MarketResearchAi().crew().kickoff(inputs={
        "product": product,
        "region": region,
        "country": country,
        "current_year": str(datetime.now().year),
    })
    return result.raw


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {})


@app.post("/", response_class=HTMLResponse)
def report(
    request: Request,
    product: str = Form(..., max_length=100),
    region: str = Form(..., max_length=100),
    country: str = Form(..., max_length=100),
):
    product, region, country = product.strip(), region.strip(), country.strip()
    try:
        markdown_text, error = generate_report(product, region, country), None
    except Exception:
        markdown_text, error = "", "Could not generate the report. Please try again."

    return templates.TemplateResponse(request, "index.html", {
        "product": product,
        "region": region,
        "country": country,
        "error": error,
        "markdown_text": markdown_text,
        "report_html": md.render(markdown_text) if markdown_text else "",
    })


@app.post("/download")
def download(markdown_text: str = Form(...)):
    return Response(
        markdown_text,
        media_type="text/markdown; charset=utf-8",
        headers={"Content-Disposition": 'attachment; filename="report.md"'},
    )