from ezFrame import ezFrame
import abc #abstract base classes

class ezEvent:
    types = ["assign","funcdef","classdef","funccall"]

    '''
    assign: (poss: pointer)
    funcdef: (poss: class method)
    classdef: (no variants, but it's complicated enough...)
    funccall: (poss: instantiate, method, )  
    '''

    # assignment
    # definition (class or function, but might look similar)
    # function call
    # 

    def __init__(self):
        '''
        only requires type of object before definition, adding frames comes later
        '''
        self.frameList = []
        self.strRepr = "Default String"

    def add(self, f):
        # generic setup, collect ezFrames/Events in one place
        try:
            if isinstance(f, ezFrame) or isinstance(f, ezEvent):
                # might append ezEvent to an ezEvent 
                # (ex: func def within class def, constructor call within assignment, etc.)
                self.frameList.append(f)
            elif isinstance(f, list):
                self.frameList += f
        except:
            raise TypeError("ezEvent 'add()' requires ezFrame or list of ezFrames")

    @abc.abstractmethod
    # doesn't NEED to be abstract, but works well in this case
    def analyze():
        pass

    def __str__(self):
        return self.strRepr

    def __repr__(self):
        return self.strRepr
