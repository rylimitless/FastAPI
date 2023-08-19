from fastapi import FastAPI

app = FastAPI()
count = 0

@app.get("/")
async def root():
    global count
    count +=1
    return {"count":f"{count}"}

@app.get("/count")
async def c():
    global count
    return {"count value" : f"{count}"}
