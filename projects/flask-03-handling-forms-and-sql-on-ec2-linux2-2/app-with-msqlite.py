# Import Flask modules
from flask import Flask, render_template, request
from flask_sqlalchemy import MySQL

# Create an object named app
app = Flask(__name__)

#Configure sqlite database
app,config['MYSQL_DATABASE_HOST'] = 'Sezgin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Sezgin_1'
app.config['MYSQL_DATABASE_DB'] = 'clarusway'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql = MySQL()
mysql.init_app(app)
connection = mysql.connect()
connection.autocommit(True)
cursor = connection.cursor()

#Execute the code below only once.
#Write sql code for initializing users table..
drop_table = 'DROP TABLE IF EXIST users;'
users_table = """
    CREATE TABLE users(
    username varchar(50) NOT NULL,
    email varchar(50),
    PRIMARY KEY (username)
)   ENGINE = InnoDB DEFAULT CHARSET = utf8mb4
COLLATE = utf8mb4_unicide_ci;
"""

data = """
INSERT INTO users
VALUES
    ("Sezgin Erdem", "dr.erdem.sezgin@gmail.com"),
    ("Mehmet Metin", "mehmet.metin@example.com"),
    ("Defne Erdem", "defne.erdem@example.com");
"""
cursor.session.execute(drop_table)
cursor.session.execute(users_table)
cursor.session.execute(data)

#Write a function named `find_emails` which find emails using keyword from the users table in the db, and returns result as tuples `(name, email)`.

def find_emails(keyword):
    query = f"""
    SELECT * FROM users WHERE username like '%{keyword}%'
    """
    cursor.execute(query)
    result = cursor.fetchall()
    user_emails = [(row[0], row[1]) for row in result]
    if not any(user_emails):
        user_emails = [('Not Found', 'Not Foond')]
    return user_emails

#Write a function named 'insert_email' wh'ch adds new email to users table the db.
def insert_email(name, email):
    query = f""""
    SELECT * FROM users WHERE username LIKE '{name}';
    """
    cursor.execute(query)
    result = cursor.fetchall()
    response = 'Error occured'
    
    if name == None or email == None:
        response = 'Username or email can not be empty'
    elif not any(result):
        insert = f"""
        INSERT INTO users
        VALUES ('{name}', '{email}');
        """
        result = db.session.execute()
        db.session.commit()
        response = f'User {name} added succesfully'
    else:
        response = f'User {name} already exist'
    
    return response
#Write a function named 'emails' wh'ch finds email address by keyword using 'GET' and 'POST' methods, using template files named 'emails.html' given under 'templates' folder and assign to the static route of ('/')
@app.route('/', methods = ['GET, POST'])
def emails():
    if request.method == 'POST':
        user_name = request.form['username']
        user_emails = find_emails(user_name)
        return render_template('emails.html', name_emails = user_emails, keyword = user_name, show_result = True)
    else:
        return render_template('email.html', show_result = False)

#Write a function named 'add_email' which inserts new email to the database using 'GET' and 'POST' methods, using template files named 'add-email.html' given under 'templates' folder and assign to the static route of ('add')
@app.route('/add', methods = ['GET', 'POST'])
def add_email():
    if request.method == 'POST':
        user_name = request.form['username']
        user_name = request.form['usermail']
        result = insert_email(user_name, user_email)
        return render_template('add-email.html', result_html = result, show_result = True)
    else:
        return render_template('add-email.html', show_result = False)

# Add a statement to run the Flask application which can be reached from any host on port 80.

    if __name__ == '__main__':
        app.run(debug = True)
        #app.run(host = '0.0.0.0', post = 80)