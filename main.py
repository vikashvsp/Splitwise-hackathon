from flask import Flask,request,render_template,session
from splitwise import Splitwise
import json
import logging
import Config
import requests
import pyqrcode
import png
from pyqrcode import QRCode

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


@app.route('/', methods=['GET', 'POST'])
def home():
     return render_template("home.html")

@app.route('/get_current_user', methods=['GET', 'POST'])
def get_current_user():
     response = (requests.get(url+'/get_current_user', auth=BearerAuth('rDbzbDRhoutm3quupPHPv7Iv9xDftcVYXfAAE70H'))).json()
     return render_template("index.html",response=response)




@app.route('/get_expenses', methods=['GET', 'POST'])
def get_expenses():
     response = (requests.get(url+'/get_expenses', auth=BearerAuth('rDbzbDRhoutm3quupPHPv7Iv9xDftcVYXfAAE70H'))).json()
     # return (response)
     return render_template("expense.html",response=response)

@app.route('/create_friend', methods=['GET', 'POST'])
def create_friend():
     data={"user_email": "ada@example.com","user_first_name": "Ada","user_last_name": "Lovelace"
}
     response = (requests.post(url+'/create_friend',data=(data), auth=BearerAuth('rDbzbDRhoutm3quupPHPv7Iv9xDftcVYXfAAE70H')))
     return response.json()


@app.route('/get_friends', methods=['GET', 'POST'])
def get_friends():
     response = (requests.get(url+'/get_friends', auth=BearerAuth('rDbzbDRhoutm3quupPHPv7Iv9xDftcVYXfAAE70H'))).json()
     return response

@app.route('/create_group', methods=['GET', 'POST'])
def create_group():
     data={
  "name": "The Brain Trust",
  "group_type": "trip",
  "users__0__first_name": "Alan",
  "users__0__last_name": "Turing",
  "users__0__email": "alan@example.org",
  "users__1__id": 5823
}
     response = (requests.post(url+'/create_group',data=(data), auth=BearerAuth('rDbzbDRhoutm3quupPHPv7Iv9xDftcVYXfAAE70H')))
     return response.json()




@app.route('/create_expense', methods=['GET', 'POST'])
def create_expense():
     data={
  "cost": "25",
  "description": "Grocery run",
  "details": "string",
  "date": "2012-05-02T13:00:00Z",
  "repeat_interval": "never",
  "currency_code": "USD",
  "category_id": 15,
  "group_id": 0,
  "split_equally": True
}
     response = (requests.post(url+'/create_expense',data=(data), auth=BearerAuth('rDbzbDRhoutm3quupPHPv7Iv9xDftcVYXfAAE70H')))
     return response.json()





@app.route("/create_qr",methods=['GET', 'POST'])
def create_qr():
     response = (requests.get(url+'/get_expenses', auth=BearerAuth('rDbzbDRhoutm3quupPHPv7Iv9xDftcVYXfAAE70H'))).json()

     value=response['expenses'][0]['users'][0]['paid_share']
     data="click to pay"+value +"on www.paytm.com"
     img=pyqrcode.create(data)
     img.svg("myqr.svg", scale = 8)
     return render_template("qr.html")


if __name__ == '__main__':
     app.run(debug=True)