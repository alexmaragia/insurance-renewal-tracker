from ..models import Session, Client, Policy, Reminder
from ..helpers import generate_reminders
from faker import Faker
from datetime import datetime, timedelta
import random

# Initialize Faker with default locale
fake = Faker()

# Kenyan-specific data
kenyan_cities = ['Nairobi', 'Mombasa', 'Kisumu', 'Nakuru', 'Eldoret', 'Thika', 'Malindi', 'Kitale', 'Garissa', 'Kakamega']
kenyan_names = ['Kamau', 'Ochieng', 'Wanjiru', 'Muthomi', 'Otieno', 'Ngugi', 'Akinyi', 'Mutua', 'Ouko', 'Njeri']
kenyan_phone_prefixes = ['070', '071', '072', '074', '075', '076', '077', '078', '079']

policy_types = [
    'Motor Vehicle Insurance',
    'Health Insurance',
    'Property Insurance',
    'Life Insurance',
    'Business Insurance',
    'Travel Insurance'
]

insurance_companies = [
    'Jubilee Insurance',
    'APA Insurance',
    'Britam',
    'CIC Insurance Group',
    'UAP Old Mutual',
    'Kenya Orient Insurance',
    'Madison Insurance'
]

def generate_kenyan_phone():
    return f"{random.choice(kenyan_phone_prefixes)}{fake.numerify('#######')}"

def generate_kenyan_name():
    return f"{fake.first_name()} {random.choice(kenyan_names)}"

def generate_kenyan_address():
    return f"{fake.street_address()}, {random.choice(kenyan_cities)}, Kenya"

def seed_data():
    """
    Seed the database with sample data for testing purposes.
    This function creates sample clients, policies, and generates reminders
    in a Kenyan insurance context.
    """
    session = Session()

    try:
        # Create sample clients
        clients = create_sample_clients(session)

        # Create sample policies for each client
        create_sample_policies(session, clients)

        # Generate reminders for policies
        generate_reminders(session)

        print("Sample data seeded successfully.")
    except Exception as e:
        print(f"An error occurred while seeding data: {str(e)}")
        session.rollback()
    finally:
        session.close()

def create_sample_clients(session, num_clients=10):
    """
    Create and add sample clients to the database.
    
    :param session: SQLAlchemy database session
    :param num_clients: Number of sample clients to create
    :return: List of created Client objects
    """
    clients = []
    for _ in range(num_clients):
        client = Client(
            name=generate_kenyan_name(),
            email=fake.email(),
            phone=generate_kenyan_phone(),
            address=generate_kenyan_address()
        )
        session.add(client)
        clients.append(client)
    
    session.commit()
    return clients

def create_sample_policies(session, clients):
    """
    Create and add sample policies for each client.
    
    :param session: SQLAlchemy database session
    :param clients: List of Client objects to associate policies with
    """
    for client in clients:
        # Create 1 to 3 policies for each client
        for _ in range(random.randint(1, 3)):
            # Generate realistic policy details
            policy_type = random.choice(policy_types)
            start_date = fake.date_between(start_date='-2y', end_date='today')
            end_date = start_date + timedelta(days=365)  # Policies typically last one year
            
            policy = Policy(
                client_id=client.id,
                policy_number=f"KE-{fake.unique.random_number(digits=8)}",
                type=policy_type,
                start_date=start_date,
                end_date=end_date,
                premium_amount=round(random.uniform(5000, 100000), 2),  # Premium in Kenyan Shillings
                insurance_company=random.choice(insurance_companies)
            )
            session.add(policy)
    
    session.commit()

if __name__ == '__main__':
    seed_data()