from fastapi import FastAPI
import os
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







if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port)