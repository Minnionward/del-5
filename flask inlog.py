from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# login pass og brukernavn
USER_CREDENTIALS = {'minion': '123QWEr'}

# hvor kontorene skal bli lagret
rented_offices = []

# funksjon for å sjekke om passord/brukernavn er rett
def check_credentials(username, password):
    return username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password

# login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if check_credentials(username, password):
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', message='Invalid username or password')
    return render_template('login.html', message=None)

# Dashbaord etter du har logget in
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', rented_offices=rented_offices)

# legg till et kontor
@app.route('/add_office', methods=['POST'])
def add_office():
    office_name = request.form['office_name']
    rented_offices.append(office_name)
    return redirect(url_for('dashboard'))

# slett et kontor
@app.route('/delete_office/<office_name>', methods=['POST'])
def delete_office(office_name):
    rented_offices.remove(office_name)
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
