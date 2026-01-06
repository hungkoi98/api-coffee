from fastapi import FastAPI

from app.routers import customers, procurement, conversion_rate

app = FastAPI()
app.include_router(customers.router, tags=["customers"])
app.include_router(procurement.router, tags=["procurement"])
app.include_router(conversion_rate.router, tags=["conversion"])

@app.get("/")
async def root():
    return {"message": "Hello World"}