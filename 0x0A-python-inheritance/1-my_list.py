#!/usr/bin/python3
"""class MyList that inherits from list:"""


class MyList(list):
    """class than inherits from list"""

    def print_sorted(self):
        """method that print the list sorted"""
        print(sorted(self))
