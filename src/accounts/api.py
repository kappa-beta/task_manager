from typing import List

from fastapi import FastAPI
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from .schemas import Account as AccountSchema
from .schemas import AccountCreate
from .services import AccountService
from src.auth.dependencies import get_current_account
from src.auth.schemas import AuthAccount
from src.exceptions import EntityConflictError
from src.exceptions import EntityDoesNotExistError

router = APIRouter(
    prefix='/accounts',
)


def init_accounts(app: FastAPI):
    app.include_router(router)


@router.post(
    '',
    response_model=AccountSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_account(
        account_create: AccountCreate,
        service: AccountService = Depends(),
):
    try:
        account = service.create_account(account_create)
        return account
    except EntityConflictError:
        raise HTTPException(status.HTTP_409_CONFLICT) from None


@router.get('', response_model=List[AccountSchema])
def get_accounts(
        current_account: AuthAccount = Depends(get_current_account),
        service: AccountService = Depends(),
):
    return service.get_accounts()


@router.get('/{account_id}', response_model=AccountSchema)
def get_account(
        account_id: int,
        current_account: AuthAccount = Depends(get_current_account),
        service: AccountService = Depends(),
):
    try:
        return service.get_account(account_id)
    except EntityDoesNotExistError:
        raise HTTPException(status.HTTP_404_NOT_FOUND) from None
