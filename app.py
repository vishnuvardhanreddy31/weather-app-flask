from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username and password are correct
        if username == 'admin' and password == 'password':
            # If the login is successful, redirect to the home page
            return redirect('/home')
        else:
            # If the login is unsuccessful, render the login page with an error message
            return render_template('login.html', error='Invalid username or password')
    else:
        # If the request method is GET, render the login page
        return render_template('login.html')


# Home page
@app.route('/home')
def home():
    # Render the home page
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
