from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, XMLConverter, HTMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text
    #return str(text).split()

pdfDir = "E:\\Kishore.pdf"
#txtDir = "C:\\Users\\Mythrebi Selvan\\Desktop\\sampleresume\\out"
text = convert(pdfDir)
textFile = open("E:\\Kishoreout", "w",encoding="utf-8")
textFile.write(text)
convert(pdfDir)