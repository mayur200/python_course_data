from PyPDF2 import  PdfFileReader
import pandas as pd


pdf_read  = PdfFileReader('/home/mayur/Downloads/2monthbank.pdf')
page = pdf_read.getPage(0)
page_content = page.extractText()
print(page_content)
