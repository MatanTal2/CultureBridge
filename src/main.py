from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging

from src.core.config import settings
from src.api.v1.api import api_router_v1
# from src.services.database import engine, Base # We'll uncomment this later

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Placeholder for lifespan manager (e.g., for DB connections, Redis)
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application startup...")
    # Initialize database (e.g., create tables if they don't exist)
    # Base.metadata.create_all(bind=engine) # Uncomment when DB is set up
    
    # Initialize Redis connection pool if needed
    # app.state.redis = await redis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB}", encoding="utf8", decode_responses=True)
    logger.info("Connecting to Redis...")
    # Simulate Redis connection or setup
    
    yield
    
    logger.info("Application shutdown...")
    # if hasattr(app.state, 'redis') and app.state.redis:
    #     await app.state.redis.close()
    #     logger.info("Redis connection closed.")

app = FastAPI(
    title="CultureBridge API",
    description="API for seamless messaging across cultural and digital divides.",
    version="0.1.0",
    lifespan=lifespan # Enable lifespan manager
)

@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return {"status": "ok", "message": "CultureBridge API is healthy!"}

# Include API routers
app.include_router(api_router_v1, prefix="/api/v1")

# Example: How to access settings
logger.info(f"App running on {settings.APP_HOST}:{settings.APP_PORT}")
if settings.DATABASE_URL:
    logger.info(f"Database URL configured: {settings.DATABASE_URL[:20]}...") # Log only part for security


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=settings.RELOAD_APP
    )