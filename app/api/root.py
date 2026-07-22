# =============================================================================
# Import Required Libraries
# =============================================================================
from fastapi import APIRouter 


# =============================================================================
# Create Root Router
# =============================================================================
router = APIRouter() 


# =============================================================================
# Root Endpoint
# Returns basic information about the API.
# =============================================================================
@router.get('/')
def root():
    """
    Return basic information about the API.
    """
    return {
        "message": "Welcome to the Bangladeshi Taka Note Detection API",
        "status": "running",
        "version": "1.0.0"
    }