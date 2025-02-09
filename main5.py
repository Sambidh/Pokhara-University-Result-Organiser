import os
import PyPDF2

def find_and_merge_pdfs(directories, roll_number, output_file):
    merger = PyPDF2.PdfMerger()
    valid_grades = ['A', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D']
    invalid_terms = ['F', 'Abs', 'Expelled', 'Withheld', '', 'CNR', 'Rechecking', 'Re-totaling']

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
                                lines = text.split('\n')
                                for line in lines:
                                    if roll_number in line:
                                        grades_in_line = [grade for grade in line.split() if grade in valid_grades + invalid_terms]
                                        # Merge the page if there is any valid grade present
                                        if any(grade in valid_grades for grade in grades_in_line):
                                            merger.append(fileobj=pdf_file, pages=(page_num, page_num + 1))
                                            break  # Stop after finding the first relevant page
                                else:
                                    continue
                                break

    if merger.pages:
        with open(output_file, 'wb') as output_pdf:
            merger.write(output_pdf)
        print(f"Merged PDF saved as {output_file}")
    else:
        print("No pages found meeting the criteria. Merged PDF not created.")

roll_number = input("Enter your roll number: ")
output_file_name = input("Enter the name for the merged PDF file (without extension): ")

base_directory = r'C:\Users\Hp\Documents\projects\python\Pokhara University Result Organiser\Result'
merged_pdf = r'C:\Users\Hp\Documents\projects\python\Pokhara University Result Organiser\MergedPDF'
output_pdf_path = os.path.join(merged_pdf, f"{roll_number} {output_file_name}.pdf")

directories = {
    'PU_2016..2017Fall': os.path.join(base_directory, '1. PU_2016..2017Fall'),
    'PU_2016..2017Spring': os.path.join(base_directory, '2. PU_2016..2017Spring'),
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

directories_to_process = list(directories.values())

find_and_merge_pdfs(directories_to_process, roll_number, output_pdf_path)
