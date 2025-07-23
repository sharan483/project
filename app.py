from flask import Flask, request, redirect, send_from_directory
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']

        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE email=? AND password=? AND role=?", (email, password, role))
            user = cursor.fetchone()

            
        finally:
            conn.close()

        if user:
            if role == 'student':
                return redirect('/student_dashboard.html')
            elif role == 'teacher':
                return redirect('/teacher_dashboard.html')
        else:
            return send_from_directory('pages', 'login.html')

    return send_from_directory('pages', 'login.html')
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']

        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)", 
                          (name, email, password, role))
            conn.commit()
            return redirect('/login')
        except sqlite3.IntegrityError:
            return redirect('/register?error=1')
        finally:
            conn.close()

    return send_from_directory('pages', 'register.html')


@app.route('/student_dashboard.html')
def student_dashboard():
    return send_from_directory('pages', 'student_dashboard.html')

@app.route('/teacher_dashboard.html')
def teacher_dashboard():
    return send_from_directory('pages', 'teacher_dashboard.html')


@app.route('/show_users')
def show_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return '<br>'.join(str(row) for row in rows)


if __name__ == '__main__':
    app.run(debug=True)