import sample
import sys
import inspect
from ezFrame import ezFrame
from assignment import assignment
from ezEvent import ezEvent
import inspect as ins
from pprint import pprint as pp

def trace(filename, verbose):

    global ezFrames
    ezFrames = []

    def make_my_trace(fn):
        def mytrace(frame, event, arg):
            if ((fn in frame.f_code.co_filename) or (fn in frame.f_back.f_code.co_filename)):
                ez = ezFrame(frame, event, arg)
                ezFrames.append(ez)
            return mytrace
        return mytrace

    # ensure that custom trace function is being used
    def do_trace(fn):
        traceFunc = make_my_trace(fn)
        sys.settrace(traceFunc) # set tracer to be custom trace func
        sample.run() # the current crutch, not sure how to run a file without being able to import it
        sys.settrace(None)


    # function calls begin HERE
    do_trace(filename)

    if verbose:
        for frame in ezFrames:
            frame.ezPrint()
    

    '''
    For Gabe:

    TODO: This is where code event interpolation will go
    at this point in the code:
    - all frames are contained in the list 'ezFrames'
    - interpolater needs to analyze multiple frames, break it up into events
    - for each event found, the associated object should be constructed (ie. assignment())
    - ezEvent.add() can be used to add frames to an event object
        - add() will accept: a list of frames, 1 frame, or an entire nested event
    - once all of the relevant frames have been added to an event object:
        - ezEvent.analyze() (abstract, implemented in child classes) will analyze the frames
        - the __repr__ will then be set to a neat description of the event in question
        - ex: for an assignment(): "New variable 'x' was assigned value of '2'"

    Here's a breakdown of all the files and what they're responsible for:
    tracing.py: contains the tracing functions, creates event objects, runs sample file, etc.
    ezFrame.py: class file for the ezFrame object, check class variables for more info
    ezEvent.py: class file for the ezEvent object, parent class to the below files:
        assignment.py
        funccall.py
        funcdef.py
        classdef.py
        - all of which should be mostly self-explanatory
        - each one needs a working analyze() function
    test_trace.py: holds any and all pyTest tests (filename must begin with 'test')
    sample.py: currently, this contains the run() function that gets traced
        - put the code that you want to trace within this file
    short.py: leftover from my own testing, not necessary
    '''

    # event creation and frame allocation is currently done manually
    # each frame must be given an event type (ie. "assign", "funccall", "funcdef", "classdef")
    event1 = assignment()

    eventList = []
    eventList.append(event1)

    # first and last traces are ALWAYS calling and returning from run()
    event1.add(ezFrames[1])
    event1.add(ezFrames[2])

    # organize events into a list so that you can do this:
    for e in eventList:
        e.analyze()

    # uses the __repr__ of ezEvent to print Event descriptions
    print(f"\nRESULTS from [{filename}]:")
    for e in eventList:
        print(e)
    print("\nTRACE RESULTS:")
    print(f"{len(ezFrames)} frames found.")

    return eventList

if __name__ == "__main__":
    # default filename provided when running this file
    # verbose output is also set to True by default
    trace("sample.py", True)