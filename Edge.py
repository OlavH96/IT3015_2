class Edge:

    def __init__(self, fromState, toState, content):
        self.fromState = fromState
        self.toState = toState
        self.content = content

    def __str__(self):
        return "Edge{from=" + str(self.fromState) + ", to=" + str(self.toState) + ", content=" + str(self.content) + "}"

    def __eq__(self, other):
        return hash(self)==hash(other)

    def __hash__(self):
        return hash((self.fromState, self.toState, self.content))
