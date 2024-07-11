import fitz  # PyMuPDF

# Define the path to the PDF file
pdf_path = r'C:\Users\Hp\Documents\projects\python\Pokhara University Result Organiser\MergedPDF\17120010 Bishesh.pdf'

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

# Function to parse and print results for a specific student
def parse_and_print_results(text, student_id):
    # Find the student's data block
    student_data_start = text.find(student_id)
    if student_data_start == -1:
        print(f"Student ID {student_id} not found in the PDF.")
        return
    
    # Extract the lines corresponding to the student's data
    lines = text[student_data_start:].split('\n')
    
    # Filter out empty lines and strip whitespaces
    lines = [line.strip() for line in lines if line.strip()]
    
    # Assuming the number of lines for each semester block and SGPA line
    semester_lines = 7  # 6 subjects + 1 SGPA line

    # Print the results in a formatted table
    print(f"Results for student {student_id}:")
    for semester_start in range(0, len(lines), semester_lines):
        semester_data = lines[semester_start:semester_start + semester_lines]
        
        # Print semester header
        print("\n" + "-" * 40)
        print(f"{'Subject':<30} {'Grade':<10}")
        print("-" * 40)
        
        subjects = [
            "Engineering Mathematics I",
            "Physics",
            "Communication Techniques",
            "Problem Solving Techniques",
            "Basic Electrical Engineering",
            "Programming in C"
        ]
        
        for subject, line in zip(subjects, semester_data[1:]):  # Skip the first line (student ID)
            grade = line.split()[1] if len(line.split()) > 1 else "N/A"
            print(f"{subject:<30} {grade:<10}")
        
        # Print SGPA if available
        if "SGPA" in semester_data[-1]:
            print(f"\nSGPA: {semester_data[-1].split()[-1]}")

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Parse and print results for the specific student
student_id = "17120010"
parse_and_print_results(pdf_text, student_id)
