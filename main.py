from datetime import datetime

from fastapi import FastAPI, Form, Request, logger
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from markdown_it import MarkdownIt

#from crew import MarketResearchAi #true position

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
#md = MarkdownIt("js-default") #true position
md = MarkdownIt("default") # in rending time, we will use the default renderer instead of the js-default renderer, because the js-default renderer is not safe for untrusted input. The default renderer is safe for untrusted input, but it does not support some features like tables and footnotes.
  # raw HTML disabled, so AI output can't inject markup


def generate_report(product: str, region: str, country: str) -> str:
    from crew import MarketResearchAi #in rending time, we will import the MarketResearchAi class from the crew module, because the crew module is not available at the top level of the application, and we want to avoid circular imports.
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
        logger.exception("Report generation failed")
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