import fitz  # PyMuPDF

# Define the path to the PDF file
pdf_path = r'C:\Users\Hp\Documents\projects\python\Pokhara University Result Organiser\MergedPDF\17120010 Bishesh.pdf'

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text("text")
    return text

# Function to parse and print results for the first semester
def parse_and_print_results(text, student_id):
    # Define subjects for the first semester
    subjects = [
        "Engineering Mathematics I",
        "Physics",
        "Communication Techniques",
        "Problem Solving Techniques",
        "Basic Electrical Engineering",
        "Programming in C"
    ]
    
    # Find the student's data block
    student_data_start = text.find(student_id)
    if student_data_start == -1:
        print(f"Student ID {student_id} not found in the PDF.")
        return
    
    # Extract the lines corresponding to the student's data
    lines = text[student_data_start:].split('\n')
    
    # Combine lines until reaching the end of the data block
    student_data = []
    for line in lines:
        if line.strip().isdigit() or line.strip().startswith(student_id):
            student_data.append(line.strip())
        else:
            break
    
    # Combine the data lines
    student_line = " ".join(student_data)
    
    # Split the student's data line into words
    data = student_line.split()
    
    # Ensure the data length matches the expected number of subjects + 2 (for ID and SGPA)
    if len(data) != len(subjects) + 2:
        print("The data format does not match the expected number of subjects.")
        return
    
    # Print the results in a formatted table
    print(f"Results for student {student_id} (First Semester):")
    print("-" * 60)
    print(f"{'Subject':<40} {'Grade':<10}")
    print("-" * 60)
    
    # Extract and print grades for each subject
    for i, subject in enumerate(subjects):
        grade = data[i + 1]
        print(f"{subject:<40} {grade:<10}")
    
    # Print SGPA if available
    sgpa = data[-1]
    print(f"\nSGPA: {sgpa}")

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Parse and print results for the specific student
student_id = "17120010"
parse_and_print_results(pdf_text, student_id)
