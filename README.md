# Insurance Renewal Tracker CLI

## Overview

The Insurance Renewal Tracker CLI is a command-line interface application designed to help insurance brokers and agents manage policy renewals, client information, and reminders. This tool aims to improve client retention and streamline the process of tracking policy expirations.

## Features

- Policy Management: Add, view, list, update, and delete insurance policies
- Client Management: Add, view, list, update, and delete client information
- Reminder System: Generate reminders for policies expiring within 3 months
- Expiring Policies Report: View policies expiring within a specified timeframe

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-username/insurance-renewal-tracker.git
   cd insurance-renewal-tracker
   ```

2. Set up a virtual environment:
   ```
   pipenv install
   pipenv shell
   ```

3. Install dependencies:
   ```
   pipenv install sqlalchemy alembic click faker
   ```

4. Set up the database:
   ```
   alembic upgrade head
   ```

5. (Optional) Seed the database with sample data:
   ```
   python -m lib.db.seed
   ```

## Usage

To start the CLI, run:

```
python -m lib.cli
```

This will launch the main menu of the Insurance Renewal Tracker CLI.

### Main Menu

The main menu offers the following options:

1. Manage Policies
2. Manage Clients
3. Manage Reminders
0. Exit

Enter the number corresponding to your choice and press Enter.

### Policies Menu

In the Policies menu, you can:

1. Add Policy: Enter policy details to create a new policy
2. View Policy: View details of a specific policy by ID
3. List Policies: Display all policies in the system
4. Update Policy: Modify details of an existing policy
5. Delete Policy: Remove a policy from the system
0. Go back to the main menu

### Clients Menu

In the Clients menu, you can:

1. Add Client: Enter client details to create a new client record
2. View Client: View details of a specific client by ID
3. List Clients: Display all clients in the system
4. Update Client: Modify details of an existing client
5. Delete Client: Remove a client from the system
0. Go back to the main menu

### Reminders Menu

In the Reminders menu, you can:

1. Generate Reminders: Create reminders for policies expiring within 3 months
2. List Reminders: Display all pending reminders
3. View Expiring Policies: Show policies expiring within a specified number of days
0. Go back to the main menu

## Functions Workflow

### Policy Management

- `add_policy(session, **policy_data)`: Adds a new policy to the database
- `get_policy(session, policy_id)`: Retrieves a specific policy by ID
- `list_policies(session)`: Retrieves all policies from the database
- `update_policy(session, policy_id, **kwargs)`: Updates an existing policy
- `delete_policy(session, policy_id)`: Deletes a policy from the database

### Client Management

- `add_client(session, **client_data)`: Adds a new client to the database
- `get_client(session, client_id)`: Retrieves a specific client by ID
- `list_clients(session)`: Retrieves all clients from the database
- `update_client(session, client_id, **kwargs)`: Updates an existing client
- `delete_client(session, client_id)`: Deletes a client from the database

### Reminder Management

- `generate_reminders(session)`: Generates reminders for policies expiring within 3 months
- `list_reminders(session)`: Retrieves all pending reminders
- `get_expiring_policies(session, days)`: Retrieves policies expiring within the specified number of days

## Data Structures

The CLI utilizes various Python data structures:

- **Tuples**: Used for storing menu options
- **Dictionaries**: Used for collecting and displaying policy and client data
- **Lists and List Comprehensions**: Used for formatting and displaying policy, client, and reminder information

## Dependencies

- SQLAlchemy: ORM for database operations
- Alembic: Database migration tool
- Click: CLI framework
- Faker: Generating sample data

## Contributing

Contributions to the Insurance Renewal Tracker CLI are welcome. Please ensure to follow the existing code style and add unit tests for any new features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
Alex Maragia - maragialex@gmail.com
Project Link: [[(https://github.com/alexmaragia/insurance-renewal-tracker.git)](https://github.com/alexmaragia/insurance-renewal-tracker.git)]