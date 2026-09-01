from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
  return {"message": "Gretel Synthetics Service is running!"}
