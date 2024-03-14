from fastapi import APIRouter

from . import operations


router = APIRouter()
router.include_router(operations.router)
