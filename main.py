from flask import Flask, redirect
from pyngrok import ngrok
import os
app=Flask(__name__)
os.system("python3 main3.py&")
ngrok.set_auth_token("1l3JibP4VTI3Zh3DmJHyFGRldOX_63Gd9JaRdsrrLW2TSJvB2")
ngr=ngrok.connect(5100)
@app.route("/")
def index():
    return redirect(ngr.public_url)
app.run(host='0.0.0.0', port=os.environ.get("PORT", 8080))