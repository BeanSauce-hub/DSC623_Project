import sqlite3


##Question a
def create_schema():
    connection = sqlite3.connect("dbms_project.db")
    cursor = connection.cursor()

    # Create tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Clinic (
            clinicNo CHAR(5) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            address VARCHAR(255) NOT NULL,
            telephoneNo VARCHAR(20) UNIQUE NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Staff (
            staffNo CHAR(5) PRIMARY KEY,
            clinicNo CHAR(5) NOT NULL,
            name VARCHAR(255) NOT NULL,
            address VARCHAR(255) NOT NULL,
            telephoneNo VARCHAR(20) NOT NULL,
            DOB DATE NOT NULL,
            position VARCHAR(255) NOT NULL,
            salary DECIMAL(10, 2) NOT NULL,
            FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Owner (
            ownerNo CHAR(5) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            address VARCHAR(255) NOT NULL,
            telephoneNo VARCHAR(20) UNIQUE NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Pet (
            petNo CHAR(5) PRIMARY KEY,
            ownerNo CHAR(5) NOT NULL,
            clinicNo CHAR(5) NOT NULL,
            name VARCHAR(255) NOT NULL,
            DOB DATE NOT NULL,
            species VARCHAR(255) NOT NULL,
            breed VARCHAR(255) NOT NULL,
            color VARCHAR(50) NOT NULL,
            FOREIGN KEY (ownerNo) REFERENCES Owner(ownerNo),
            FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Examination (
            examNo CHAR(5) PRIMARY KEY,
            petNo CHAR(5) NOT NULL,
            staffNo CHAR(5) NOT NULL,
            complaint VARCHAR(255) NOT NULL,
            description TEXT NOT NULL,
            examDate DATE NOT NULL,
            actionsTaken TEXT,
            FOREIGN KEY (petNo) REFERENCES Pet(petNo),
            FOREIGN KEY (staffNo) REFERENCES Staff(staffNo)
        );
    """)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_schema()
    print("Database schema created successfully.")


##Question b
def insert_data():
    connection = sqlite3.connect("dbms_project.db")
    cursor = connection.cursor()

    # Insert data into Clinic
    clinics = [
        ('C001', 'Pawsome Pets Miami', '1234 Elm Street, Miami, FL', '(305)-555-1234'),
        ('C002', 'Pawsome Pets Orlando', '5678 Oak Avenue, Orlando, FL', '(407)-555-5678'),
        ('C003', 'Pawsome Pets Tampa', '9101 Pine Lane, Tampa, FL', '(813)-555-9101'),
        ('C004', 'Pawsome Pets Jacksonville', '2233 Maple Drive, Jacksonville, FL', '(904)-555-2233'),
        ('C005', 'Pawsome Pets Fort Lauderdale', '3344 Birch Boulevard, Fort Lauderdale, FL', '(754)-555-3344')
    ]
    cursor.executemany("INSERT INTO Clinic VALUES (?, ?, ?, ?);", clinics)

    # Insert data into Staff
    staff = [
        ('S001', 'C001', 'Alice Johnson', '135 Spruce St, Miami, FL', '(305)-555-2001', '1985-03-15', 'Veterinarian', 85000.00),
        ('S002', 'C002', 'Bob Smith', '246 Willow Rd, Orlando, FL', '(407)-555-3002', '1990-06-20', 'Technician', 55000.00),
        ('S003', 'C003', 'Charlie Brown', '357 Aspen Way, Tampa, FL', '(813)-555-4003', '1980-09-25', 'Receptionist', 40000.00),
        ('S004', 'C004', 'Dana White', '468 Cedar Ct, Jacksonville, FL', '(904)-555-5004', '1975-12-10', 'Manager', 60000.00),
        ('S005', 'C005', 'Eve Black', '579 Alder Cir, Fort Lauderdale, FL', '(754)-555-6005', '1995-01-30', 'Veterinarian', 90000.00)
    ]
    cursor.executemany("INSERT INTO Staff VALUES (?, ?, ?, ?, ?, ?, ?, ?);", staff)

    # Insert data into Owner
    owners = [
        ('O001', 'Michael Green', '741 Palm Dr, Miami, FL', '(305)-555-7410'),
        ('O002', 'Laura Blue', '852 Cypress Ln, Orlando, FL', '(407)-555-8521'),
        ('O003', 'James Red', '963 Maple St, Tampa, FL', '(813)-555-9632'),
        ('O004', 'Sophia White', '174 Oak Ct, Jacksonville, FL', '(904)-555-1743'),
        ('O005', 'Emma Gold', '285 Birch Blvd, Fort Lauderdale, FL', '(754)-555-2854')
    ]
    cursor.executemany("INSERT INTO Owner VALUES (?, ?, ?, ?);", owners)

    # Insert data into Pet
    pets = [
        ('P001', 'O001', 'C001', 'Buddy', '2020-05-10', 'Dog', 'Labrador', 'Yellow'),
        ('P002', 'O002', 'C002', 'Kitty', '2018-11-22', 'Cat', 'Siamese', 'Cream'),
        ('P003', 'O003', 'C003', 'Max', '2021-02-14', 'Dog', 'Golden Retriever', 'Golden'),
        ('P004', 'O004', 'C004', 'Bella', '2019-08-09', 'Dog', 'Bulldog', 'White'),
        ('P005', 'O005', 'C005', 'Luna', '2022-01-17', 'Cat', 'Maine Coon', 'Brown')
    ]
    cursor.executemany("INSERT INTO Pet VALUES (?, ?, ?, ?, ?, ?, ?, ?);", pets)

    # Insert data into Examination
    examinations = [
        ('E001', 'P001', 'S001', 'Coughing', 'Physical exam and X-ray performed.', '2024-11-01', 'Prescribed cough suppressant.'),
        ('E002', 'P002', 'S002', 'Skin Rash', 'Dermatological tests conducted.', '2024-11-05', 'Applied topical ointment.'),
        ('E003', 'P003', 'S003', 'Loss of appetite', 'Blood test and urine analysis performed.', '2024-11-10', 'Recommended special diet.'),
        ('E004', 'P004', 'S004', 'Limping', 'Physical exam and X-ray performed.', '2024-11-15', 'Applied bandage and prescribed painkillers.'),
        ('E005', 'P005', 'S005', 'Hair Loss', 'Complete examination and allergy tests.', '2024-11-20', 'Prescribed anti-allergic shampoo.')
    ]
    cursor.executemany("INSERT INTO Examination VALUES (?, ?, ?, ?, ?, ?, ?);", examinations)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    insert_data()
    print("Data inserted successfully.")


##Question c
connection = sqlite3.connect("dbms_project.db")

def register_pet(petNo, ownerNo, clinicNo, name, DOB, species, breed, color):
    """Transaction 1: Register a new pet for a specific owner at a clinic"""
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO Pet (petNo, ownerNo, clinicNo, name, DOB, species, breed, color)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (petNo, ownerNo, clinicNo, name, DOB, species, breed, color))
    connection.commit()
    print(f"Pet {name} registered successfully.")

def assign_staff_to_exam(examNo, petNo, staffNo, complaint, description, examDate, actionsTaken):
    """Transaction 2: Assign a staff member to conduct an examination for a pet"""
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO Examination (examNo, petNo, staffNo, complaint, description, examDate, actionsTaken)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (examNo, petNo, staffNo, complaint, description, examDate, actionsTaken))
    connection.commit()
    print(f"Examination {examNo} assigned successfully.")

def update_owner_contact(ownerNo, address, telephoneNo):
    """Transaction 3: Update contact details for an owner"""
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE Owner
        SET address = ?, telephoneNo = ?
        WHERE ownerNo = ?
    """, (address, telephoneNo, ownerNo))
    connection.commit()
    print(f"Owner {ownerNo}'s contact information updated successfully.")

def get_pets_by_clinic(clinicNo):
    """Transaction 4: Retrieve all pets registered to a specific clinic"""
    cursor = connection.cursor()
    cursor.execute("""
        SELECT petNo, name, DOB, species, breed, color
        FROM Pet
        WHERE clinicNo = ?
    """, (clinicNo,))
    pets = cursor.fetchall()
    print(f"Pets registered in clinic {clinicNo}:")
    for pet in pets:
        print(pet)

def list_examinations_by_staff(staffNo):
    """Transaction 5: List all examinations conducted by a specific staff member"""
    cursor = connection.cursor()
    cursor.execute("""
        SELECT examNo, petNo, complaint, description, examDate, actionsTaken
        FROM Examination
        WHERE staffNo = ?
    """, (staffNo,))
    examinations = cursor.fetchall()
    print(f"Examinations conducted by staff {staffNo}:")
    for exam in examinations:
        print(exam)

# Example usage of the functions
if __name__ == "__main__":
    # Transaction 1
    register_pet('P006', 'O002', 'C002', 'Snowy', '2023-03-01', 'Dog', 'Husky', 'White')

    # Transaction 2
    assign_staff_to_exam('E006', 'P006', 'S002', 'Eye Infection', 'Eye check and cleaning', '2024-12-01', 'Prescribed eye drops.')

    # Transaction 3
    update_owner_contact('O002', '999 Blue Street, Orlando, FL', '(407)-555-9999')

    # Transaction 4
    get_pets_by_clinic('C002')

    # Transaction 5
    list_examinations_by_staff('S002')

# Close the connection
connection.close()
