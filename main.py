from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/create_class")
def create_class():
    return render_template('create_class.html')

@app.route("/custom_course", methods=["GET","POST"])
def custom_class():

    if request.method == "POST":

        req = request.form

        #Collecting the form values
        #course_code = req.get("course_code")
        #course_title = req.get("course_title")
        #start_time = req.get("start_time")
        #end_time = req.get("end_time")
        #professor_name = req.get("professor_name")
        #email = req.get("email")
        #website_link = req.get("website_link")
        #syllabus_link = req.get("syllabus_link")

    return render_template('custom_course.html', req = req)

@app.route("/class")
def course():
    return render_template('class.html')

if __name__ == "__main__":
    app.run(debug=True)
