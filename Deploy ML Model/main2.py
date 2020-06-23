from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')

app = FastAPI()


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(name='index.html', context={
        'request': request
    })


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = 'Send some questions'):
    return {"item_id": item_id, "q": q}
