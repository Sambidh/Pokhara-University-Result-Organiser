import os
import PyPDF2

def find_and_merge_pdfs(base_dir, roll_number, output_file):
    merger = PyPDF2.PdfMerger()
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                with open(pdf_path, 'rb') as pdf_file:
                    reader = PyPDF2.PdfReader(pdf_file)
                    for page_num in range(len(reader.pages)):
                        page = reader.pages[page_num]
                        text = page.extract_text()
                        if roll_number in text:
                            merger.append(pdf_file, pages=(page_num, page_num+1))
    
    with open(output_file, 'wb') as output_pdf:
        merger.write(output_pdf)

    print(f'Merged PDF saved as {output_file}')

base_directory = r'C:\Users\Hp\Documents\projects\python\Pokhara University Result Organiser\Result'
roll_number = '17120032'
output_pdf_path = r'C:\Users\Hp\Documents\projects\python\Pokhara University Result Organiser\Merged_BEIT_Result.pdf'

find_and_merge_pdfs(base_directory, roll_number, output_pdf_path)
