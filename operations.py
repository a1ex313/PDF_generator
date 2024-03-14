from typing import (
    List,
    Optional,
)

from fastapi import (
    Depends,
    status,
    HTTPException,
)

from .. import pdfgen
from pdfgen import merge_two_pdf
from ..models.operations import (
    OperationCreateTable,
    OperationCreateVerticalBar,
    OperationCreateHorizontalBar,
)

import os.path

class OperationsService:
    def create_Table(self, operation_data: OperationCreateTable):
        filename = operation_data.file_name
        orientation = operation_data.orientation

        db_name = operation_data.db_name
        user_name = operation_data.user_name
        passw = operation_data.passw
        host = operation_data.host
        table_name = operation_data.table_name
        if not os.path.exists(filename):
            file = pdfgen.CreatingPDF(filename)
            file.createLayout(orientation)
            file.createTable(db_name, user_name, passw, host, table_name)
        else:
            buf = pdfgen.CreatingPDF("buf.pdf")
            buf.createLayout(orientation)
            buf.createTable(db_name, user_name, passw, host, table_name)
            merge_two_pdf(filename, "buf.pdf", orientation)


    def create_VerticalBarChart(self, operation_data: OperationCreateVerticalBar):
        filename = operation_data.file_name
        orientation = operation_data.orientation
        db_name = operation_data.db_name
        user_name = operation_data.user_name
        passw = operation_data.passw
        host = operation_data.host
        table_name = operation_data.table_name
        if not os.path.exists(filename):
            file = pdfgen.CreatingPDF(filename)
            file.createLayout(orientation)
            file.createVerticalBarChart(db_name, user_name, passw, host, table_name)
        else:
            buf = pdfgen.CreatingPDF("buf.pdf")
            buf.createLayout(orientation)
            buf.createVerticalBarChart(db_name, user_name, passw, host, table_name)
            merge_two_pdf(filename, "buf.pdf", orientation)


    def create_HorizontalBarChart(self, operation_data: OperationCreateHorizontalBar):
        filename = operation_data.file_name
        orientation = operation_data.orientation

        db_name = operation_data.db_name
        user_name = operation_data.user_name
        passw = operation_data.passw
        host = operation_data.host
        table_name = operation_data.table_name
        if not os.path.exists(filename):
            file = pdfgen.CreatingPDF(filename)
            file.createLayout(orientation)
            file.createHorizontalBarChart(db_name, user_name, passw, host, table_name)
        else:
            buf = pdfgen.CreatingPDF("buf.pdf")
            buf.createLayout(orientation)
            buf.createHorizontalBarChart(db_name, user_name, passw, host, table_name)
            merge_two_pdf(filename, "buf.pdf", orientation)
