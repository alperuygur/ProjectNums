from fastapi import FastAPI
from routers.num_mod import check_type, decimal_op, is_float, num_mod_act

description = """
## Examples:
* ● input: 500 output 500
* ● input: 3400 outputs 3.5k
* ● input: 1000000 output: 1M
* ● input: 2500000.34 output: 2.5M
* ● input: 1123456789 output: 1.1B

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

@app.get('/')
def root():
    return {'Project Test'}


@app.get('/numbers/{num}', tags=['numbers'])
async def number(num: str):
    return {"Input": check_type(num),
            "Output": num_mod_act(num)
            }   # for testing(decimal_op), num_mod_act() remove later