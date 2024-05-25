from container import Container
from value import Value

container = Container()


@Component
class ServiceA:
    def __init__(self):
        self.name = "ServiceA"


@Component
class ServiceB:
    def __init__(self):
        self.name = "ServiceB"


@Component
class Client:
    @Autowired
    def __init__(self, service_a: ServiceA, service_b: ServiceB):
        self.service_a = service_a
        self.service_b = service_b


@Value("message", "Hello, World!")
class MessageService:
    pass


@Resource("config", {"key": "value"})
class ConfigService:
    pass

client = container.get_bean("Client")
print(MessageService().message)
print(ConfigService().config)