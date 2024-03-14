from typing import (
    List,
    Optional,
)

from fastapi import (
    APIRouter,
    Depends,
    Response,
    status,
)

from .. models.operations import (
    Operation,
    OperationCreateTable,
    OperationCreateVerticalBar,
    OperationCreateHorizontalBar,
)
from ..services.operations import OperationsService


router = APIRouter(
    prefix='/operations',
)


@router.post('/create_table', response_model=Operation)
def create_Table(
    operation_data1: OperationCreateTable,
    service: OperationsService = Depends(),
):
    return service.create_Table(operation_data1)

@router.post('/create_vertical_bar_chart', response_model=Operation)
def create_VerticalBarChart(
    operation_data2: OperationCreateVerticalBar,
    service: OperationsService = Depends(),
):
    return service.create_VerticalBarChart(operation_data2)

@router.post('/create_horizontal_bar_chart', response_model=Operation)
def create_HorizontalBarChart(
    operation_data3: OperationCreateHorizontalBar,
    service: OperationsService = Depends(),
):
    return service.create_HorizontalBarChart(operation_data3)


