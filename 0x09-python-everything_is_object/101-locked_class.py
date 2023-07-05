#!/usr/bin/python3

class LockedClass:
    """
    LockedClass that prevents dynamic creation of instance attributes
    except for 'first_name'.
    """
    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("'LockedClass'no attribute '{}'".format(name))
        super().__setattr__(name, value)
