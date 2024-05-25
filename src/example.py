from container import Component, Autowired, Resource, container
from value import Value
from flask import *

app = Flask(__name__)
@Component
class ServiceA:
    def __init__(self):
        self.name = "ServiceA"


@Component
class ServiceB:
    def __init__(self):
        self.name = "ServiceB"


@Autowired(ServiceA)
@Autowired(ServiceB)
@Component
class Client:
    def __init__(self):
        pass


@Value("message", "Hello, World!")
@Component
class MessageService:
    pass


@Resource("config", {"key": "value"})
@Component
class ConfigService:
    pass

@app.route('/')
def index():
    return container.get_bean("MessageService").message

app.run(app, port=80, host='0.0.0.0')