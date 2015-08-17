#!/usr/bin/env python3
"""Recursion for bruteforcer, under construction"""
import time


def Im_a_loop(current_depth, max_depth, word):
##    print (word)
    if current_depth >= (max_depth):
        return word

    for num in range(10):
        word1 = word + str(num)
#        print ("curr:" + str(current_depth), "max:", max_depth, "range:",
#               max_depth - current_depth, "word:", word, "word1", word1)
##        print ("curr:", word1)
        Im_a_loop(current_depth + 1, max_depth, word1)
    return str(word)


def main():
    """Main needs a docstring?"""
    print("checkpoint 0 (program load)")
    time_start = time.time()
    x = Im_a_loop(0, 20, "")
    time_stop = time.time()
    time_lapsed = time_stop - time_start
    print("time_start:", time_start)
    print("time_stop:", time_stop)
    print("time_lapsed:", time_lapsed)
    print ("x",x)
    print("checkpoint 1 (right now this means done)")
    return 0


if __name__ == '__main__':
    main()
