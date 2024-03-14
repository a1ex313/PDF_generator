from reportlab.pdfgen import canvas

from reportlab.graphics.charts.barcharts import VerticalBarChart, VerticalBarChart3D
from reportlab.graphics.charts.barcharts import HorizontalBarChart, HorizontalBarChart3D
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF

import psycopg2

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4, portrait, landscape
from reportlab.pdfbase import pdfmetrics
from PyPDF2 import PdfWriter, PdfReader, PdfMerger
import io, os
import pathlib

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table, TableStyle, colors

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('arial', 'arial.ttf'))

#A4 is 595 × 842 points

class Layout:
    def __init__(self, filename):
        self.filename = filename
        self.file_pdf = canvas.Canvas(self.filename)
        self.image1 = 'image1.jpg'
        self.image2 = 'image2.jpg'
        self.orientation = ''


    def createLayout(self, orientation):
        if orientation == 'portrait':
            self.orientation = 'portrait'
            self.file_pdf.setPageSize(portrait(A4))

            # self.file_pdf.setFont("arial", 20)
            # self.file_pdf.setTitle("Report")
            # self.file_pdf.drawString(270, 770, "Report")
            self.file_pdf.save()
        elif orientation == 'landscape':
            self.orientation = 'landscape'
            self.file_pdf.setPageSize(landscape(A4))

            # self.file_pdf.setFont("arial", 20)
            # self.file_pdf.setTitle("Report")
            # self.file_pdf.drawString(400, 520, "Report")
            self.file_pdf.save()


    def createTemplate(self):
        template_pdf = canvas.Canvas("template.pdf")

        if self.orientation == 'portrait':
            template_pdf.setPageSize(portrait(A4))

            template_pdf.drawImage(self.image1, 10, 740, 120, 100)
            template_pdf.drawImage(self.image2, 450, 15)
            template_pdf.save()
        elif self.orientation == 'landscape':
            template_pdf.setPageSize(landscape(A4))

            template_pdf.drawImage(self.image1, 10, 470, 120, 100)
            template_pdf.drawImage(self.image2, 680, 25)
            template_pdf.save()


    def deleteTemplate(self):
        os.remove("template.pdf")


    def drawMarking(self):
        buffile_pdf = canvas.Canvas("buffer.pdf")


        if self.orientation == 'portrait':
            buffile_pdf.setPageSize(portrait(A4))
            buffile_pdf.drawString(100, 800, 'x100')
            buffile_pdf.line(100, 0, 100, 850)
            buffile_pdf.drawString(200, 800, 'x200')
            buffile_pdf.line(200, 0, 200, 850)
            buffile_pdf.drawString(300, 800, 'x300')
            buffile_pdf.line(300, 0, 300, 850)
            buffile_pdf.drawString(400, 800, 'x400')
            buffile_pdf.line(400, 0, 400, 850)
            buffile_pdf.drawString(500, 800, 'x500')
            buffile_pdf.line(500, 0, 500, 850)

            buffile_pdf.drawString(10, 100, 'y100')
            buffile_pdf.line(0, 100, 600, 100)
            buffile_pdf.drawString(10, 200, 'y200')
            buffile_pdf.line(0, 200, 600, 200)
            buffile_pdf.drawString(10, 300, 'y300')
            buffile_pdf.line(0, 300, 600, 300)
            buffile_pdf.drawString(10, 400, 'y400')
            buffile_pdf.line(0, 400, 600, 400)
            buffile_pdf.drawString(10, 500, 'y500')
            buffile_pdf.line(0, 500, 600, 500)
            buffile_pdf.drawString(10, 600, 'y600')
            buffile_pdf.line(0, 600, 600, 600)
            buffile_pdf.drawString(10, 700, 'y700')
            buffile_pdf.line(0, 700, 600, 700)
            buffile_pdf.drawString(10, 800, 'y800')
            buffile_pdf.line(0, 800, 600, 800)
            buffile_pdf.save()
        else:
            buffile_pdf.setPageSize(landscape(A4))
            buffile_pdf.drawString(100, 0, 'x100')
            buffile_pdf.line(100, 0, 100, 600)
            buffile_pdf.drawString(200, 0, 'x200')
            buffile_pdf.line(200, 0, 200, 600)
            buffile_pdf.drawString(300, 0, 'x300')
            buffile_pdf.line(300, 0, 300, 600)
            buffile_pdf.drawString(400, 0, 'x400')
            buffile_pdf.line(400, 0, 400, 600)
            buffile_pdf.drawString(500, 0, 'x500')
            buffile_pdf.line(500, 0, 500, 600)
            buffile_pdf.drawString(600, 0, 'x600')
            buffile_pdf.line(600, 0, 600, 600)
            buffile_pdf.drawString(700, 0, 'x700')
            buffile_pdf.line(700, 0, 700, 600)
            buffile_pdf.drawString(800, 0, 'x800')
            buffile_pdf.line(800, 0, 800, 600)

            buffile_pdf.drawString(10, 100, 'y100')
            buffile_pdf.line(0, 100, 850, 100)
            buffile_pdf.drawString(10, 200, 'y200')
            buffile_pdf.line(0, 200, 850, 200)
            buffile_pdf.drawString(10, 300, 'y300')
            buffile_pdf.line(0, 300, 850, 300)
            buffile_pdf.drawString(10, 400, 'y400')
            buffile_pdf.line(0, 400, 850, 400)
            buffile_pdf.drawString(10, 500, 'y500')
            buffile_pdf.line(0, 500, 850, 500)
            buffile_pdf.save()

        file1 = PdfReader(self.filename, 'rb')
        file2 = PdfReader("buffer.pdf", 'rb')
        output = PdfWriter()

        for page_num in range(0, len(file1.pages)):
            page = file1.pages[page_num]
            page.merge_page(file2.pages[0])
            output.add_page(page)

        with open(self.filename, "wb") as outputStream:
            output.write(outputStream)
        os.remove("buffer.pdf")


    def merge_pdf(self, file_name):
        self.createTemplate()
        file1 = PdfReader(file_name, 'rb')
        file2 = PdfReader("template.pdf", 'rb')
        output = PdfWriter()

        for page_num in range (len(file1.pages)):
            page = file1.pages[page_num]
            page.merge_page(file2.pages[0])
            output.add_page(page)

        with open("output.pdf", "wb") as outputStream:
            output.write(outputStream)

        merger = PdfMerger()
        merger.append(PdfReader(self.filename, 'rb'))
        merger.append(PdfReader("output.pdf", 'rb'))
        merger.write(self.filename)
        merger.close()

        os.remove(file_name)
        os.remove("output.pdf")
        self.deleteTemplate()


class CreatingPDF(Layout):
    def __init__(self, filename):
        super().__init__(filename)


    def get_data(self, db_name, user, password, host, table_name):
        conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host
        )

        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table_name};")

        column_names = [desc[0] for desc in cur.description]
        rows = cur.fetchall()

        data_list = []
        for i in range(len(rows)):
            data_list.append(rows[i])

        cur.close()
        conn.close()

        return column_names, data_list


    def createTable(self, db_name, user, password, host, table_name):
        column_names, data_list = self.get_data(db_name, user, password, host, table_name)

        data = []
        data.append(column_names)
        for i in range(len(data_list)):
            data.append(data_list[i])

        if self.orientation == 'portrait':
            pdf = SimpleDocTemplate(
                "table.pdf",
                pagesize=portrait(A4),
            )
        else:
            pdf = SimpleDocTemplate(
                "table.pdf",
                pagesize=landscape(A4),
            )

        table = Table(data)

        style = TableStyle([
            #('BACKGROUND', (0,0), (-1,0), colors.red),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, -1), 'arial'),
            ('FONTSIZE', (0, 0), (-1, -1), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12)
        ])
        table.setStyle(style)

        rownumb = len(data)
        for row in range(1, rownumb):
            if row % 2 == 0:
                back_color = colors.lightgrey
            else:
                back_color = colors.beige

            ts = TableStyle(
                [('BACKGROUND', (0, row), (-1, row), back_color)]

            )
            table.setStyle(ts)

        borders = TableStyle(
            [
                ('BOX', (0, 0), (-1, -1), 2, colors.black),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]
        )
        table.setStyle(borders)

        elems = []
        elems.append(table)
        pdf.build(elems)

        self.merge_pdf("table.pdf")


    def createVerticalBarChart(self,  db_name, user, password, host, table_name):
        columns, data_list = self.get_data(db_name, user, password, host, table_name)

        column_names = columns[1:]
        data = []
        for i in range(len(data_list)):
            data.append(data_list[i][1:])

        if self.orientation == 'portrait':
            d = Drawing(595, 842)
            bc = VerticalBarChart()
            bc.x = 50  # horizontal position
            bc.y = 120  # vertical position
            bc.height = 600  # height of the chart area
            bc.width = 500  # width of the chart area
            bc.data = data
            bc.strokeColor = colors.black  # bar edges colour
            # bc.bars[0].fillColor = colors.yellow  # first member of group bar
            # bc.bars[1].fillColor = colors.lightgreen  # second member of group
            bc.groupSpacing = 10  # gap between groups
            bc.barSpacing = 2.5  # gap within groups ( among members )
            bc.valueAxis.valueMin = 0  # value Axis
            bc.valueAxis.valueMax = 50
            bc.valueAxis.valueStep = 10
            bc.categoryAxis.labels.boxAnchor = 'ne'
            bc.categoryAxis.labels.dx = 5
            bc.categoryAxis.labels.dy = -2
            bc.categoryAxis.labels.angle = 45

            # bc.categoryAxis.style = 'stacked' # stacked bar graph, parallel
            bc.categoryAxis.categoryNames = column_names
            d.add(bc, '')
        elif self.orientation == 'landscape':
            d = Drawing(842, 595)
            bc = VerticalBarChart()
            bc.x = 160  # horizontal position
            bc.y = 120  # vertical position
            bc.height = 400  # height of the chart area
            bc.width = 600  # width of the chart area
            bc.data = data
            bc.strokeColor = colors.black  # bar edges colour
            # bc.bars[0].fillColor = colors.yellow  # first member of group bar
            # bc.bars[1].fillColor = colors.lightgreen  # second member of group
            bc.groupSpacing = 10  # gap between groups
            bc.barSpacing = 2.5  # gap within groups ( among members )
            bc.valueAxis.valueMin = 0  # value Axis
            bc.valueAxis.valueMax = 50
            bc.valueAxis.valueStep = 10
            bc.categoryAxis.labels.boxAnchor = 'ne'
            bc.categoryAxis.labels.dx = 5
            bc.categoryAxis.labels.dy = -2
            bc.categoryAxis.labels.angle = 30
            # bc.categoryAxis.style = 'stacked' # stacked bar graph, parallel
            bc.categoryAxis.categoryNames = column_names
            d.add(bc, '')

        renderPDF.drawToFile(d, "VertBarChars.pdf", '')
        self.merge_pdf("VertBarChars.pdf")


    def createHorizontalBarChart(self, db_name, user, password, host, table_name):
        columns, data_list = self.get_data(db_name, user, password, host, table_name)

        column_names = columns[1:]
        data = []
        for i in range(len(data_list)):
            data.append(data_list[i][1:])

        if self.orientation == 'portrait':
            d = Drawing(595, 842)
            bc = HorizontalBarChart()
            bc.x = 70  # horizontal position
            bc.y = 120  # vertical position
            bc.height = 600  # height of the chart area
            bc.width = 480  # width of the chart area
            bc.data = data
            bc.strokeColor = colors.black  # bar edges colour
            # bc.bars[0].fillColor = colors.yellow  # first member of group bar
            # bc.bars[1].fillColor = colors.lightgreen  # second member of group
            bc.groupSpacing = 10  # gap between groups
            bc.barSpacing = 2.5  # gap within groups ( among members )
            bc.valueAxis.valueMin = 0  # value Axis
            bc.valueAxis.valueMax = 50
            bc.valueAxis.valueStep = 10
            bc.categoryAxis.labels.boxAnchor = 'ne'
            bc.categoryAxis.labels.dx = -15
            bc.categoryAxis.labels.dy = -2
            bc.categoryAxis.labels.angle = 45
            # bc.categoryAxis.style = 'stacked' # stacked bar graph, parallel
            bc.categoryAxis.categoryNames = column_names
            d.add(bc, '')
        elif self.orientation == 'landscape':
            d = Drawing(842, 595)
            bc = HorizontalBarChart()
            bc.x = 160  # horizontal position
            bc.y = 120  # vertical position
            bc.height = 400  # height of the chart area
            bc.width = 600  # width of the chart area
            bc.data = data
            bc.strokeColor = colors.black  # bar edges colour
            # bc.bars[0].fillColor = colors.yellow  # first member of group bar
            # bc.bars[1].fillColor = colors.lightgreen  # second member of group
            bc.groupSpacing = 10  # gap between groups
            bc.barSpacing = 2.5  # gap within groups ( among members )
            bc.valueAxis.valueMin = 0  # value Axis
            bc.valueAxis.valueMax = 50
            bc.valueAxis.valueStep = 10
            bc.categoryAxis.labels.boxAnchor = 'ne'
            bc.categoryAxis.labels.dx = 5
            bc.categoryAxis.labels.dy = -2
            bc.categoryAxis.labels.angle = 30
            # bc.categoryAxis.style = 'stacked' # stacked bar graph, parallel
            bc.categoryAxis.categoryNames = column_names
            d.add(bc, '')

        renderPDF.drawToFile(d, "HorizBarChars.pdf", '')
        self.merge_pdf("HorizBarChars.pdf")


def merge_two_pdf(file_name1, file_name2, orientation):
    def createTemplate(orientation):
        template_pdf = canvas.Canvas("template.pdf")
        image1 = 'image1.jpg'
        image2 = 'image2.jpg'

        if orientation == 'portrait':
            template_pdf.setPageSize(portrait(A4))

            template_pdf.drawImage(image1, 10, 740, 120, 100)
            template_pdf.drawImage(image2, 450, 15)
            template_pdf.save()
        elif orientation == 'landscape':
            template_pdf.setPageSize(landscape(A4))

            template_pdf.drawImage(image1, 10, 470, 120, 100)
            template_pdf.drawImage(image2, 680, 25)
            template_pdf.save()


    def deleteTemplate():
        os.remove("template.pdf")


    createTemplate(orientation)
    file1 = PdfReader(file_name2, 'rb')
    file2 = PdfReader("template.pdf", 'rb')
    output = PdfWriter()

    for page_num in range(len(file1.pages)):
        page = file1.pages[page_num]
        page.merge_page(file2.pages[0])
        output.add_page(page)

    with open("output.pdf", "wb") as outputStream:
        output.write(outputStream)

    merger = PdfMerger()
    merger.append(PdfReader(file_name1, 'rb'))
    merger.append(PdfReader("output.pdf", 'rb'))
    merger.write(file_name1)
    merger.close()

    os.remove(file_name2)
    os.remove("output.pdf")
    deleteTemplate()



if __name__ == "__main__":
    myfile = CreatingPDF("Report.pdf")
    myfile.createLayout('landscape')
    # myfile.createLayout('portrait')

    myfile.createTable("db_pdf", "root", "1111", "localhost", "records")

    myfile.createVerticalBarChart("db_barchart", "root", "1111",
                                  "localhost", "data_bc")

    myfile.createHorizontalBarChart("db_barchart", "root", "1111",
                                    "localhost", "data_bc")

    # myfile.drawMarking()
