class PropertyResolver:
    def __init__(self, properties):
        self.properties = properties

    def resolve(self, key):
        return self.properties.get(key)
