from flask import Flask
from os import environ
# Initializing flask app
app = Flask(__name__)
  
  
# Route for seeing a data
@app.route('/data')
def get_bag_of_dicks():
  
    # Returning an api for showing in  reactjs
    return {
        "Title":"huku.rocks", 
        "Text1":"coming soon-ish",
        "Text2":"eventually", 
        "github":"python",
        "docker":"python",
        "twitter":"python",
        "email":"python",
        "copy":"huku.rocks",
        "menu":"monitor"
        }
  
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)