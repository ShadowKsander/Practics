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

    def fork(self):
        return self.update({
            State.A: [State.B, 0],
            State.E: [State.G, 7],
            State.F: [State.G, 8],
            State.H: [State.B, 11],
        })

    def log(self):
        return self.update({
            State.A: [State.G, 1],
            State.B: [State.C, 2],
            State.D: [State.E, 4],
        })

    def peep(self):
        return self.update({
            State.C: [State.D, 3],
            State.D: [State.A, 5],
            State.E: [State.F, 6],
            State.G: [State.H, 10],
            State.F: [State.B, 9],
        })

    def update(self, transitions):
        self.state, signal = transitions[self.state]
        return signal


def main():
    return StateMachine()

o = main()
print(o.fork())
print(o.log())
print(o.peep())
print(o.fork())