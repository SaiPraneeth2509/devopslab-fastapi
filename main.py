from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "DevOpsLab is running on Ubuntu VM!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
