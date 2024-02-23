import csv
import random
from datetime import datetime, timedelta


def generate_student_data(num_students, first_names, last_names, schools, programs):
    dataset = []

    for _ in range(num_students):
        student_id = random.randint(100000, 999999)
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        birth_date = (datetime.now() - timedelta(days=random.randint(365 * 18, 365 * 25))).strftime('%Y-%m-%d')
        school = random.choice(schools)
        program = random.choice(programs[school])
        gpa = round(random.uniform(2.5, 4.0), 2)

        student_data = {
            'Student ID': student_id,
            'First Name': first_name,
            'Last Name': last_name,
            'Birth Date': birth_date,
            'School': school,
            'Program': program,
            'GPA': gpa
        }

        dataset.append(student_data)

    return dataset

def save_to_csv(dataset, filename='university_dataset.csv'):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Student ID', 'First Name', 'Last Name', 'Birth Date', 'School', 'Program', 'GPA']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for student_data in dataset:
            writer.writerow(student_data)

if __name__ == '__main__':
    num_students = 5000

    schools = ["School of Engineering", "School of Science", "School of Business", "School of Computer Science"]
    
    programs = {
        "School of Engineering": ["CIE", "Nano Tech", "Renewable", "Aero Space"],
        "School of Science": ["Bio Medical", "Nano", "Physics"],
        "School of Business": ["Finance", "Marketing", "Management"],
        "School of Computer Science": ["DSAI", "SWD", "IT"]
    }

    first_names = ["Mohamed", "Ziad", "Ahmed", "Mahmoud","Seif","Rony","Mazen", "Mark", "Ali", "Omar", "Amr", "Khaled", "Hassan", "Hussein", "Abdullah", "Abdulrahman", "Abdulaziz", "Youssef", "Karim", "Yahia", "Yasser", "Mariam", "Rahma", "Nour", "Hana", "Fatma", "Aya", "Nada", "Haneen", "Sara", "Nouran", "Salma", "Layla", "Lina"]
    last_names = ["Moahmed","Moataz","Khaled", "Ahmed", "Mahmoud", "Taha", "Ali", "Abdelsalam", "Abdelrahim", "Abdulrahman", "Abdulaziz", "Abdullah", "Youssef", "Karim", "Yahia", "Yasser", "Mostafa", "Tarek", "Shaaban", "Ramadan", "Hendy", "Samir", "Walid", "Hatem", "Hani"]

    university_dataset = generate_student_data(num_students, first_names, last_names, schools, programs)
    save_to_csv(university_dataset, 'templates//university_dataset.csv')
    print(f'{num_students} student records generated and saved to university_dataset.csv')
