import json
from finite_state_machine import FiniteStateMachine


#load the machine and input data
file = open('data.json')
data = json.load(file)
file.close()

#Create new machine
fsm = FiniteStateMachine(data["rules"], data["initial"])

#Run machine on inputs
for i in data["inputs"]:
    fsm.next(i)
