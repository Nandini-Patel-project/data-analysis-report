import pandas as pd
from fpdf import FPDF

# Read data from a CSV file
def read_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("Error: File not found.")
        return None

# Analyze the data
def analyze_data(data):
    analysis_results = {
        "average_score": data['Score'].mean(),
        "max_score": data['Score'].max(),
        "min_score": data['Score'].min(),
        "total_students": len(data),
        "highest_score_student": data.loc[data['Score'].idxmax()]['Name'],
        "lowest_score_student": data.loc[data['Score'].idxmin()]['Name'],
    }
    return analysis_results

# Define the PDF class
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Automated Report', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# Generate the PDF report
def generate_pdf_report(data, analysis_results, output_file):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)

    # Add content to the PDF
    pdf.cell(0, 10, 'Data Analysis Report', 0, 1, 'C')
    pdf.ln(10)  # Line break

    # Add analysis results
    pdf.cell(0, 10, f"Average Score: {analysis_results['average_score']:.2f}", 0, 1)
    pdf.cell(0, 10, f"Maximum Score: {analysis_results['max_score']}", 0, 1)
    pdf.cell(0, 10, f"Minimum Score: {analysis_results['min_score']}", 0, 1)
    pdf.cell(0, 10, f"Total Students: {analysis_results['total_students']}", 0, 1)
    pdf.cell(0, 10, f"Highest Scoring Student: {analysis_results['highest_score_student']}", 0, 1)
    pdf.cell(0, 10, f"Lowest Scoring Student: {analysis_results['lowest_score_student']}", 0, 1)
    
    pdf.ln(10)  # Line break

    # Add a table of all students' scores
    pdf.cell(40, 10, 'Student Name', 1)
    pdf.cell(40, 10, 'Score', 1)
    pdf.ln()

    for index, row in data.iterrows():
        pdf.cell(40, 10, row['Name'], 1)
        pdf.cell(40, 10, str(row['Score']), 1)
        pdf.ln()

    # Save the PDF
    pdf.output(output_file)
    print(f"Report saved as {output_file}")

# Main function
def main():
    file_path = 'data.csv'  # Replace with your file name
    output_file = 'report.pdf'

    # Step 1: Read the data
    data = read_data(file_path)
    if data is None:
        return

    # Step 2: Analyze the data
    analysis_results = analyze_data(data)

    # Step 3: Generate the PDF report
    generate_pdf_report(data, analysis_results, output_file)

# Run the script
if __name__ == "__main__":
    main()
