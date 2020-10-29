from flask import Flask, render_template
app = Flask(__name__)

users = ['Alice', 'Bob', 'Chris', 'Debbie']

@app.route('/')
def home_Page():
    return render_template('index.html', users = users)

@app.route('/Alice')
def alice_name():
    user = 'Alice'
    return render_template('existing_user.html', user=user)

@app.route('/Bob')
def bob_name():
    user = 'Bob'
    return render_template('existing_user.html', user=user)

@app.route('/Chris')
def chris_name():
    user = 'Chris'
    return render_template('existing_user.html', user=user)

@app.route('/Debbie')
def debbie_name():
    user = 'Debbie'
    return render_template('existing_user.html', user=user)

app.run(debug=True)