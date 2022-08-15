from ezEvent import ezEvent

class funccall(ezEvent):
    def __init__(self) -> None:
        super().__init__()

    def add(self, frames):
        # call parent function to add frames (generic behavior)
        super().add(frames)
        # TODO: type-specific checks

    def analyze(self):
        # TODO: analyze a function call
        return None

    def __str__(self):
        return self.strRepr

    def __repr__(self):
        return self.strRepr
