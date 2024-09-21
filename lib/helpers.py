from .models import Session, Client, Policy, Reminder
from sqlalchemy import func
from datetime import datetime, timedelta

# Policy Management Functions

def add_policy(session, client_id, policy_number, policy_type, start_date, end_date, premium_amount):
    """
    Add a new policy to the database.
    
    :param session: SQLAlchemy database session
    :param client_id: ID of the client associated with the policy
    :param policy_number: Unique identifier for the policy
    :param policy_type: Type of insurance policy
    :param start_date: Start date of the policy
    :param end_date: End date of the policy
    :param premium_amount: Annual premium amount for the policy
    :return: Newly created Policy object
    """
    new_policy = Policy(
        client_id=client_id,
        policy_number=policy_number,
        type=policy_type,
        start_date=start_date,
        end_date=end_date,
        premium_amount=premium_amount
    )
    session.add(new_policy)
    session.commit()
    return new_policy

def get_policy(session, policy_id):
    """
    Retrieve a policy by its ID.
    
    :param session: SQLAlchemy database session
    :param policy_id: ID of the policy to retrieve
    :return: Policy object if found, None otherwise
    """
    return session.query(Policy).get(policy_id)

def list_policies(session):
    """
    Retrieve all policies from the database.
    
    :param session: SQLAlchemy database session
    :return: List of all Policy objects
    """
    return session.query(Policy).all()

def update_policy(session, policy_id, **kwargs):
    """
    Update an existing policy in the database.
    
    :param session: SQLAlchemy database session
    :param policy_id: ID of the policy to update
    :param kwargs: Dictionary of fields to update
    :return: Updated Policy object if found, None otherwise
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
    
    :param session: SQLAlchemy database session
    :param policy_id: ID of the policy to delete
    :return: True if policy was deleted, False otherwise
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
    
    :param session: SQLAlchemy database session
    :param name: Name of the client
    :param email: Email address of the client
    :param phone: Phone number of the client
    :param address: Physical address of the client
    :return: Newly created Client object
    """
    new_client = Client(name=name, email=email, phone=phone, address=address)
    session.add(new_client)
    session.commit()
    return new_client

def get_client(session, client_id):
    """
    Retrieve a client by their ID.
    
    :param session: SQLAlchemy database session
    :param client_id: ID of the client to retrieve
    :return: Client object if found, None otherwise
    """
    return session.query(Client).get(client_id)

def list_clients(session):
    """
    Retrieve all clients from the database.
    
    :param session: SQLAlchemy database session
    :return: List of all Client objects
    """
    return session.query(Client).all()

def update_client(session, client_id, **kwargs):
    """
    Update an existing client in the database.
    
    :param session: SQLAlchemy database session
    :param client_id: ID of the client to update
    :param kwargs: Dictionary of fields to update
    :return: Updated Client object if found, None otherwise
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
    
    :param session: SQLAlchemy database session
    :param client_id: ID of the client to delete
    :return: True if client was deleted, False otherwise
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
    
    :param session: SQLAlchemy database session
    """
    three_months_from_now = datetime.now().date() + timedelta(days=90)
    policies_to_remind = session.query(Policy).filter(Policy.end_date <= three_months_from_now).all()
    
    for policy in policies_to_remind:
        # Check if a reminder already exists for this policy
        existing_reminder = session.query(Reminder).filter_by(policy_id=policy.id, status='pending').first()
        if not existing_reminder:
            # Create a reminder for each policy expiring within 3 months
            reminder = Reminder(policy_id=policy.id, reminder_date=datetime.now().date(), status='pending')
            session.add(reminder)
    
    session.commit()

def list_reminders(session):
    """
    Retrieve all pending reminders from the database.
    
    :param session: SQLAlchemy database session
    :return: List of all pending Reminder objects
    """
    return session.query(Reminder).filter(Reminder.status == 'pending').all()

def update_reminder_status(session, reminder_id, new_status):
    """
    Update the status of a reminder.
    
    :param session: SQLAlchemy database session
    :param reminder_id: ID of the reminder to update
    :param new_status: New status for the reminder ('pending', 'sent', or 'acknowledged')
    :return: Updated Reminder object if found, None otherwise
    """
    reminder = session.query(Reminder).get(reminder_id)
    if reminder:
        reminder.status = new_status
        session.commit()
    return reminder

# Utility Functions

def get_expiring_policies(session, days=90):
    """
    Retrieve policies expiring within the specified number of days.
    
    :param session: SQLAlchemy database session
    :param days: Number of days to look ahead (default: 90)
    :return: List of Policy objects expiring within the specified period
    """
    expiry_date = datetime.now().date() + timedelta(days=days)
    return session.query(Policy).filter(Policy.end_date <= expiry_date).all()

def get_client_policies(session, client_id):
    """
    Retrieve all policies associated with a specific client.
    
    :param session: SQLAlchemy database session
    :param client_id: ID of the client
    :return: List of Policy objects associated with the client
    """
    return session.query(Policy).filter_by(client_id=client_id).all()

def get_policy_reminders(session, policy_id):
    """
    Retrieve all reminders associated with a specific policy.
    
    :param session: SQLAlchemy database session
    :param policy_id: ID of the policy
    :return: List of Reminder objects associated with the policy
    """
    return session.query(Reminder).filter_by(policy_id=policy_id).all()