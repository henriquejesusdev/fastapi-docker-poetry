from fastapi import FastAPI

app = FastAPI(title="Aplicação FastAPI de Exemplo")

@app.get("/")
async def read_root():
    return {"message": "Bem-vindo à aplicação FastAPI!"}

@app.get("/health")
async def health_check():
    return {"status": "saudável"}
