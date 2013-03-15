import fpdf as pyfpdf
from fpdf import FPDF, HTMLMixin

class MyFPDF(FPDF, HTMLMixin):
    pass
                    
pdf=MyFPDF()

#First page
#pdf = pyfpdf.FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=10)
html = """<H1 align="center">Summary of Inquiries</H1>
<h3>Date:</h3>
<h3>Branch:</h3>"""
html += """
<table border="1" align="center" width="100%">
<thead><tr><th width="15%">Date of Inquiry</th><th width="15%">Name of Customer</th><th width="15%">Address</th><th width="15%">Contact Number</th><th width="15%">Receptionist</th><th width="15%">Status</th></tr></thead>
<tbody>
<tr><td>cell 1hgjhh jhjhjk jhj</td><td>cell 2</td></tr>
<tr><td>cell 2</td><td>cell 3</td></tr>
"""
html += '<tr><td>' + 'data' + '</td><td>' + 'data' +'</td></tr>'
html += """</tbody></table>"""
pdf.write_html(html)
pdf.output('html.pdf','F')
