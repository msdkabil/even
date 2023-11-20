from flask import Flask

app = Flask(__name__)
  
@app.route('/')

def hello():
    """Return a friendly HTTP greeting."""
    i=0
    n=10
    b=[]
    while(n>0):
        a=n*2
        b[i]=a
        n-=1
        i+=1
    return(b)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
