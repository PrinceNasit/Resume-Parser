import PyPDF2

def get_links(filename):
    links=[]
    pdf_reader = PyPDF2.PdfReader(filename)
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        annotations = page.get('/Annots')
        if annotations:
            for annotation in annotations:
                annotation_object = annotation.get_object()
                if annotation_object.get('/Subtype') == '/Link':
                    link = annotation_object.get('/A').get('/URI')
                    if link:
                        links.append(link)
    # for x in links:
    #     print(x)
    print(links)
    return links    
get_links('My_resume.pdf')
# from docx import Document
# import re

# def extract_links_from_docx(docx_path):
#     links = []
#     doc = Document(docx_path)
#     for paragraph in doc.paragraphs:
#         text = paragraph.text
#         urls = re.findall(r'https?://\S+', text)
#         links.extend(urls)
#     return links

# links = extract_links_from_docx('My_resume.docx')
# for link in links:
#     print(link)
