import json, config
from flask import Flask, request, render_template

class App:
    def __init__(self,name,filename=None,port=None,host=None):
        # Every app has a name
        self.name = name
        self.events = config.events

        if filename:
            self.filename = filename
            self.state = json.load(open(filename))
        else:
            self.state = None

        # If host or port is given, initate a Flask app
        if host or port:
            self.app = Flask(self.name)

        if host:
            self.host = host
        else:
            self.host = config.DEFAULT_HOST
        # If port is given set port to that
        if port:
            self.port = port
        else:
            self.port = config.DEFAULT_PORT

    def on(self,event,function):
        if event in self.events.keys():
            self.events[event].append(function)
        else:
            raise ValueError("Couldn't add event:" + event + ", because it doesn't exist")

    def __react_to_event__(self,event):
        for event_reaction in self.events[event]:
            event_reaction(self)

    def start(self):
        self.__react_to_event__('start')

    def shutdown(self):
        self.__react_to_event__('shutdown')

    def route(self,rule,endpoint,view_func):
        self.app.add_url_rule(rule,endpoint,view_func)
