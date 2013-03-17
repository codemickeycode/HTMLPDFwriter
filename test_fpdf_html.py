import fpdf as pyfpdf
from fpdf import FPDF, HTMLMixin

class MyFPDF(FPDF, HTMLMixin):
    pass

pdf=MyFPDF()

#First page
#pdf = pyfpdf.FPDF(format='letter')
pdf.add_page()
#set the font
pdf.set_font("Arial", size=10)

#define the html text
html = """<H1 align="center">Summary of Transactions</H1>
<h3>Date:</h3>
<h3>Branch:</h3>"""
html += """
<table border="1" align="center" width="100%">
<thead><tr><th width="20%">Date of Transaction</th><th width="20%">Name of Customer</th><th width="20%">Address</th><th width="20%">Contact Number</th><th width="20%">Status</th></tr></thead>
<tbody>
<tr><td>cell 1hgjhh jhjhjk jhjfsafsafsafsaf</td><td>cell 2</td><td>cell 3</td><td>cell 4</td><td>cell 5</td></tr>
<tr><td>cell 1</td><td>cell 2</td><td>cell 3</td><td>cell 4</td><td>cell 5</td></tr>
"""
html += '<tr><td>' + 'data' + '</td><td>' + 'data' +'</td> <td>' + 'data' +'</td> <td>' + 'data' +'</td><td>' + 'data' +'</td></tr>'
html += """</tbody></table>"""

html2 ="""<table>
    <tr>
      <th>#</th>
      <th>test</th>
      <th> ting</th>
      <th> 1</th>
      <th> 2</th>
      <th> 3</th>
    </tr>
    <tr>
      <td>1</td>
      <td>hey</td>
      <td> ho</td>
      <td> lets</td>
      <td> go</td>
    </tr>
  </table>"""

#write the html text to PDF
pdf.write_html(html)
pdf.output('html.pdf','F')
