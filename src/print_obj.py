def print_obj(obj, namespace):
    variable_name = [name for name in namespace if namespace[name] is obj]
    print (variable_name, "=", obj)
    return

