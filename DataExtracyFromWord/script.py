from docx import Document
import jsone

file = '1.docx'
document = Document(file)
for paragraph in document.paragraphs:
    if paragraph.style.name == 'Heading 2':
        print(paragraph.text)
    if paragraph.style.name == 'Heading 3':
        print(paragraph.text)
