# ezNotions
code repo for ERoels23.github.io (Notional Machines Research)

    tracing.py:
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
