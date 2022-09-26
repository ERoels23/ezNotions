from copy import deepcopy
import ast
import ujson
import cloudpickle

class ezFrame:
    address = None  # stack memory address of the frame
    line = None     # line number in the file
    eType = None    # line, return, etc.
    caller = None   # caller function for this frame
    current = None  # current function being run
    file = None     # full filepath of current file
    locs = []       # contain local variables
    locaddrs = []   # contain addresses of local variables
    args = []       # local arguments for 'current' function

    def __init__(self, frame, event, arg):
        # requires a live frame object in order to instantiate
        self.line = frame.f_lineno
        self.caller = frame.f_back
        self.eType = event
        self.current = frame.f_code.co_name
        
        self.address = id(frame)

        # we also need to record the addresses of each variable, to find pointers
        self.locaddrs = {}

        for k in frame.f_locals.keys():
            # this should be giving us the actual memory address now...
            self.locaddrs[k] = id(frame.f_locals[k])

        # attempting to skirt the deepcopy TypeError
        self.locs = cloudpickle.dumps(frame.f_locals)
        self.locs = cloudpickle.loads(self.locs)
        # seems like that's working... for now
        
        self.args = arg
        self.file = frame.f_code.co_filename

    def ezPrint(self):
        ret = "PROGRAM SNAPSHOT:\n"
        ret += f"ADDRESS: {self.address}\n"
        ret += f"LINE NO: {self.line}\n"
        ret += f"TYPE   : {self.eType}\n"
        ret += f"CURFUNC: {self.current}\n"
        ret += f"PARENT : {self.caller}\n"
        ret += f"ARGS   : {self.args}\n"
        ret += f"FILE   : {self.file}\n"
        ret += f"LOCALS : {str(self.locs)}\n"
        print(ret)
