from fastapi import FastAPI
from routers.num_mod import check_type, decimal_op, is_float, num_mod_act

app = FastAPI()


@app.get('/')
def root():
    return {'Project Test'}


@app.get('/numbers/{num}')
async def number(num: str):
    return {"num": check_type(num),
            "Decimal": decimal_op(is_float(num)),
            "Output": num_mod_act(num)
            }   # for testing(decimal_op), num_mod_act() remove later