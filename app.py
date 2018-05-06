from flask import Flask, render_template,redirect, url_for,request
import json

'''Key Learning Goals
1. Defining routes and navigation between routes
2. Jinjas2 templating
3. Processing data from forms
4. Simple data storage using json
5. Build a fully functional app

Overview:
- Backend for login
- Backend for signup
- Backend for home page
- Backend for task entry page
- Rendering for home page
- Rendering for index page
- 22 items to complete
'''

app=Flask(__name__)

'''Allows users to go to the index page'''
@app.route("/")
def index():
    #TODO:(4.5) Show different template renderings using name
    name="Ryan"
    return render_template("index.html",name=name)

'''Allows users to login'''
@app.route("/login")
def login():
    return render_template("login.html")

'''Allows users to sign up'''
@app.route("/signup")
def signup():
    return render_template("signup.html")

'''Allows entries into the Todo List'''
@app.route("/entry")
def entry():
    #TODO:(2) Return the correct template
    return render_template("entry.html")

#TODO:(4) Render the correct template for the "home" page
#TODO:(12) Add permissions for post requests
@app.route("/home",methods=["GET","POST"])
def home():
    #TODO:(5) Inject the below list of tasks and name into the correct template
    #Data that will be injected into the template
    tasks = ["Cleaning the dishes", "Walking the dog", "Cooking dinner", "Playing basketball", "Practicing piano"]
    name=""

    # TODO:(22) Update the tasks with the ones from the "tasks.json" file
    #Opens the "tasks.json" file and reads the contents into tasks
    with open("tasks.json", "r") as f:
        tasks = json.load(f)

    #TODO:(13) Check post request
    #TODO:(14) Get the entered username
    #TODO:(15) Check if the username and password match
    #TODO:(16) If there is a match, re-render the "home" page with the tasks and the username

    #Checks the form method
    if request.method=="POST":

        #Obtains username and password from the form
        username=request.form["username"]
        password=request.form["password"]

        #Loads the user login data and compares with the posted data
        with open("user.json","r") as f:
            user_data=json.load(f)

            #Checks to see if the entered usernames and passwords match with the record in "user.json"
            if user_data["username"]==username and user_data["password"]==password:

                #Re-renders template with user data
                return render_template("home.html",tasks=tasks,name=username)

    return render_template("home.html",tasks=tasks,name=name)

#TODO:(17) Check post request
#TODO:(18) Create an empty list for tasks
#TODO:(19) Get all of the tasks from the form and store in a var
#TODO:(20) Add all tasks to the task list
#TODO:(21) Write all of the tasks to the "tasks.json" file
@app.route("/confirm-entry",methods=["POST","GET"])
def confirm_entry():

    #Checks if the method of the request is post
    if request.method=="POST":

        #Initializes an empty list
        tasks_list=[]

        #Obtains the tasks from the frontend form
        tasks=request.form

        #Adds each task to the tasks_list
        for key in tasks:
            task=tasks[key]
            tasks_list.append(task)

        #Writes the tasks to the json file
        with open("tasks.json","w") as f:
            json.dump(tasks_list,f)

    return "Your tasks have been saved <br> <a href='home'><button>View Tasks</button></a>"

#TODO:(1) Make a new route whose name is "confirm-signup"
#TODO:(3) Make the new route render the "confirm-signup" page
#TODO:(6) Allow post and get for the confirmation page
@app.route("/confirm-signup",methods=["POST","GET"])
def confirm_signup():

    #TODO:(7) Check post request form data
    #TODO:(8) Create variables from the posted data
    #TODO:(9) Store data in the "user" dictionary
    #TODO:(10) Store data in json file
    #TODO:(11) Server side redirect to "login" page

    #Checks if the request method is post
    if request.method=="POST":

        #Initializes empty user dictionary
        user={}

        #Obtains the username, password, and email from the frontend form
        username=request.form["username"]
        password=request.form["password"]
        email=request.form["email"]

        #Stores the user data into the previously created user dictionary
        user["password"]=password
        user["username"]=username
        user["email"]=email

        #Writes the data to the user json file
        with open("user.json","w") as f:
            json.dump(user,f)

        #Redirects to the login page
        return redirect(url_for("login"))

    return render_template("confirm-signup.html")

if __name__=="__main__":
    app.run(debug=True) #Never run as debug=True in a production environment


