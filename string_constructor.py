#!/usr/bin/env python3
"""wrapper for StringConstructor class"""


class StringConstructor(object):
    """Generates all possible sequences of strings from a set of characters"""

    # Constructor requires:
    # 1. starting string length, must be > 0 and <
    #   2. ending string length, must be > 0 and >= min_length
    #   3. a list containing the characters to create strings with,
    #       must have >= 2 elements and cannot contain duplicates
    def __init__(self, min_length, max_length, character_list):
        self.min_length = min_length
        self.max_length = max_length
        self.current_length = min_length
        self.character_list = character_list
        self.current_string = "\0"
        # add parameter validation for lengths
        # ensure list >=2 characters and distinct and does not contain "\0"

    def increment_char(self, i, char_pos, beyond_string):
        """internal function used by next(). Char incrementing and carry"""
        if not beyond_string:
            # char is at end of string
            if i == 1:
                self.current_string = self.current_string[:-1] + \
                    self.character_list[char_pos + 1]
            # char is at start of string
            elif i == self.current_length:
                self.current_string = self.character_list[char_pos + 1]
                for char in range(self.current_length - i + 1,
                                  self.current_length):
                    self.current_string += self.character_list[0]
            # char is in middle of string
            else:
                self.current_string = self.current_string[
                    :self.current_length - i] +  \
                    self.character_list[char_pos + 1]
                for char in self.current_string[:i - 1]:
                    self.current_string += self.character_list[0]
        # if position was beyond the string, expand the string up to max
        else:
            # return empty string to indicate exhaustion of strings
            if self.current_length == self.max_length:
                self.current_string = ""
            # otherwise create the new starting string
            else:
                self.current_length += 1
                self.current_string = ""
                for char in range(self.current_length):
                    self.current_string += self.character_list[0]

    def next_string(self):
        """constructs and returns the next string in the sequence"""
        if self.current_string == "\0":
            # create initial string with repetition of first character
            self.current_string = ""
            for char in range(self.min_length):
                self.current_string += self.character_list[0]
        else:
            i = 1
            beyond_string = False
            # check last char for position in chars list
            last_char = self.current_string[-i]
            char_pos = self.character_list.index(last_char)
            # char is in last position; iterate until a non end of list char is
            # found in the string
            while char_pos == (len(self.character_list) - 1) and not \
                    beyond_string:

                # cannot find char if it is beyond the string size
                if i < self.current_length:
                    i += 1
                    last_char = self.current_string[-i]
                    char_pos = self.character_list.index(last_char)
                else:
                    beyond_string = True

            # increment char in iterated position
            self.increment_char(i, char_pos, beyond_string)

        return self.current_string
