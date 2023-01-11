def lookup(obj):
    """
    This function takes an object as an argument
    and returns a list of all attributes and
    methods of that object.
    :param obj: any object
    :return: list of attributes and methods of obj
    """
    attributes = []
    methods = []
    for name in dir(obj):
        """
        Iterating through all attributes and methods of the object.
        """
        item = getattr(obj, name)
        """
        Getting the value of the attribute or method with that name.
        """
        if callable(item):
            methods.append(name)
        else:
            attributes.append(name)
    return attributes + methods
