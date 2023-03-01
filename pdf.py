# importing required modules
from PyPDF2 import PdfReader

# creating a pdf reader object
reader = PdfReader('Results sem.pdf')

# printing number of pages in pdf file
print(len(reader.pages))

# getting a specific page from the pdf file
page = reader.pages[0]

# extracting text from page
text = page.extract_text(0)
print(text.find('CODESUBJECT'))

