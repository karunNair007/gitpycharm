from flask import Flask,request,render_template

kk=Flask(__name__)

@kk.route('/')
def webcontent():
    return "welcome"

if __name__=="__main__":
    kk.run(debug=True)

