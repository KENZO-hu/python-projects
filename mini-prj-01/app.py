from flask import Flask,render_template
app=Flask(__name__)
#smaple data for employers
employees=[
    {"name": "Alice Johnson", "role": "Fitness Trainer", "email": "alice@example.com"},
    {"name": "Bob Smith", "role": "Nutrition Specialist", "email": "bob@example.com"},
    {"name": "Catherine Lee", "role": "Yoga Instructor", "email": "catherine@example.com"},
    {"name": "David Brown", "role": "Strength Coach", "email": "david@example.com"},
]
@app.route("/")
def index():
    return render_template("index.html",employees=employees)
if __name__ == "__main__":
    app.run(debug=True)