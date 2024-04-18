from flask import Flask         # from the flask module import the Flask class

app = Flask(__name__)           # Create an instance of the Flask class

@app.get("/about")
@app.get("/")                   # Flask decorater that maps view functions to routes
def index():                    # view function
    me = {                      #python dictionary
        "first_name": "Andrew",
        "last_name": "Reyna",
        "hobbies": "BJJ",
        "is_online": True
    }
    return me                    #when tou return a dict from a view function, it becomes JSON