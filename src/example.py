from container import Component, Autowired, Resource, container
from value import Value

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

client = container.get_bean("Client")
print(container.get_bean("MessageService").message)
print(container.get_bean("ConfigService").config)
