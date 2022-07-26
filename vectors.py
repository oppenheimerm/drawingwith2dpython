from math import sqrt, sin, cos, atan2

# deprecated
#def add(v1,v2):
#    return (v1[0] + v2[0], v1[1] + v2[1])

def subtract(v1,v2):
    return (v1[0] - v2[0], v1[1] - v2[1])

def add(*vectors):
    return (sum([v[0] for v in vectors]), sum([v[1] for v in vectors]))

def translate(translation, vectors):
    return [add(translation, v) for v in vectors]

def length(v):
    return sqrt(v[0]**2 + v[1]**2)

def distance(v1,v2):
    return length(subtract(v1,v2))

def scale(scalar, v):
    return(v[0]*scalar, v[1]*scalar)