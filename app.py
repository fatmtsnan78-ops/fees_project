from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def login():
    return render_template('login.html')
@app.route('/login',methods=['POST'])
def handle_login():
    return render_template('pay.html')
@app.route('/student')
def student_dashboard():
  return render_template('pay.html')
@app.route('/pay')
def pay_page():
  return render_template('pay.html')
if __name__=="__main__":
  app.run(debug=True)
     
