import os
import PyPDF2

def find_and_merge_pdfs(directories, roll_number, output_file):
    merger = PyPDF2.PdfMerger()
    
    for dir_path in directories:
        for root, _, files in os.walk(dir_path):
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

# Define the base directory containing the result folders and the roll number
base_directory = r'C:\Users\Hp\Documents\projects\python\Pokhara University Result Organiser\Result'
roll_number = '17120032'
output_pdf_path = r'C:\Users\Hp\Documents\projects\python\Pokhara University Result Organiser\Merged_BEIT_Result_2017_2023.pdf'

# Define the directories for the required years and semesters
directories = {
    'PU_2017..2018Fall': os.path.join(base_directory, '3. PU_2017..2018Fall'),
    'PU_2017..2018Spring': os.path.join(base_directory, '4. PU_2017..2018Spring'),
    'PU_2018..2019Fall': os.path.join(base_directory, '5. PU_2018..2019Fall'),
    'PU_2018..2019Spring': os.path.join(base_directory, '6. PU_2018..2019Spring'),
    'PU_2019..2020Fall': os.path.join(base_directory, '7. PU_2019..2020Fall'),
    'PU_2019..2020Spring': os.path.join(base_directory, '8. PU_2019..2020Spring'),
    'PU_2020..2021Fall': os.path.join(base_directory, '9. PU_2020..2021Fall'),
    'PU_2020..2021Spring': os.path.join(base_directory, '10. PU_2020..2021Spring'),
    'PU_2021..2022Fall': os.path.join(base_directory, '11. PU_2021..2022Fall'),
    'PU_2021..2022Spring': os.path.join(base_directory, '12. PU_2021..2022Spring'),
    'PU_2022..2023Fall': os.path.join(base_directory, '13. PU_2022..2023Fall'),
}

# Convert dictionary values to a list
directories_to_process = list(directories.values())

# Call the function to find and merge the PDFs
find_and_merge_pdfs(directories_to_process, roll_number, output_pdf_path)