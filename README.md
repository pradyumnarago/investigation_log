# investigation_log
Here's a detailed README to set up and run your Flask application with a MySQL database. This guide includes instructions to create the necessary database and tables, configure the application, and run it.

---

## README

# Flask Application with MySQL Database

This Flask application connects to a MySQL database to manage and display various types of data, including cases, people, jail records, locations, evidence, and testimonials. The application supports user login to access and manipulate the database.

### Table of Contents
1. [Requirements](#requirements)
2. [Database Setup](#database-setup)
3. [Flask Application Setup](#flask-application-setup)
4. [Running the Application](#running-the-application)

### Requirements

- Python 3.7 or higher
- MySQL Server
- Flask
- Flask-MySQL
- Other required Python packages listed in `requirements.txt`

### Database Setup

1. **Install MySQL**:
    - Download and install MySQL Server from [MySQL Downloads](https://dev.mysql.com/downloads/mysql/).

2. **Start MySQL Server**:
    - Ensure your MySQL server is running. You can start it using the terminal or MySQL Workbench.

3. **Create the Database**:
    - Open MySQL command line or MySQL Workbench.
    - Create a new database with the following command:
    ```sql
    CREATE DATABASE investigation_log;
    ```

4. **Create Tables**:
    - Connect to the `investigation_log` database:
    ```sql
    USE investigation_log;
    ```
    - Create tables using the following SQL commands:

    ```sql
    CREATE TABLE cases (
        case_id INT PRIMARY KEY,
        date_time DATETIME,
        type VARCHAR(255),
        victim_id INT,
        culprit_id INT,
        location_id INT,
        discription TEXT
    );

    CREATE TABLE people (
        person_id INT PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        phno VARCHAR(255),
        address_id INT,
        relationship VARCHAR(255)
    );

    CREATE TABLE jail_record (
        record_id INT PRIMARY KEY,
        preson_id INT,
        reason TEXT,
        enter_date DATE,
        release_date DATE
    );

    CREATE TABLE location (
        location_id INT PRIMARY KEY,
        location_name VARCHAR(255),
        description TEXT,
        place VARCHAR(255)
    );

    CREATE TABLE evidences (
        evidence_id INT PRIMARY KEY,
        location_id INT,
        description TEXT,
        notes TEXT,
        case_id INT
    );

    CREATE TABLE testimonials (
        testimonial_id INT PRIMARY KEY,
        case_id INT,
        person_id INT,
        statement TEXT
    );
    ```

### Flask Application Setup

1. **Clone the Repository**:
    - Clone this repository to your local machine.
    ```bash
    git clone https://github.com/pradyumnarago/investigation_log.git
    cd flask-mysql-app
    ```

2. **Create Virtual Environment**:
    - Create and activate a virtual environment.
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    - Install the required packages.
    ```bash
    pip install -r requirements.txt
    ```


### Running the Application

1. **Run the Flask Application**:
    - Make sure your MySQL server is running.
    - Start the Flask application.
    ```bash
    python app.py
    ```
    - The application should be running on `http://127.0.0.1:5000/`.

2. **Access the Application**:
    - Open your browser and go to `http://127.0.0.1:5000/`.
    - Enter your MySQL credentials to login.
    - Navigate through different sections to manage and display data.

### Notes

- **Database Connectivity**:
    - Ensure that the MySQL server is accessible from your Flask application. The `host` parameter in `mysql.connector.connect()` is set to `localhost` by default, assuming that the MySQL server is running on the same machine as the Flask application. Modify it if your MySQL server is on a different machine.
  
- **Debug Mode**:
    - The application is set to run in debug mode. This is useful for development and debugging, but make sure to disable debug mode in a production environment.

---

With these steps, you should have a fully functional Flask application connected to a MySQL database. This application allows users to input, view, and manage data related to cases, people, jail records, locations, evidence, and testimonials.