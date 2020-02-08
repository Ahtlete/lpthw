directions = ('north', 'east', 'west', 'south')
verbs = ('go', 'stop', 'kill', 'eat')
nouns = ('door', 'bear', 'princess')

def scan(inputs):
    words = inputs.split()
    result = []
    for word in words:
        if word in directions:
            result.append(('direction', word))
        elif word in verbs:
            result.append(('verb', word))
        else:
            result.append(('noun', word))
    return result