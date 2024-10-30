from fastapi import APIRouter

from app.routers import auth, admin, users

api_router = APIRouter()

api_router.include_router(auth.router, tags=["Auth"], prefix="/auth")
api_router.include_router(admin.router, tags=["Admin"], prefix="/admin")
api_router.include_router(users.router, tags=["Users"], prefix="/user")
