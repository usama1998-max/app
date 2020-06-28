from flask import Flask,render_template,url_for

master=Flask(__name__)

@master.route('/')
def web():
  return render_template("web.html")

if __name__=='__main__':
    master.run(debug=True)