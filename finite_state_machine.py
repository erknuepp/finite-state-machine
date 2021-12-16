class FiniteStateMachine:
    def __init__(self, rules: dict, initial: str):
        '''
        Creates a finite state machine with
        and inital state and a set of rules
        to control state based on an input

        keyword arguments
        inital: the intial state of the machine
        rules: the rules for setting state
        '''
        self.state = initial
        self.rules = rules

    def next(self, i: str):
        '''
        Gets the next state based on the current state
        and an input

        keyword arguments
        i: the input to determine the next state
        '''
        current_state = self.state
        next_state = self.rules[current_state][i]
        self.state = next_state
        print(i, ":", current_state, "->", next_state)
