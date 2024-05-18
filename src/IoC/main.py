class BeanDefinition:
    def __init__(self, bean_class):
        self.bean_class = bean_class
        self.dependencies = []

    def add_dependency(self, dependency):
        self.dependencies.append(dependency)

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
        return bean_instance

