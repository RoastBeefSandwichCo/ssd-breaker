#!/usr/bin/env python3
#TODO: commandnd-line invocation & paramters


"""Test the string_constructor module"""
import string_constructor
from subprocess import call
#import sys

TEST_1 = string_constructor.StringConstructor(2, 2, ["0", "1"])
TEST_2 = string_constructor.StringConstructor(1, 3, ["a", "b", "c"])
TEST_3 = string_constructor.StringConstructor(4, 6, ["a", "b", "c", "1", "2",
                                                     "3"])
#UNUSED_CHAR_LIST = [' ', '-', '\\', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '{', '|', '}']
UNUSED_CHAR_LIST = [' ', '-', '\\', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '.', '/', '?', '{', '|', '}']#TODO: separate unused (in my pw) from actually invalid characters



def create_ascii_code_list():
    """returns a list of characters by cycling through printable ascii codes"""
    unused_chars = []
    ascii_chars_list = []
    for each in range(32, 126):
        this_char = chr(each)
        if not this_char in UNUSED_CHAR_LIST:
            ascii_chars_list.extend(this_char)
            #print ("%s not in unused" % (this_char), UNUSED_CHAR_LIST)
        elif this_char in UNUSED_CHAR_LIST:
            #print ("found %s in UNUSED_CHAR_LIST" % (this_char))
            unused_chars.extend(this_char)
    
    print ("using charset: ", ascii_chars_list)
    print ("disqualified: ", unused_chars)
    print("because they are in this list: ", UNUSED_CHAR_LIST)
    return ascii_chars_list


def hawkes_tests():
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


def Leons_bf_function():
    characters = create_ascii_code_list()
    print("doing stuff now!")
    resume_string = "zzzzzzz" #Must be something or False
    max_length = 1
    start_length = 1 #minimum is 1
    #FIXME: with screwy start/max_length values, this thing acts funny! Implement error-checking.
    
    if resume_string: #TODO: clean this up. Looks like shit. Fine for a draft, though.
        Leon_test = string_constructor.StringConstructor(len(resume_string), max_length, characters)
    else:
        Leon_test = string_constructor.StringConstructor(start_length, max_length, characters)

    #override test
    if resume_string:
        Leon_test.current_string = resume_string
        
    string = Leon_test.next_string()

    while string != "":
        string = Leon_test.next_string()
        hdparm_exit_code = call(["sudo", "hdparm", "--user-master", "m", "--security-unlock", string, "/dev/sdc"])
#        print ("EXIT CODE!", hdparm_exit_code)
        # if hdparm_exit_code == 5:  #verify exit code comparison.
        #     print("FAILED! Exit code verified. STRING = ", string)
        #     return string
        if hdparm_exit_code == 0:
            print ("exit code is triggering return")
            print("HOLY GUS TARBALLS!! IT WORKED! STRING = ", string)
            return string
    print ("DONE.")
    return "Cycling finished without successful unlock"


def main():
    """Run string_constructor module tests"""
    #hawkes_tests()
    attempt = Leons_bf_function()
    print ("Leons_bf_function returned! That SHOULD mean a success.")
    print ("result:", attempt)
    with open("STRING.TXT", 'w') as f:
        x = f.write(attempt)


if __name__ == '__main__':
    main()  # run self-test
