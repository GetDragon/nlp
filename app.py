import nltkmodules

from flask import Flask, render_template, request, jsonify, make_response
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
      p = int(request.args.get("p"))
      type = request.args.get("type")
      return jsonify(
        type=type,
        text=sumy.Execute(type, batch, p)
      )
   except BaseException as err:
      return make_response(err, 200)

if __name__ == '__main__':
   app.run()