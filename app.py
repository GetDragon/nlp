import nltkmodules

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

from summary_sumy import SumyHelper

@app.route('/') 
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/summary', methods=['POST'])
def summary():
   batch = request.data.decode("utf-8")
   try:
      sumy = SumyHelper()
      return sumy.Execute(batch)
   except BaseException as err:
      return bytes(err.user_message, "utf-8")

if __name__ == '__main__':
   app.run()