#!/usr/bin/python3
import requests
import sys

def fetch_employee_todo_progress(employee_id):
    # Define the base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Define the endpoints for users and todos
    users_endpoint = '/users'
    todos_endpoint = '/todos'

    # Build the complete URLs for the users and todos resources
    users_url = f"{base_url}{users_endpoint}/{employee_id}"
    todos_url = f"{base_url}{todos_endpoint}"

    try:
        # Fetch user data
        response_user = requests.get(users_url)
        response_user.raise_for_status()
        user_data = response_user.json()

        # Fetch todo data for the user
        response_todos = requests.get(todos_url, params={'userId': employee_id})
        response_todos.raise_for_status()
        todos_data = response_todos.json()

        # Extract user information
        employee_name = user_data['name']

        # Count completed and total tasks
        completed_tasks = [todo for todo in todos_data if todo['completed']]
        total_tasks = len(todos_data)
        completed_task_count = len(completed_tasks)

        # Display the progress
        print(f"Employee {employee_name} is done with tasks({completed_task_count}/{total_tasks}):")
        for todo in completed_tasks:
            print(f"    {todo['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
