def Value(name, value):
    def decorator(cls):
        setattr(cls, name, value)
        return cls
    return decorator