from fastapi import FastAPI, Request, Form
from routers.num_mod import check_type, num_mod_act
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

description = """
## Examples:
* ● input: 500 output 500
* ● input: 3400 outputs 3.4K
* ● input: 1000000 output: 1M
* ● input: 2500000.34 output: 2.5M
* ● input: 1123456789 output: 1.1B
* ● input: -2545.266555555 output: -2.5K<br>
* ● input: -15000 output: -15K<br>

"""
tags_metadata = [
    {
        "name": "numbers",
        "description": "Coverts input numbers to examples output",
    }
]
app: FastAPI = FastAPI(
    openapi_tags=tags_metadata,
    title="Task",
    description=description,
    version="0.0.1",
    contact={
        "name": "Alper Uygur",
        "url": "https://github.com/alperuygur/ProjectNums",
        "email": "alper.uyg@gmail.com",
    },

)

templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})


@app.get('/numbers/', tags=['numbers'], response_class=HTMLResponse)
async def get_number(request: Request):
    return templates.TemplateResponse('numbers.html', {'request': request})

@app.post('/numbers/', tags=['numbers'], response_class=HTMLResponse)
async def post_number(request: Request, num: str = Form()):
    return templates.TemplateResponse('numbers.html', {'request': request, "Input": check_type(num), "Output": num_mod_act(num), 'num': num})