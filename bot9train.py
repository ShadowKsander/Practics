from enum import Enum

class State(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6
    H = 7


class StateMachine:
    state = State.A

    def tag(self):
        return self.update({
            State.A: [State.B, 0],
            State.B: [State.E, 5]
        })

    def group(self):
        return self.update({
            State.A: [State.C, 3],
            State.C: [State.E, 7],
            State.D: [State.E, 8],
            State.G: [State.H, 11]
        })

    def shift(self):
        return self.update({
            State.A: [State.D, 1],
            State.F: [State.G, 10]
        })

    def punch(self):
        return self.update({
            State.B: [State.C, 4],
            State.C: [State.D, 6],
            State.A: [State.E, 2],
            State.E: [State.F, 9]
        })

    def update(self, transitions):
        self.state, signal = transitions[self.state]
        return signal

def main():
    return StateMachine()

o = main()

print(o.tag()) # 0
print(o.punch()) # 4
print(o.punch()) # 6
print(o.group()) # 8

# from enum import Enum
#
# class State(Enum):
#    A = 0
#    B = 1
#    C = 2
#    D = 3
#    E = 4
#    F = 5
#    G = 6
#    H = 7
#
# class StateMachine:
#    state = State.A
#
#    def xuy(self):
#        return self.update({
#            State.A: [State.E, 3],
#        })
#
#
#    def update(self,transitions):
#        self.state, signal = transitions[self.state]
#        return signal
#
# def main():
#    return StateMachine





