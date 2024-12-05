import sqlite3

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
