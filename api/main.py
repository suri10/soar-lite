from dotenv import load_dotenv
import os

load_dotenv()  # ✅ Load environment variables from .env

# Print all environment variables to debug
print("Environment Variables:", os.environ)



from fastapi import FastAPI
from api.routes import logs

app = FastAPI(title="SOAR Lite - AI-Powered Security Automation")

# Include the log route
app.include_router(logs.router, prefix="/logs")

@app.get("/")
def read_root():
    return {"message": "SOAR Lite API is running"}
