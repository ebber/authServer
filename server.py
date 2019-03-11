from flask import Flask, render_template_string
app = Flask(__name__)

from hardwareController import lock, unlock
@app.route("/")
def hello():
    return "Hello World, this is the auth server"

@app.route("/unlock/<bay_num>")
def unlock_route(bay_num):
   success = unlock(bay_num)
   if success:
       return render_template_string("Successful unlock"), 200
   else:
       return render_template_string("Failed unlock"), 500



@app.route("/lock/<bay_num>")
def lock_route(bay_num):
   success = lock(bay_num)
   if success:
       return render_template_string("Successful lock"), 200
   else:
       return render_template_string("Failed lock"), 500




