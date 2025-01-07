# we are going to learn how to work with pdf files in python.
# first step is install pypdf2, pipenv pypdf2

import PyPDF2

# we read the file usinf open
with open("thefalcon_omakran.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    print(len(reader.pages))
    page = reader.pages[0]
    page.rotate(90)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    # now let's write a new pdf file and add the rotate page(page) to it.
    with open("rotated.pdf", "wb") as output:
        writer.write(output)