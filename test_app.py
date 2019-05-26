from App import App
import config
import json

app = App('myApp','myApp.json',5000,'0.0.0.0')
def test_init():
    assert app.state == json.load(open('myApp.json'))
    assert app.filename == 'myApp.json'
    assert app.events == config.events
    assert app.port == 5000
    assert app.host == '0.0.0.0'

def test_on():
    def log_start(app):
        print("Started {}\nWeb server lives on: {}:{}\nLoaded state: {}".format(app.name,app.host,app.port,app.state))
    app.on('start',log_start)
    assert app.events['start'][0] == log_start
    app.start()
