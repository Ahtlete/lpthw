class Room(object):

    def __init__(self, name, descripthion):
        self.name = name
        self.descripthon = descripthion
        self.paths = {}

    def go(self, direction):
        return  self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)