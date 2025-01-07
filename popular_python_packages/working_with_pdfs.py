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

# now we are going to combine multiple pdfs into a single pdf
file_names = ["thefalcon_omakran.pdf", "rotated.pdf"]
merger = PyPDF2.PdfMerger()
for file_name in file_names:
    merger.append(file_name)
merger.write("combine.pdf") # we create the new pdf