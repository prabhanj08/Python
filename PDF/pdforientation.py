from reportlab.pdfgen.canvas import Canvas
from PyPDF2 import PdfFileReader,PdfFileWriter
import os,re

# Logic to check file size
output = PdfFileWriter()
tempoutput = PdfFileWriter()
pdfFileWriter = PdfFileWriter()
blank_page = []

pdf_path = 'D:\My_work\Studies\Datasets\sample.pdf'
outfile = 'D:\My_work\Studies\Datasets\sample_res.pdf'


# Check file size

def getSize(filename):
    st = os.stat(filename)
    return st.st_size

filesize = os.path.getsize(pdf_path)
if filesize == 0:
    print("The file is empty: " + str(filesize))
    exit()
else:
    print("The file is not empty: " + str(filesize))

'''Logic to check PDF orientation '''
    pdf_reader = PdfFileReader(pdf_path)
    numPages1 = pdf_reader.getNumPages()
    deg = pdf_reader.getPage(0).get('/Rotate')
    page = pdf_reader.getPage(0).mediaBox
    if page.getUpperRight_x() - page.getUpperLeft_x() > page.getUpperRight_y() -page.getLowerRight_y():
        if deg in [0,180,None]:
            print('Landscape')
        else:
            print('Portrait')
    else:
        if deg in [0,180,None]:
            print('Portrait')
        else:
            print('Landscape')

'''Logic to get empty files List '''

    for i in range(numPages1):
        s = ''
        canv1 = Canvas("paginatemporal.pdf")
        canv1.showPage()
        canv1.save()
        archivotemp = open("paginatemporal.pdf", "rb")
        temporal = PdfFileReader(archivotemp)
        page = pdf_reader.getPage(i)
        page.mergePage(temporal.getPage(0))
        tempoutput.addPage(page)
        outputStreamTemp = open("paginasize.pdf", "wb")
        tempoutput.write(outputStreamTemp)
        page = pdf_reader.getPage(i)
        text = (page.extractText())
        s = ("".join(text.split()))
        pdfsize1 = getSize("paginasize.pdf")
        if len(s) < 2:
            blank_page.append(i+1)
        else:
            print("Page number " + str(i + 1) + " is not blank.")
            pass

''' Logic to delete empty pages'''

    for index in range(1, numPages1):
        if index not in blank_page:
            pageObj = pdf_reader.getPage(index-1)
            pdfFileWriter.addPage(pageObj)
    pdfFileWriter.write(open(outfile, 'wb'))

archivotemp.close()
outputStreamTemp.close()
