def lookup(obj):
    attributes = []
    methods = []
    for name in dir(obj):
        item = getattr(obj, name)
        if callable(item):
            methods.append(name)
        else:
            attributes.append(name)
    return attributes + methods
