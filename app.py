from flask import Flask, render_template, request, jsonify
from flask import Flask, render_template, request, redirect
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed to keep the client-side sessions secure

class GlobalSQLCredentials:
    username = None
    password = None

# Function to connect to the database
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user=GlobalSQLCredentials.username,  # Update with your MySQL username
            password=GlobalSQLCredentials.password,  # Update with your MySQL password
            database="investigation_log"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

@app.route('/')
def home():
    return render_template('sql_login.html')

@app.route('/sql_login', methods=['GET', 'POST'])
def sql_login():
    if request.method == 'POST':
        sql_username = request.form['username']
        sql_password = request.form['password']

        # Test database connection with provided credentials
        GlobalSQLCredentials.username = sql_username
        GlobalSQLCredentials.password = sql_password

        connection = get_db_connection()
        if connection:
            connection.close()
            return render_template('options.html')  # Redirect to the main page or dashboard
        else:
            error = 'Invalid SQL credentials. Please try again.'
            return render_template('sql_login.html', error=error)
    else:
        return render_template('sql_login.html')

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
def submit_people():
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

@app.route('/submit_location', methods=['POST'])
def submit_location():
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
def submit_evidence():
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
def submit_testimonials():
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

@app.route('/show_tables', methods=['GET', 'POST'])
def show_tables():
    if request.method == 'POST':
        table = request.form.get('table')
        whereatt = request.form.get('whereatt')
        operator = request.form.get('operator')
        value = request.form.get('value')
        
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                
                query = f"SELECT * FROM {table} WHERE {whereatt} {operator} %s"
                cursor.execute(query, (value,))
                
                results = cursor.fetchall()
                column_names = [i[0] for i in cursor.description]
                
                cursor.close()
                connection.close()
                
                return render_template('show_tables.html', columns=column_names, data=results, show_table=True)
            except Error as e:
                return f"An error occurred while retrieving data: {e}"
            finally:
                cursor.close()
                connection.close()
        else:
            return "Failed to connect to the database."
    
    return render_template('show_tables.html', show_table=False)

@app.route('/get_columns', methods=['POST'])
def get_columns():
    table_name = request.json.get('table')
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(f"SHOW COLUMNS FROM {table_name}")
            columns = [row[0] for row in cursor.fetchall()]
            cursor.close()
            connection.close()
            return jsonify(columns)
        except Error as e:
            return jsonify({"error": str(e)})
    return jsonify({"error": "Failed to connect to the database."})

@app.route('/join_tables', methods=['GET', 'POST'])
def join_tables():
    if request.method == 'POST':
        selected_table = request.form.get('selected_table')
        table1 = request.form.get('table1')
        table2 = request.form.get('table2')
        attribute1 = request.form.get('attribute1')
        attribute2 = request.form.get('attribute2')
        whereatt = request.form.get("whereatt")
        value = request.form.get("value")
        
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                
                sql = f"SELECT * FROM {table1} NATURAL JOIN {table2} ON {table1}.{attribute1}={table2}.{attribute2} WHERE {table1}.{whereatt}={value}"
                cursor.execute(sql)
                
                results = cursor.fetchall()
                column_names = [i[0] for i in cursor.description]
                
                cursor.close()
                connection.close()
                
                return render_template('join_tables.html', columns=column_names, data=results, show_table=True, selected_table=selected_table)
            except Error as e:
                return f"An error occurred while retrieving data: {e}"
            finally:
                cursor.close()
                connection.close()
        else:
            return "Failed to connect to the database."
    
    # Fetch all table names from the database
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = [table[0] for table in cursor.fetchall()]
        cursor.close()
        connection.close()
        
        return render_template('join_tables.html', tables=tables, show_table=False)

    return "Failed to connect to the database."

@app.route('/get_attributes', methods=['POST'])
def get_attributes():
    table_name = request.form.get('table_name')

    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        sql = f"SHOW COLUMNS FROM {table_name}"
        try:
            cursor.execute(sql)
            columns = cursor.fetchall()
            attribute_names = [column[0] for column in columns]

            cursor.close()
            connection.close()
            return jsonify(attributes=attribute_names)

        except Error as e:
            return jsonify(error=str(e))

    else:
        return jsonify(error="Failed to connect to the database.")

if __name__ == '__main__':
    app.run(debug=True)
