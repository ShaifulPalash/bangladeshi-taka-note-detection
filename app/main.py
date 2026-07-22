# =============================================================================
# Import Required Libraries
# =============================================================================
from fastapi import FastAPI 
 
# =============================================================================
# Initialize FastAPI Application
# Configure application metadata for the automatically generated API
# documentation (Swagger UI and ReDoc).
# =============================================================================
app = FastAPI(
    title='Bangladeshi Taka Note Detection API',
    description='A FastAPI application that uses a YOLO model to detect Bangladeshi Taka notes from uploaded images.',
    version='1.0.0'
)

# =============================================================================
# Root Endpoint
# Returns basic information about the API.
# =============================================================================
@app.get('/')
def root():
    """
    Root endpoint to verify that the API is running.
    """
    return {
        "message": "Welcome to the Bangladeshi Taka Note Detection API",
        "status": "running",
        "version": "1.0.0"
    }