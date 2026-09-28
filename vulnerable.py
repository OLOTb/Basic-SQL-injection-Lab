from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# HTML template for the web page
HTML_TEMPLATE = """
<div style="text-align:center; margin-top:15%;">
    <h2>Login (Vulnerable Version)</h2>
    <form method="POST">
        Username: <input type="text" name="username"><br><br>
        Password: <input type="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
    <p style="color:{msg_color}"><b>{message}</b></p>
    </div>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""
    msg_color = "black"
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
    
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
        try:
            cursor.execute(query)
            user = cursor.fetchone()
        
            if user:
                message = f"Success: Logged in (Admin bypassed!) - Executed query:{query}"
                msg_color = "green"
            else:
                message = "Error: Invalid credentials."
                msg_color = "red"
        except sqlite3.Error as e:
            message = f"SQL Error: {e}"
            msg_color = "red"
        
        conn.close()
    
    return render_template_string(HTML_TEMPLATE, message=message, msg_color=msg_color)

if __name__ == '__main__':
    print("VULNERABLE application running on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)