import os, sys

sys.path.insert(0, os.getcwd())

from script import addition


def test_add():
    subj = addition(7, 9)
    print(subj)
    assert subj == 16


test_add()
