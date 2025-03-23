from fastapi import FastAPI

app = FastAPI()

@app.get("/api/login")
def login():
    return {"message": "Login successful!"}

@app.get("/api/dashboard")
def dashboard():
    return {"message": "Welcome to the Dashboard!"}

@app.get("/api/map")
def map_view():
    return {"message": "Map data is being displayed!"}
