from .models import Client, Policy, Reminder
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timedelta

# Policy Management Functions

def add_policy(session, client_id, policy_number, policy_type, start_date, end_date, premium_amount, insurance_company):
    """
    Add a new policy to the database.
    """
    try:
        new_policy = Policy(
            client_id=client_id,
            policy_number=policy_number,
            type=policy_type,
            start_date=start_date,
            end_date=end_date,
            premium_amount=premium_amount,
            insurance_company=insurance_company
        )
        session.add(new_policy)
        session.commit()
        return new_policy
    except SQLAlchemyError as e:
        session.rollback()
        raise Exception(f"Database error: {str(e)}")

def get_policy(session, policy_id):
    """
    Retrieve a policy by its ID.
    """
    return session.query(Policy).get(policy_id)

def list_policies(session):
    """
    Retrieve all policies from the database.
    """
    return session.query(Policy).all()

def update_policy(session, policy_id, **kwargs):
    """
    Update an existing policy in the database.
    """
    policy = get_policy(session, policy_id)
    if policy:
        for key, value in kwargs.items():
            setattr(policy, key, value)
        session.commit()
    return policy

def delete_policy(session, policy_id):
    """
    Delete a policy from the database.
    """
    policy = get_policy(session, policy_id)
    if policy:
        session.delete(policy)
        session.commit()
        return True
    return False

# Client Management Functions

def add_client(session, name, email, phone, address):
    """
    Add a new client to the database.
    """
    try:
        new_client = Client(name=name, email=email, phone=phone, address=address)
        session.add(new_client)
        session.commit()
        return new_client
    except SQLAlchemyError as e:
        session.rollback()
        raise Exception(f"Database error: {str(e)}")

def get_client(session, client_id):
    """
    Retrieve a client by their ID.
    """
    return session.query(Client).get(client_id)

def list_clients(session):
    """
    Retrieve all clients from the database.
    """
    return session.query(Client).all()

def update_client(session, client_id, **kwargs):
    """
    Update an existing client in the database.
    """
    client = get_client(session, client_id)
    if client:
        for key, value in kwargs.items():
            setattr(client, key, value)
        session.commit()
    return client

def delete_client(session, client_id):
    """
    Delete a client from the database.
    """
    client = get_client(session, client_id)
    if client:
        session.delete(client)
        session.commit()
        return True
    return False

# Reminder Management Functions

def generate_reminders(session):
    """
    Generate reminders for policies expiring within the next 3 months.
    """
    three_months_from_now = datetime.now().date() + timedelta(days=90)
    policies_to_remind = session.query(Policy).filter(Policy.end_date <= three_months_from_now).all()
    
    for policy in policies_to_remind:
        existing_reminder = session.query(Reminder).filter_by(policy_id=policy.id, status='pending').first()
        if not existing_reminder:
            reminder = Reminder(policy_id=policy.id, reminder_date=datetime.now().date(), status='pending')
            session.add(reminder)
    
    session.commit()

def list_reminders(session):
    """
    Retrieve all pending reminders from the database.
    """
    return session.query(Reminder).filter(Reminder.status == 'pending').all()

def get_expiring_policies(session, days=90):
    """
    Retrieve policies expiring within the specified number of days.
    """
    expiry_date = datetime.now().date() + timedelta(days=days)
    return session.query(Policy).filter(Policy.end_date <= expiry_date).all()

# Utility Functions

def get_client_policies(session, client_id):
    """
    Retrieve all policies associated with a specific client.
    """
    return session.query(Policy).filter_by(client_id=client_id).all()

def get_policy_reminders(session, policy_id):
    """
    Retrieve all reminders associated with a specific policy.
    """
    return session.query(Reminder).filter_by(policy_id=policy_id).all()