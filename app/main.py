from os import getenv
from fastapi import FastAPI

app = FastAPI()


def square(n: int):
    return n * n


def fibonacci(n: int):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


version = getenv("SERIES_VERSION", "")
if version == "square":
    _series = square
elif version == "fibonacci":
    _series = fibonacci
elif version == "":
    raise ValueError("SERIES_VERSION not set.")
else:
    raise ValueError(f"Invalid SERIES_VERSION: {version}")


@app.get("/series")
async def series(n: int = 1):
    return {version: str(_series(n))}
