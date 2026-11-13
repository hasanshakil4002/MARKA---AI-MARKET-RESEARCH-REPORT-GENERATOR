from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from markdown_it import MarkdownIt

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# HTML inside the report is disabled, so AI output can't inject markup.
md = MarkdownIt("js-default")


def generate_report(product: str, region: str, country: str) -> str:
    """Connect your AI market research assistant here.
    It must return the report as a Markdown string."""
    return (
        f"# Market Research: {product}\n\n"
        f"**Region:** {region}  \n**Country:** {country}\n\n"
        "## Summary\n"
        "Sample report. Replace `generate_report()` in `main.py` "
        "with your AI assistant.\n\n"
        "## Market demand\n- Demand trend\n- Target customers\n\n"
        "## Competitors\n"
        "| Brand | Price | Strength |\n|---|---|---|\n"
        "| Brand A | $10 | Distribution |\n"
        "| Brand B | $8 | Low price |\n\n"
        f"## Recommendation\nStart with a small pilot launch in {country}.\n"
    )


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
        markdown_text = generate_report(product, region, country)
        error = None
    except Exception:
        markdown_text, error = "", "Could not generate the report. Please try again."

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "product": product,
            "region": region,
            "country": country,
            "error": error,
            "markdown_text": markdown_text,
            "report_html": md.render(markdown_text) if markdown_text else "",
        },
    )


@app.post("/download")
def download(markdown_text: str = Form(...)):
    return Response(
        content=markdown_text,
        media_type="text/markdown; charset=utf-8",
        headers={"Content-Disposition": 'attachment; filename="report.md"'},
    )
