from flask import flask,
render_template
app = flask (__name__)
@app.route("/")
def home():
  retern
  render_template("login.htm")
@app.route("/dashboard")
def dashbord():
     retern
   render_template("dashboard.htm")
if__name_ =="__main__":
   app.run(debug=True)
