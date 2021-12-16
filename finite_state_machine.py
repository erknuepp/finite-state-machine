class FiniteStateMachine:
    def __init__(self, rules, initial):
        self.state = rules[initial]
        self.rules = rules

    def next_method(self, i):
        self.state = self.rules[i]