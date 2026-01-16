from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from io import BytesIO
from datetime import datetime
from .qr_generator import generate_qr_code

def generate_modern_template(data: dict) -> BytesIO:

    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    
    
    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer
