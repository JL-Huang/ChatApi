from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def hello_rag():
    return {"message": "Hello RAG!"}
