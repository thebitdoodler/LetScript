# Python program to convert docx to pdf using docx2pdf module

# Import the convert method from the docx2pdf module

#code 

from docx2pdf import convert

# Converting docx present in the same folder as the python file
convert("TEST.docx")

# Converting docx specifying both the input and output paths
convert("TEST\TEST_1.docx", "New_Folder\Mine.pdf")

# Notice that the output filename need not be the same as the docx

# Bulk Conversion
convert("TEST\")
