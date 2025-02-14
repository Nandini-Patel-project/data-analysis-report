# Create or overwrite data in a CSV file
def create_sample_file():
    # Large set of data (first and second pages)
    all_data = """Name,Score
Alice,85
Bob,90
Charlie,78
David,92
Emily,88
Frank,80
Grace,95
Hannah,91
Isaac,84
Jack,89
Lily,94
Mason,87
Nora,82
Oscar,77
Paul,93
Quinn,79
Rachel,85
Samuel,92
Tina,81
Uma,83
Victor,90
Wendy,88
Xander,91
Yara,86
Zane,80
Amelia,88
Ben,91
Clara,84
Daniel,92
Ella,89
Finn,86
Georgia,82
Henry,93
Ivy,85
James,87
Kylie,78
Leo,90
Maya,94
Nathan,85
Olivia,92
Penny,79
Quincy,91
Riley,88
Sophia,83
Tyler,77
Ursula,90
Vera,84
Will,89
Xena,82
Yasmin,80
Zoe,88
"""
    
    # Create the file and write the full data
    with open("data.csv", "w") as file:
        file.write(all_data)
    print("data.csv file created with fresh data.")

# Call the function to create the file with full data
create_sample_file()
