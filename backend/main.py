from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI() #inicia fastAPI (sem isso o framework não funciona)

# Permite que o Front-end acesse o Back-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de dados que o Front-end vai enviar
class DadosImovel(BaseModel):
    area: float
    quartos: int
    banheiros: int

@app.post("/predict")
async def predict(dados: DadosImovel):
    # Cálculo temporário (enquanto a IA não chega)
    preco = (dados.area * 5000) + (dados.quartos * 20000)
    return {"preco_estimado": preco}