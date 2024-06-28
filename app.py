from flask import Flask, render_template, request, redirect
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Function to connect to the database
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Update with your MySQL username
            password="pradyu9164",  # Update with your MySQL password
            database="investigation_log"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_cases', methods=['POST'])
def submit_cases():
    case_id = request.form['case_id']
    date_time = request.form['date_time']
    case_type = request.form['type']
    victim_id = request.form['victim_id']
    culprit_id = request.form['culprit_id']
    location_id = request.form['location_id']
    discription = request.form['discription']

    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        sql = "INSERT INTO `cases` (case_id, date_time, type, victimid, criminalid, location_id, discription) VALUES (%s, %s, %s, %s, %s, %s,%s)"
        val = (case_id, date_time, case_type, victim_id, culprit_id, location_id, discription)

        try:
            cursor.execute(sql, val)
            connection.commit()
            return redirect('/')
        except Error as e:
            return f"An error occurred while inserting data: {e}"
        finally:
            cursor.close()
            connection.close()
    else:
        return "Failed to connect to the database"

@app.route('/submit_people', methods=['POST'])
def submit_cases():
    person_id = request.form['person_id']
    name = request.form['name']
    age = request.form['age']
    phno = request.form['phno']
    address_id = request.form['address_id']
    relationship = request.form['relationship']

    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        sql = "INSERT INTO `cases` (person_id, name, age, phno, address_id, relationship) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (person_id, name, age, phno, address_id, relationship)

        try:
            cursor.execute(sql, val)
            connection.commit()
            return redirect('/')
        except Error as e:
            return f"An error occurred while inserting data: {e}"
        finally:
            cursor.close()
            connection.close()
    else:
        return "Failed to connect to the database"

@app.route('/submit_jail', methods=['POST'])
def submit_jail():
    record_id = request.form['record_id']
    preson_id = request.form['preson_id']
    reason = request.form['reason']
    enter_date = request.form['enter_date']
    release_date = request.form['release_date']
    

    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        sql = "INSERT INTO `cases` (record_id, preson_id, reason, enter_date, release_date) VALUES (%s, %s, %s, %s, %s)"
        val = (record_id, preson_id, reason, enter_date, release_date)

        try:
            cursor.execute(sql, val)
            connection.commit()
            return redirect('/')
        except Error as e:
            return f"An error occurred while inserting data: {e}"
        finally:
            cursor.close()
            connection.close()
    else:
        return "Failed to connect to the database"


@app.route('/submit_people', methods=['POST'])
def submit_cases():
    location_id = request.form['location_id']
    location_name = request.form['location_name']
    description = request.form['description']
    place = request.form['place']

    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        sql = "INSERT INTO `cases` (location_id, location_name, description, place) VALUES (%s, %s, %s, %s)"
        val = (location_id, location_name, description, place)

        try:
            cursor.execute(sql, val)
            connection.commit()
            return redirect('/')
        except Error as e:
            return f"An error occurred while inserting data: {e}"
        finally:
            cursor.close()
            connection.close()
    else:
        return "Failed to connect to the datalocation"
    


@app.route('/submit_evidence', methods=['POST'])
def submit_cases():
    evidence_id = request.form['evidence_id']
    location_id = request.form['location_id']
    description = request.form['description']
    notes = request.form['notes']
    case_id= request.form['case_id']
    

    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        sql = "INSERT INTO `cases` (evidence_id, location_id, description, notes, case_id) VALUES (%s, %s, %s, %s, %s)"
        val = (evidence_id, location_id, description, notes,case_id)

        try:
            cursor.execute(sql, val)
            connection.commit()
            return redirect('/')
        except Error as e:
            return f"An error occurred while inserting data: {e}"
        finally:
            cursor.close()
            connection.close()
    else:
        return "Failed to connect to the database"

@app.route('/submit_testimonials', methods=['POST'])
def submit_cases():
    testimonial_id = request.form['testimonial_id']
    case_id = request.form['case_id']
    person_id = request.form['person_id']
    statement = request.form['statement']

    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        sql = "INSERT INTO `cases` (testimonial_id, case_id, person_id, statement) VALUES (%s, %s, %s, %s)"
        val = (testimonial_id, case_id, person_id, statement)

        try:
            cursor.execute(sql, val)
            connection.commit()
            return redirect('/')
        except Error as e:
            return f"An error occurred while inserting data: {e}"
        finally:
            cursor.close()
            connection.close()
    else:
        return "Failed to connect to the database"
