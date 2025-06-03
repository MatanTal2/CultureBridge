# src/api/v1/api.py
from fastapi import APIRouter

# Import endpoint routers here when they are created
# from .endpoints import users, bridges, webhooks, cultural_profiles, auth

api_router = APIRouter()

# Include routers from endpoint modules
# api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
# api_router.include_router(users.router, prefix="/users", tags=["Users"])
# api_router.include_router(bridges.router, prefix="/bridges", tags=["Bridges"])
# api_router.include_router(cultural_profiles.router, prefix="/cultural-profiles", tags=["Cultural Profiles"])
# api_router.include_router(webhooks.router, prefix="/webhooks", tags=["Webhooks"])

# Placeholder route until other routers are added
@api_router.get("/v1-status")
async def v1_status():
    return {"status": "API v1 is active"}