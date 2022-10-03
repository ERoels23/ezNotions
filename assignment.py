from ezEvent import ezEvent

class assignment(ezEvent):
    def __init__(self) -> None:
        super().__init__()

    def add(self, frames):
        # call parent function to add frames (generic behavior)
        super().add(frames)
        # maybe throw in some assignment-specific checks
        if len(self.frameList) > 2:
            print("WARNING: too many frames given for assignment, using first 2")

    def analyze(self):
        isPointer = False
        # only two frames to worry about with assignment
        ez1 = self.frameList[0]
        ez2 = self.frameList[1]

        # dictionary comprehension to get new variable name/value
        newvar = {k: ez2.locs[k] for k in set(ez2.locs) - set(ez1.locs)}

        newName = list(newvar.keys())[0]
        newVal = list(newvar.values())[0]

        # here is where we could probably make sure it's a variable
        # because a funcDef also gets picked up here
        if type(newVal) == type(add):
            # need to quit the assignment creation!
            # AAAAAA abort, this should be a funcDef!!

        newID = 0
        oldName = 0

        # check if new variable is pointer to old variable
        for tup in ez2.locaddrs.items():
            if tup[0] == newName:
                newID = tup[1]

        for tup in ez2.locaddrs.items():
            if tup[1] == newID and tup[0] != newName:
                isPointer = True
                oldName = tup[0]

        # create string representation from analysis
        self.strRepr = f"New variable '{newName}' was assigned value of '{newVal}'"
        if isPointer:
            self.strRepr += f" (points to '{oldName}')"

    def __str__(self):
        return self.strRepr

    def __repr__(self):
        return self.strRepr

