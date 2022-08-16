import pytest
from assignment import assignment
from tracing import trace

'''
Goals:
- be able to provide a filename for trace sample
- be able to extract data from runtime to complete the test
'''

# call the tracing function like this:
# events1 = trace("sample.py", False)
# all of the events get returned in a list

def test_sample():
    events = trace("sample.py", False)
    dumbyAssign = assignment()
    assert type(events[0]) == type(dumbyAssign)

def test_output():
    events = trace("sample.py", False)
    assert str(events[0]) == "New variable 'x' was assigned value of '1'"

# quick example test to make sure I know how to use pyTest...
def test_1():
    x = 1
    y = x 
    assert (y is x)
