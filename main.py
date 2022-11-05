from flask import Flask,request,render_template,session
from splitwise import Splitwise
import json
import logging
import Config
import requests
logging.basicConfig(level=logging.DEBUG)
sObj = Splitwise("GWPWDMzSxHbd31BJlvLLAKaC5aeXNZvH8LNMD52R","4nsG7SFUjBCeqgHMNZece3KbfBUWKQ8q5Kyn8O2w")
app = Flask(__name__)

class BearerAuth(requests.auth.AuthBase):
     def __init__(self, token):
          self.token = token
     def __call__(self, r):
          r.headers["authorization"] = "Bearer " + self.token
          return r



url="https://secure.splitwise.com/api/v3.0"




@app.route('/get_current_user', methods=['GET', 'POST'])
def get_current_user():
     response = (requests.get(url+'/get_current_user', auth=BearerAuth('rDbzbDRhoutm3quupPHPv7Iv9xDftcVYXfAAE70H'))).json()
     return render_template("index.html",response=response)




@app.route('/get_expenses', methods=['GET', 'POST'])
def get_expenses():
     response = (requests.get(url+'/get_expenses', auth=BearerAuth('rDbzbDRhoutm3quupPHPv7Iv9xDftcVYXfAAE70H'))).json()
     return response



if __name__ == '__main__':
     app.run(debug=True)