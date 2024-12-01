from fastapi import FastAPI

app = FastAPI(
    deprecated='First site'
)


@app.get('/')
def index():
    return {'status': 200}
