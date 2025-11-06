from fastapi import FastAPI
from .routes import deals, analytics
from .database import Base, engine

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Salema & Salema IB Deal Tracker (Backend)")

app.include_router(deals.router)
app.include_router(analytics.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Salema & Salema IB Deal Tracker backend!"}
