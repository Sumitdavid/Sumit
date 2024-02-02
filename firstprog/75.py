# from pypdf import PdfReader,PdfWriter
# reader=PdfReader("PrajaPalana-Appliancation.pdf")
# number_of_pages=len(reader.pages)
# page=reader.pages[0]
# text=page.extract_text()
# print(text)
# writer=PdfWriter
# # writer.write_stream()
#
# from pypdf import PdfReader
#
# reader = PdfReader("Self Declaration for Authentication of Certificate.pdf")
#
# page = reader.pages[0]
# count = 0
#
# for image_file_object in page.images:
#     with open(str(count) + image_file_object.name) as fp:
#         fp.write(image_file_object.data)
#         count += 1
#

from pypdf import PdfWriter, PdfReader

stamp = PdfReader("192324_corrigendum.pdf").pages[0]
writer = PdfWriter("Self Declaration for Authentication of Certificate.pdf")
for page in writer.pages:
    page.merge_page(stamp)  # here set to False for watermarking

writer.write("out1.pdf")