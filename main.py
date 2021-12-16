import json
from finite_state_machine import FiniteStateMachine

file = open('data.json')
data = json.load(file)
initial = data["initial"]
rules = data["rules"]
inputs = data["inputs"]

fsm = FiniteStateMachine(rules, initial)
for i in inputs:
    fsm.next_method(i)
