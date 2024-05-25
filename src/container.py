class BeanDefinition:
    def __init__(self, bean_class):
        self.bean_class = bean_class
        self.dependencies = []
        self.properties = {}
        self.resources = {}

    def add_dependency(self, dependency):
        self.dependencies.append(dependency)

    def add_property(self, name, value):
        self.properties[name] = value

    def add_resource(self, name, resource):
        self.resources[name] = resource

    def __repr__(self):
        return f'BeanDefinition({self.bean_class.__name__}, {self.dependencies})'


class Container:
    def __init__(self):
        self.bean_definitions = {}

    def register(self, bean_class):
        bean_name = bean_class.__name__
        self.bean_definitions[bean_name] = BeanDefinition(bean_class)

    def get_bean(self, bean_name):
        bean_definition = self.bean_definitions.get(bean_name)
        if not bean_definition:
            raise Exception(f'Bean {bean_name} not found')
        bean_instance = bean_definition.bean_class()
        dependencies = {}
        for dependency_class in bean_definition.dependencies:
            dependencies[dependency_class.__name__] = self.get_bean(dependency_class.__name__)
        for dependency_name, dependency_instance in dependencies.items():
            setattr(bean_instance, dependency_name, dependency_instance)
        for property_name, property_value in bean_definition.properties.items():
            setattr(bean_instance, property_name, property_value)
        for resource_name, resource_value in bean_definition.resources.items():
            setattr(bean_instance, resource_name, resource_value)
        return bean_instance


def Component(cls):
    container.register(cls)
    return cls


def Autowired(bean_class):
    container.bean_definitions[func.__name__].add_dependency(bean_class)
    return bean_class


def Value(name, value):
    def decorator(cls):
        container.bean_definitions[cls.__name__].add_property(name, value)
        return cls
    return decorator


def Resource(name, resource):
    def decorator(cls):
        container.bean_definitions[cls.__name__].add_resource(name, resource)
        return cls
    return decorator