class FiniteStateMachine:
    def __init__(self, rules, initial):
        self.state = initial
        self.rules = rules

    def next_method(self, i):
        current_state = self.state
        next_state = self.rules[current_state][i]
        self.state = next_state
        print(i, ":",current_state,"->",next_state)