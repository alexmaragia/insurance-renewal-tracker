import click
from .models import Session
from .helpers import (
    add_policy, get_policy, list_policies, update_policy, delete_policy,
    add_client, get_client, list_clients, update_client, delete_client,
    generate_reminders, list_reminders, get_expiring_policies
)
from datetime import datetime

# Using tuples for menu
MAIN_MENU_OPTIONS = (
    "Manage Policies",
    "Manage Clients",
    "Manage Reminders"
)

POLICIES_MENU_OPTIONS = (
    "Add Policy",
    "View Policy",
    "List Policies",
    "Update Policy",
    "Delete Policy"
)

CLIENTS_MENU_OPTIONS = (
    "Add Client",
    "View Client",
    "List Clients",
    "Update Client",
    "Delete Client"
)

REMINDERS_MENU_OPTIONS = (
    "Generate Reminders",
    "List Reminders",
    "View Expiring Policies"
)

def print_menu(options):
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    print("0. Go back/Exit")

def get_user_choice(max_choice):
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 0 <= choice <= max_choice:
                return choice
            else:
                print(f"Please enter a number between 0 and {max_choice}")
        except ValueError:
            print("Please enter a valid number")

def policies_menu(session):
    while True:
        print("\n--- Policies Menu ---")
        print_menu(POLICIES_MENU_OPTIONS)
        choice = get_user_choice(len(POLICIES_MENU_OPTIONS))

        if choice == 0:
            break
        elif choice == 1:
            # add policy
            # using a dictionary to collect policy data
            policy_data = {
                'client_id': int(input("Enter client ID: ")),
                'policy_number': input("Enter policy number: "),
                'type': input("Enter policy type: "),
                'start_date': datetime.strptime(input("Enter start date (YYYY-MM-DD): "), "%Y-%m-%d").date(),
                'end_date': datetime.strptime(input("Enter end date (YYYY-MM-DD): "), "%Y-%m-%d").date(),
                'premium_amount': float(input("Enter premium amount: ")),
                'insurance_company': input("Enter insurance company: ")
            }
            new_policy = add_policy(session, **policy_data)
            print(f"Added new policy: {new_policy}")
        elif choice == 2:
            # view policy
            policy_id = int(input("Enter policy ID: "))
            policy = get_policy(session, policy_id)
            if policy:
                # using a dictionary to display policy details
                policy_details = {
                    'ID': policy.id,
                    'Number': policy.policy_number,
                    'Type': policy.type,
                    'Start Date': policy.start_date,
                    'End Date': policy.end_date,
                    'Premium': policy.premium_amount,
                    'Insurance Company': policy.insurance_company
                }
                for key, value in policy_details.items():
                    print(f"{key}: {value}")
            else:
                print("Policy not found")
        elif choice == 3:
            # list policies
            policies = list_policies(session)
            # using a list comprehension to format policy information
            policy_list = [f"ID: {p.id}, Number: {p.policy_number}, Type: {p.type}" for p in policies]
            for policy_info in policy_list:
                print(policy_info)
        elif choice == 4:
            # Update Policy
            policy_id = int(input("Enter policy ID to update: "))
            field = input("Enter field to update (type/start_date/end_date/premium_amount/insurance_company): ")
            value = input("Enter new value: ")
            updated_policy = update_policy(session, policy_id, **{field: value})
            print(f"Updated policy: {updated_policy}")
        elif choice == 5:
            # Delete Policy
            policy_id = int(input("Enter policy ID to delete: "))
            if delete_policy(session, policy_id):
                print("Policy deleted successfully")
            else:
                print("Policy not found")

def clients_menu(session):
    while True:
        print("\n--- Clients Menu ---")
        print_menu(CLIENTS_MENU_OPTIONS)
        choice = get_user_choice(len(CLIENTS_MENU_OPTIONS))

        if choice == 0:
            break
        elif choice == 1:
            # Add Client
            # Using a dictionary to collect client data
            client_data = {
                'name': input("Enter client name: "),
                'email': input("Enter client email: "),
                'phone': input("Enter client phone: "),
                'address': input("Enter client address: ")
            }
            new_client = add_client(session, **client_data)
            print(f"Added new client: {new_client}")
        elif choice == 2:
            # View Client
            client_id = int(input("Enter client ID: "))
            client = get_client(session, client_id)
            if client:
                # Using a dictionary to display client details
                client_details = {
                    'ID': client.id,
                    'Name': client.name,
                    'Email': client.email,
                    'Phone': client.phone,
                    'Address': client.address
                }
                for key, value in client_details.items():
                    print(f"{key}: {value}")
            else:
                print("Client not found")
        elif choice == 3:
            # List Clients
            clients = list_clients(session)
            # Using a list comprehension to format client information
            client_list = [f"ID: {c.id}, Name: {c.name}, Email: {c.email}" for c in clients]
            for client_info in client_list:
                print(client_info)
        elif choice == 4:
            # Update Client
            client_id = int(input("Enter client ID to update: "))
            field = input("Enter field to update (name/email/phone/address): ")
            value = input("Enter new value: ")
            updated_client = update_client(session, client_id, **{field: value})
            print(f"Updated client: {updated_client}")
        elif choice == 5:
            # Delete Client
            client_id = int(input("Enter client ID to delete: "))
            if delete_client(session, client_id):
                print("Client deleted successfully")
            else:
                print("Client not found")

def reminders_menu(session):
    while True:
        print("\n--- Reminders Menu ---")
        print_menu(REMINDERS_MENU_OPTIONS)
        choice = get_user_choice(len(REMINDERS_MENU_OPTIONS))

        if choice == 0:
            break
        elif choice == 1:
            # Generate Reminders
            generate_reminders(session)
            print("Reminders generated successfully")
        elif choice == 2:
            # List Reminders
            reminders = list_reminders(session)
            # Using a list comprehension to format reminder information
            reminder_list = [f"ID: {r.id}, Policy ID: {r.policy_id}, Date: {r.reminder_date}, Status: {r.status}" for r in reminders]
            for reminder_info in reminder_list:
                print(reminder_info)
        elif choice == 3:
            # View Expiring Policies
            days = int(input("Enter number of days to look ahead: "))
            policies = get_expiring_policies(session, days)
            # Using a list comprehension to format expiring policy information
            expiring_policies = [f"Policy ID: {p.id}, Number: {p.policy_number}, Expiry Date: {p.end_date}" for p in policies]
            for policy_info in expiring_policies:
                print(policy_info)

def main_menu():
    session = Session()
    try:
        while True:
            print("\n--- Insurance Renewal Tracker ---")
            print_menu(MAIN_MENU_OPTIONS)
            choice = get_user_choice(len(MAIN_MENU_OPTIONS))

            if choice == 0:
                print("Goodbye!")
                break
            elif choice == 1:
                policies_menu(session)
            elif choice == 2:
                clients_menu(session)
            elif choice == 3:
                reminders_menu(session)
    finally:
        session.close()

if __name__ == '__main__':
    main_menu()