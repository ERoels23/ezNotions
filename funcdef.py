from ezEvent import ezEvent

class funcdef(ezEvent):
    def __init__(self) -> None:
        super().__init__()

    def add(self, frames):
        # call parent function to add frames (generic behavior)
        super().add(frames)
        # TODO: type-specific checks


    def analyze(self):
        # new stack pointer, call type, curfunc for name
        # need: function name, argument names, return value name (if applicable)
        ez1 = self.frameList[0]
        ez2 = self.frameList[1]

        # format: line with almost no info,
        # then line no. skips >1, another line with funcName as a local variable

        # obtain name of new function, it's recorded as a new local variable
        newFunc = {k: ez2.locs[k] for k in set(ez2.locs) - set(ez1.locs)}
        funcName = list(newFunc.keys())[0]

        self.strRepr = f"New custom function '{funcName}()' defined"

    def __str__(self):
        return self.strRepr

    def __repr__(self):
        return self.strRepr
