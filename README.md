# Study Task Manager

## Overview

Study Task Manager is a web application built with Python and Django that helps students organize their study tasks. Users can add tasks, view task details, mark tasks as completed or pending, and delete tasks when they are no longer needed.

The application uses a SQLite database to store task information, so tasks can remain saved when the user leaves the page and returns later.

## Features

- Add a study task with a title, description, and optional due date.
- View all saved tasks on the home page.
- View the details of an individual task.
- Mark a task as completed or pending.
- Delete tasks that are no longer needed.
- View the total number of tasks, completed tasks, and pending tasks.
- Store task information in a SQLite database.

## Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite
- Git and GitHub

## Pages

1. **Home page:** Displays saved tasks and task summary counts.
2. **Add Task page:** Provides a form for entering a new task.
3. **Task Details page:** Displays an individual task and provides options to update its completion status or delete it.

## How to Run the Application

### Requirements

- Python installed on your computer.
- Django installed in your Python environment.
- Git, if you want to clone the repository.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sydneyjack/StudyTaskManager.git
   ```

2. Open the project folder:

   ```bash
   cd StudyTaskManager
   ```

3. Install Django:

   ```bash
   python -m pip install django
   ```

4. Create the database tables:

   ```bash
   python manage.py migrate
   ```

5. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

6. Open your browser and visit:

   http://127.0.0.1:8000/

## Database

The application uses Django's SQLite database to store study tasks. Each task includes a title, description, optional due date, completion status, and creation date.

The database tables are created using Django migrations. The local database file is not included in the GitHub repository; running the migration command creates the required tables.

## CSE 310 Module Requirements

This project uses Django and Python to generate web pages. It includes three HTML pages, accepts user input through a form, and uses a SQLite database to save and retrieve tasks. The application runs locally using Django's development server.

## Demo Video

**Video link:** Add your 4–5 minute demonstration video link here after uploading it.

The video will demonstrate the application running, explain its main features, and walk through the important parts of the code.

## Author

Created as a CSE 310 Applied Programming module project.
