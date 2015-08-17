#!/usr/bin/env python3
"""Test the string_constructor module"""
import string_constructor

TEST_1 = string_constructor.StringConstructor(2, 2, ["0", "1"])
TEST_2 = string_constructor.StringConstructor(1, 3, ["a", "b", "c"])
TEST_3 = string_constructor.StringConstructor(2, 2, ["a", "b", "c", "1", "2",
                                                     "3"])


def main():
    """Run string_constructor module tests"""
    # test same lengths
    string = TEST_1.next_string()
    print(string)
    while string != "":
        string = TEST_1.next_string()
        print(string)

    # test a small sample
    string = TEST_2.next_string()
    print(string)
    while string != "":
        string = TEST_2.next_string()
        print(string)

    # test a larger sample
    string = TEST_3.next_string()
    print(string)
    while string != "":
        string = TEST_3.next_string()
        print(string)

if __name__ == '__main__':
    main()  # run self-test
