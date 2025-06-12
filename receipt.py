from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
DATA = [
    [ "Date" , "Name", "Subscription", "Price (Rs.)" ],
    [
        "Student name -",
        "Ashwini Dukkhi",
        ""
    ],
    [
        "04/06/2025",
        "TIT College Bhopal (Student Fees Receipt)",
        "Fees",
        "20,000.00/-",
    ],
    [ "04/06/2025", "Third semester Tution fees", "6 months", "10,000.00/-"],
    [ "Sub Total", "", "", "12,250.00/-"],
    [ "Discount", "", "", "-2,250.00/-"],
    [ "Total", "", "", "10,000.00/-"],
]
pdf = SimpleDocTemplate( "receipt.pdf" , pagesize = A4 )


styles = getSampleStyleSheet()


title_style = styles[ "Heading1" ]
title_style.alignment = 1
title = Paragraph( "Receipt" , title_style )

style = TableStyle(
    [
        ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ),
        ( "GRID" , ( 0, 0 ), ( 5, 5 ), 1 , colors.black ),
        ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ),
        ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ),
        ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ),
        ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ),
    ]
)


table = Table( DATA , style = style )
pdf.build([title,table])
