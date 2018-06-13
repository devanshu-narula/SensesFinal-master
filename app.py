from flask import Flask,render_template, request
from scrape_test import start_work
import pandas as pd
import os
app = Flask(__name__)

port=int(os.getenv('PORT',8000))
@app.route('/')
def main():
     
     return render_template('register.html')


@app.route('/handle_data', methods=['POST'])
def reply():
     x = request.form['inputID']
     sample=start_work(x)
     k=sample[0]
     if k =="error":
         k="User you entered has not made any tweets recently."
         sample.append(" ")
     elif k=="depressed":
         k="Person is Depressed"
     else:
         k="Person is not Depressed"
         
     try:
         return  render_template('out.html',plane=k, plane2=sample[1].to_html())
     except:
         return  render_template('out.html',plane=k)
    # print(sample)
    #return render_template('out.html',plane=sample)



if __name__ == "__main__":
	app.run(port=5004)
