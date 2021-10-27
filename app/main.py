from fastapi import FastAPI

app = FastAPI()

def _fibonacci(n: int):
    ans = 0
    if n == 1 or n == 2:
        ans = 1
    else:
        ans = _fibonacci(n-1) + _fibonacci(n-2)
    return ans


@app.get("/fibonacci")
async def fibonacci(n: int = 1):
    return {"Answer": str(_fibonacci(n))}
