import fpdf as pyfpdf
 
 
########################################################################
class MyPDF(pyfpdf.FPDF):
    """"""
 
    #----------------------------------------------------------------------
    def header(self):
        """
        Header on each page
        """
        # insert my logo
        #self.image("logo.png", x=10, y=8, w=23)
        # position logo on the right
        #self.cell(w=80)
 
        # set the font for the header, B=Bold
        self.set_font("Arial", style="B", size=15)
        # page title
        self.cell(40,10, "Test Title", border=1, ln=0, align="C")
        # insert a line break of 20 pixels
        self.ln(20)
 
    #----------------------------------------------------------------------
    def footer(self):
        """
        Footer on each page
        """
        # position footer at 15mm from the bottom
        self.set_y(-15)
 
        # set the font, I=italic
        self.set_font("Arial", style="I", size=8)
 
        # display the page number and center it
        pageNum = "Page %s/{nb}" % self.page_no()
        self.cell(0, 10, pageNum, align="C")
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    pdf = MyPDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font("Times", size=10)
 
    # put some lines on the page
    for i in range(1, 50):
        pdf.cell(0, 10, "Line number %s" % i, border=0, ln=1)
    pdf.output("tutorial2.pdf")
