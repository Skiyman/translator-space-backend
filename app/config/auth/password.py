from pydantic import BaseModel


class ResetPassword(BaseModel):
    current_password: str


class ChangePassword(ResetPassword):
    new_password: str
