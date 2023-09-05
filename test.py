Import("env")

def pass_through(node):
    print("Node '%s'" % (node.name))
    #print("Type: " + str(type(node)))
    # pass through works fine
    #return node
    # wrapped in env.Object() fails, even when not modfying settings
    return env.Object(node)

env.AddBuildMiddleware(pass_through)