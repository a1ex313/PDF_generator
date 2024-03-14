from datetime import date
from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class BaseOperation(BaseModel):
    db_name: str
    user_name: str
    passw: str
    host: str
    table_name: str
    file_name: str
    orientation: str


class OperationCreateTable(BaseOperation):
    pass

class OperationCreateVerticalBar(BaseOperation):
    pass

class OperationCreateHorizontalBar(BaseOperation):
    pass


class Operation(BaseOperation):

    class Config:
        from_attributes = True
