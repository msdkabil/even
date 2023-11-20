from flask import Flask, request, render_template
import requests

app = Flask(__name__)
  
@app.route('/', methods =["GET", "POST"])
def index(): 
    n=int(input("Enter the value of n:")
    for(i in range(1,2n+1):
        if((i%2)==0)
          print(i,end=" ")

if __name__ == "__main__":
    app.run()
