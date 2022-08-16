import sample
import sys
from ezFrame import ezFrame
from assignment import assignment
from ezEvent import ezEvent
import inspect as ins
from pprint import pprint as pp

def trace(f, verbose):
    # tracing function, 
    # TODO: inside main(), I know, but I'd have to rewrite it otherwise
    def mytrace(frame, event, arg):
        # currently excludes calls to built-in functions.
        if (frame.f_code.co_filename == currFile or frame.f_back.f_code.co_filename == currFile)\
                or (frame.f_code.co_filename == currFileMac or frame.f_back.f_code.co_filename == currFileMac):
            ez = ezFrame(frame, event, arg)
            ezFrames.append(ez)

        return mytrace
    
    ezFrames = []

    # may also need to change to Mac syntax if on Mac
    currFile = "c:\\Users\\Eric\\Desktop\\NOTIONS\\ezNotions\\" + f
    currFileMac = "/Users/Eric/NOTIONS/ezNotions/" + f

    # ensure that custom trace function is being used
    sys.settrace(mytrace)
    # run the sample python program, tracing as we go
    # TODO: how do we ensure that we trace the user-given file?
    sample.run()

    # pop out the first and last, because it's just call/return for run() in the target file, not useful
    """ 
    ezFrames.pop(0)
    ezFrames.pop(-1) 
    """
    # ugh okay actually these are kinda useful, because we occassionally need the previous or next frame
    # in order to fully define an assignment or function call
    if verbose:
        for frame in ezFrames:
            frame.ezPrint()

    '''
    TODO: this entire section of code below is a mess
    it relies almost entirely on manual entries, isn't generalized at all,
    and I don't even know how to get the trace function to run/import a file 
    provided to us by this user...
    '''
    
    # event creation and frame allocation is currently done manually
    # each frame must be given an event type (ie. "assign", "funccall", "funcdef", "classdef")
    event1 = assignment()
    event2 = assignment()
    event3 = assignment()
    event4 = assignment()

    eventList = []
    eventList.append(event1)
    eventList.append(event2)
    eventList.append(event3)
    eventList.append(event4)

    # remember, there is a single trace for each assignment,
    # and the first and last trace are always calling and returning from run()
    event1.add([ezFrames[1], ezFrames[2]])
    event2.add([ezFrames[2], ezFrames[3]])
    event3.add([ezFrames[3], ezFrames[4]])
    event4.add([ezFrames[4], ezFrames[5]])

    # add and analyze are now two separate functions, making it more flexible
    for e in eventList:
        e.analyze()

    # uses the __repr__ of ezEvent to print Event descriptions
    print(f"\nRESULTS from [{f}]:")
    print(str(event1))
    print(str(event2))
    print(str(event3))
    print(str(event4))

    print("\nTRACE RESULTS:")
    print("Successfully Traced.")
    print(f"{len(ezFrames)} frames found.")

    return eventList

if __name__ == "__main__":
    # default filename provided when running this file
    # verbose is also set to True by default
    trace("sample.py", True)