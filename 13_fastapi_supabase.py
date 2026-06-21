from fastapi import FastAPI
from supabase import create_client

supabase = create_client("https://rxyritjaildpdhtdjdcp.supabase.co", "")

app = FastAPI()

@app.get("/clientes")
def get_clientes():
    return supabase.table("clientes").select("*").execute()

@app.get("/clientes/{id}")
def get_cliente_by_id(id: int):
    return supabase.table("clientes").select("*").eq("id", id).execute()

@app.get("/contratos")
def listar_contratos():
    return supabase.table("contratos").select("*").execute()