import yagmail as yg
import os
from flask import Flask
app = Flask(__name__)
a1=yg.SMTP(user="mymail@gmail.com",oauth2_file="1.json")
a2=yg.SMTP(user="mymail@gmail.com",oauth2_file="2.json")
a3=yg.SMTP(user="mymail@gmail.com",oauth2_file="3.json")
a4=yg.SMTP(user="mymail@gmail.com",oauth2_file="4.json")
a5=yg.SMTP(user="mymail@gmail.com",oauth2_file="5.json")
a6=yg.SMTP(user="mymail@gmail.com",oauth2_file="6.json")
a7=yg.SMTP(user="mymail@gmail.com",oauth2_file="7.json")
a8=yg.SMTP(user="mymail@gmail.com",oauth2_file="8.json")
a9=yg.SMTP(user="mymail@gmail.com",oauth2_file="9.json")
a10=yg.SMTP(user="mymail@gmail.com",oauth2_file="10.json")
a11=yg.SMTP(user="mymail@gmail.com",oauth2_file="11.json")
a12=yg.SMTP(user="mymail@gmail.com",oauth2_file="12.json")
a13=yg.SMTP(user="mymail@gmail.com",oauth2_file="13.json")
a14=yg.SMTP(user="mymail@gmail.com",oauth2_file="14.json")
a15=yg.SMTP(user="mymail@gmail.com",oauth2_file="15.json")
a16=yg.SMTP(user="mymail@gmail.com",oauth2_file="16.json")
a17=yg.SMTP(user="mymail@gmail.com",oauth2_file="17.json")
a18=yg.SMTP(user="mymail@gmail.com",oauth2_file="18.json")
a19=yg.SMTP(user="mymail@gmail.com",oauth2_file="19.json")
a20=yg.SMTP(user="mymail@gmail.com",oauth2_file="20.json")
a21=yg.SMTP(user="mymail@gmail.com",oauth2_file="21.json")
@app.route("/1/bomb/<string:t>/<string:s>/<string:m>")
def bomb1(t,s,m): 
    a1.send(to=t,subject=s,contents=m)
    return "Sent"
@app.route("/2/bomb/<string:t>/<string:s>/<string:m>")
def bomb2(t,s,m): 
    a2.send(to=t,subject=s,contents=m)
    return "Sent"
@app.route("/3/bomb/<string:t>/<string:s>/<string:m>")
def bomb3(t,s,m): 
    a3.send(to=t,subject=s,contents=m)
    return "Sent"
@app.route("/4/bomb/<string:t>/<string:s>/<string:m>")
def bomb4(t,s,m): 
    a4.send(to=t,subject=s,contents=m)
    return "Sent"
@app.route("/5/bomb/<string:t>/<string:s>/<string:m>")
def bomb5(t,s,m): 
    a5.send(to=t,subject=s,contents=m)
    return "Sent"
@app.route("/6/bomb/<string:t>/<string:s>/<string:m>")
def bomb6(t,s,m): 
    a6.send(to=t,subject=s,contents=m)
    return "Sent"
@app.route("/7/bomb/<string:t>/<string:s>/<string:m>")
def bomb7(t,s,m): 
    a7.send(to=t,subject=s,contents=m)
    return "Sent"
@app.route("/8/bomb/<string:t>/<string:s>/<string:m>")
def bomb8(t,s,m): 
    a8.send(to=t,subject=s,contents=m)
    return "Sent"
@app.route("/9/bomb/<string:t>/<string:s>/<string:m>")
def bomb9(t,s,m): 
    a9.send(to=t,subject=s,contents=m)
    return "Sent"
@app.route("/10/bomb/<string:t>/<string:s>/<string:m>")
def bomb10(t,s,m): 
    a10.send(to=t,subject=s,contents=m)
    return "Sent"
@app.route("/11/bomb/<string:t>/<string:s>/<string:m>")
def bomb11(t,s,m): 
    a11.send(to=t,subject=s,contents=m)
    return "Sent"
@app.route("/12/bomb/<string:t>/<string:s>/<string:m>")
def bomb12(t,s,m): 
    a12.send(to=t,subject=s,contents=m)
    return "Sent"
@app.route("/13/bomb/<string:t>/<string:s>/<string:m>")
def bomb13(t,s,m): 
    a13.send(to=t,subject=s,contents=m)
    return "Sent"
@app.route("/14/bomb/<string:t>/<string:s>/<string:m>")
def bomb14(t,s,m): 
    a14.send(to=t,subject=s,contents=m)
    return "Sent"
@app.route("/15/bomb/<string:t>/<string:s>/<string:m>")
def bomb15(t,s,m): 
    a15.send(to=t,subject=s,contents=m)
    return "Sent"
@app.route("/16/bomb/<string:t>/<string:s>/<string:m>")
def bomb16(t,s,m): 
    a16.send(to=t,subject=s,contents=m)
    return "Sent"
@app.route("/17/bomb/<string:t>/<string:s>/<string:m>")
def bomb17(t,s,m): 
    a17.send(to=t,subject=s,contents=m)
    return "Sent"
@app.route("/18/bomb/<string:t>/<string:s>/<string:m>")
def bomb18(t,s,m): 
    a18.send(to=t,subject=s,contents=m)
    return "Sent"
@app.route("/19/bomb/<string:t>/<string:s>/<string:m>")
def bomb19(t,s,m): 
    a19.send(to=t,subject=s,contents=m)
    return "Sent"
@app.route("/20/bomb/<string:t>/<string:s>/<string:m>")
def bomb20(t,s,m): 
    a20.send(to=t,subject=s,contents=m)
    return "Sent"
@app.route("/21/bomb/<string:t>/<string:s>/<string:m>")
def bomb21(t,s,m): 
    a21.send(to=t,subject=s,contents=m)
    return "Sent"
if __name__ == '__main__': 
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port,debug=True)
