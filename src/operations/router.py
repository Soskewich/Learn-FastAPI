import time

from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_async_session
from src.operations.models import operations
from src.operations.schemas import OperationCreate

router = APIRouter (
    prefix="/operations",
    tags=["Operation"]
)
#@cache(expire=30) - время хранения кэш в редис
@router.get("/long_operation")
@cache(expire=30)
def get_long_op():
    time.sleep(2)
    return "Много много данных, которые вычислялись сто лет"

@router.get("/")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(operations).where(operations.c.type == operation_type)
    result = await session.execute(query)
    return result.all()

@router.post("/")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operations).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}