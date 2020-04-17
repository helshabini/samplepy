from flask import Flask
app = Flask(__name__)


@app.route('/')
def helloworld():
    return 'Hello, World!'

@app.route('/json')
def json():
   return """
{
    values: [{
        value1,
        value2,
        value3
    }]
}
   """

if __name__ == '__main__':
   app.run()