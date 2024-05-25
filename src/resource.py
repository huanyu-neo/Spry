def Resource(name, resource):
    def decorator(cls):
        setattr(cls, name, resource)
        return cls
    return decorator
