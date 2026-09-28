import json
import os
from datetime import datetime

DATA_FILE = "data.json"


# -----------------------------
# Load Data
# -----------------------------
def load_data():
    if not os.path.exists(DATA_FILE):
        return {
            "services": [],
            "programs": [],
            "trainings": [],
            "internships": [],
            "inquiries": [],
            "requests": []
        }

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except:
        return {
            "services": [],
            "programs": [],
            "trainings": [],
            "internships": [],
            "inquiries": [],
            "requests": []
        }


# -----------------------------
# Save Data
# -----------------------------
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# -----------------------------
# Generate ID
# -----------------------------
def generate_id(items):
    if not items:
        return 1

    return max(item["id"] for item in items) + 1


# -----------------------------
# Add Service
# -----------------------------
def add_service(data):
    print("\n--- Add Digital Service ---")

    name = input("Service name: ")
    description = input("Description: ")
    price = input("Price: ")

    service = {
        "id": generate_id(data["services"]),
        "name": name,
        "description": description,
        "price": price,
        "created_at": datetime.now().strftime("%Y-%m-%d")
    }

    data["services"].append(service)
    save_data(data)

    print("Service added successfully!")


# -----------------------------
# View Services
# -----------------------------
def view_services(data):
    print("\n--- Digital Services ---")

    if not data["services"]:
        print("No services available.")
        return

    for service in data["services"]:
        print("\nID:", service["id"])
        print("Name:", service["name"])
        print("Description:", service["description"])
        print("Price:", service["price"])
        print("Created:", service["created_at"])


# -----------------------------
# Add Technology Program
# -----------------------------
def add_program(data):
    print("\n--- Add Technology Program ---")

    name = input("Program name: ")
    duration = input("Duration: ")
    description = input("Description: ")

    program = {
        "id": generate_id(data["programs"]),
        "name": name,
        "duration": duration,
        "description": description
    }

    data["programs"].append(program)
    save_data(data)

    print("Technology program added successfully!")


# -----------------------------
# View Technology Programs
# -----------------------------
def view_programs(data):
    print("\n--- Technology Programs ---")

    if not data["programs"]:
        print("No programs available.")
        return

    for program in data["programs"]:
        print("\nID:", program["id"])
        print("Name:", program["name"])
        print("Duration:", program["duration"])
        print("Description:", program["description"])


# -----------------------------
# Add Training Program
# -----------------------------
def add_training(data):
    print("\n--- Add Training Program ---")

    name = input("Training name: ")
    duration = input("Duration: ")
    trainer = input("Trainer name: ")

    training = {
        "id": generate_id(data["trainings"]),
        "name": name,
        "duration": duration,
        "trainer": trainer
    }

    data["trainings"].append(training)
    save_data(data)

    print("Training program added successfully!")


# -----------------------------
# View Training Programs
# -----------------------------
def view_trainings(data):
    print("\n--- Training Programs ---")

    if not data["trainings"]:
        print("No training programs available.")
        return

    for training in data["trainings"]:
        print("\nID:", training["id"])
        print("Name:", training["name"])
        print("Duration:", training["duration"])
        print("Trainer:", training["trainer"])


# -----------------------------
# Add Internship
# -----------------------------
def add_internship(data):
    print("\n--- Add Internship Program ---")

    title = input("Internship title: ")
    duration = input("Duration: ")
    skills = input("Required skills: ")

    internship = {
        "id": generate_id(data["internships"]),
        "title": title,
        "duration": duration,
        "skills": skills
    }

    data["internships"].append(internship)
    save_data(data)

    print("Internship added successfully!")


# -----------------------------
# View Internships
# -----------------------------
def view_internships(data):
    print("\n--- Internship Programs ---")

    if not data["internships"]:
        print("No internships available.")
        return

    for internship in data["internships"]:
        print("\nID:", internship["id"])
        print("Title:", internship["title"])
        print("Duration:", internship["duration"])
        print("Skills:", internship["skills"])


# -----------------------------
# Add Customer Inquiry
# -----------------------------
def add_inquiry(data):
    print("\n--- Customer Inquiry ---")

    name = input("Customer name: ")
    email = input("Email: ")
    subject = input("Subject: ")
    message = input("Message: ")

    inquiry = {
        "id": generate_id(data["inquiries"]),
        "customer_name": name,
        "email": email,
        "subject": subject,
        "message": message,
        "status": "New",
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    data["inquiries"].append(inquiry)
    save_data(data)

    print("Customer inquiry added successfully!")


# -----------------------------
# View Inquiries
# -----------------------------
def view_inquiries(data):
    print("\n--- Customer Inquiries ---")

    if not data["inquiries"]:
        print("No customer inquiries.")
        return

    for inquiry in data["inquiries"]:
        print("\nID:", inquiry["id"])
        print("Customer:", inquiry["customer_name"])
        print("Email:", inquiry["email"])
        print("Subject:", inquiry["subject"])
        print("Message:", inquiry["message"])
        print("Status:", inquiry["status"])
        print("Date:", inquiry["date"])


# -----------------------------
# Add Service Request
# -----------------------------
def add_request(data):
    print("\n--- Service Request ---")

    customer = input("Customer name: ")
    service = input("Service required: ")
    description = input("Request description: ")

    request = {
        "id": generate_id(data["requests"]),
        "customer": customer,
        "service": service,
        "description": description,
        "status": "Pending",
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    data["requests"].append(request)
    save_data(data)

    print("Service request added successfully!")


# -----------------------------
# View Service Requests
# -----------------------------
def view_requests(data):
    print("\n--- Service Requests ---")

    if not data["requests"]:
        print("No service requests.")
        return

    for request in data["requests"]:
        print("\nID:", request["id"])
        print("Customer:", request["customer"])
        print("Service:", request["service"])
        print("Description:", request["description"])
        print("Status:", request["status"])
        print("Date:", request["date"])


# -----------------------------
# Search Services
# -----------------------------
def search_services(data):
    print("\n--- Search Services ---")

    keyword = input("Enter service name or keyword: ").lower()

    found = False

    for service in data["services"]:
        if (
            keyword in service["name"].lower()
            or keyword in service["description"].lower()
        ):
            print("\nID:", service["id"])
            print("Name:", service["name"])
            print("Description:", service["description"])
            print("Price:", service["price"])

            found = True

    if not found:
        print("No matching service found.")


# -----------------------------
# Business Report
# -----------------------------
def business_report(data):
    print("\n================================")
    print("     VEDA TECHNOLOGY REPORT")
    print("================================")

    print("Digital Services :", len(data["services"]))
    print("Technology Programs:", len(data["programs"]))
    print("Training Programs :", len(data["trainings"]))
    print("Internships       :", len(data["internships"]))
    print("Customer Inquiries:", len(data["inquiries"]))
    print("Service Requests  :", len(data["requests"]))

    pending = 0
    completed = 0

    for request in data["requests"]:
        if request["status"] == "Pending":
            pending += 1
        elif request["status"] == "Completed":
            completed += 1

    print("\nPending Requests  :", pending)
    print("Completed Requests:", completed)

    print("================================")


# -----------------------------
# Main Menu
# -----------------------------
def main():
    data = load_data()

    while True:

        print("\n")
        print("==============================================")
        print(" VEDA TECHNOLOGY BUSINESS & SERVICE SYSTEM")
        print("==============================================")

        print("1. Add Digital Service")
        print("2. View Digital Services")
        print("3. Add Technology Program")
        print("4. View Technology Programs")
        print("5. Add Training Program")
        print("6. View Training Programs")
        print("7. Add Internship")
        print("8. View Internships")
        print("9. Add Customer Inquiry")
        print("10. View Customer Inquiries")
        print("11. Add Service Request")
        print("12. View Service Requests")
        print("13. Search Services")
        print("14. Business Report")
        print("15. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_service(data)

        elif choice == "2":
            view_services(data)

        elif choice == "3":
            add_program(data)

        elif choice == "4":
            view_programs(data)

        elif choice == "5":
            add_training(data)

        elif choice == "6":
            view_trainings(data)

        elif choice == "7":
            add_internship(data)

        elif choice == "8":
            view_internships(data)

        elif choice == "9":
            add_inquiry(data)

        elif choice == "10":
            view_inquiries(data)

        elif choice == "11":
            add_request(data)

        elif choice == "12":
            view_requests(data)

        elif choice == "13":
            search_services(data)

        elif choice == "14":
            business_report(data)

        elif choice == "15":
            print("\nThank you for using Veda Technology System!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 15.")


# -----------------------------
# Start Program
# -----------------------------
if __name__ == "__main__":
    main()