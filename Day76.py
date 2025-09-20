
"""
Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. You are welcome to add more functionalities

pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well.


"""

from PyPDF2 import PdfWriter

merger = PdfWriter()

input1 = open("C://delete//1.pdf" , "rb")
input2 = open("C://delete//2.pdf" , "rb")


# add the first 1 pages of input1 document to output
merger.append(fileobj=input1, pages=(0, 1))

# insert the first page of input2 into the output beginning after the first page
merger.merge(position=2, fileobj=input2, pages=(0, 1))

output = open("C://delete//document-output.pdf", "wb")
merger.write(output)

# Close File Descriptors
merger.close()
output.close()