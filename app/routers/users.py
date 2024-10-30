from typing import Annotated

from fastapi import APIRouter, Depends

from app.config.auth.current_user import get_current_user
from app.config.auth.password import ChangePassword
from app.schemas.common.base_response import BaseResponse
from app.schemas.user import UserRole
from app.services.user_service import UserService

router = APIRouter()


@router.post(path="/change-password")
async def change_password(
        passwords: ChangePassword,
        current_user: Annotated[UserRole, Depends(get_current_user)],
        user_service: UserService.register_deps(),
) -> BaseResponse:
    return await user_service.change_password(
        current_password=passwords.current_password,
        new_password=passwords.new_password,
        user_sid=current_user.sid
    )


@router.get("/me/")
async def get_me(
        current_user: Annotated[UserRole, Depends(get_current_user)],
) -> UserRole:
    return current_user
