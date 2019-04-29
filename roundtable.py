from flask import Flask     # > Import Flask class
app = Flask(__name__)       # > Create *instance* of Flask Class obj 
                            #   - (will be our WSGI application)*
                         

@app.route('/')             # > Uses route() decorator to tell Flask
                            #   what URL should trigger our func
def hello_world():          # > Name our function (also used to generate URL's for 
                            #   this particular function)
    return 'Hello, from Round Table!'  # > Return message we want to display on User's browser



''' * --  1st arg is name of app's module/package
          We use single module, so we use __name__ b/c
          __name__ is different depending on if started
          as app or imported as module. '__main__' for app
          vs. actual import name. (Flask needs name to know
          where to look for tmeplates, static files, etc.
          See Flask documentation for more.

'''
