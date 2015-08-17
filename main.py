#!/usr/bin/env python3
#formerly "ssd.py"
"""Attempts to bruteforce unlock ssd"""


MIN_LENGTH = 8
MAX_LENGTH = 16


def create_ascii_code_list(debug_obj):
    """returns a list of characters by cycling through printable ascii codes"""

    ascii_code_list = []
    pos_counter = 0
    for each in range(32, 126):

        debug_output_variable_info_dict = {"ascii_code_list": "iteration"}
        debug_output_origin = {"Origin": "create_ascii_code_list"}
        debug_output_string = {"pos_counter": pos_counter}
        debug_obj.debug_output(debug_output_origin,
                               debug_output_variable_info_dict,
                               debug_output_string)

        debug_output_variable_info_dict = {"ascii_code_list": "general"}
        debug_output_origin = {"Origin": "create_ascii_code_list"}
        debug_output_string = {"ascii": each, "char": chr(each)}

        debug_obj.debug_output(debug_output_origin,
                               debug_output_variable_info_dict,
                               debug_output_string)
        ascii_code_list.extend(chr(each))
        pos_counter += 1

    debug_output_variable_info_dict = {"ascii_code_list": "general"}
    debug_output_origin = {"Origin": "create_ascii_code_list"}
    debug_output_string = ascii_code_list
    debug_obj.debug_output(debug_output_origin, debug_output_variable_info_dict,
                           debug_output_string)


class Debugging(object):
    """Handles all debugging output"""
    def __init__(self):
        self.dict_flags = {}
        return

    def set_flag(self, var_name, var_flag):
        """Manually set individual flags"""
        self.dict_flags[var_name] = var_flag

    def debug_output(self, call_origin_dict, variable_info_dict, user_defined):
        """Filters and prints debug info"""
        #Args: Dictionary, Dictionary, Any:
        #1) 'Origin':func name -- this is information about the function calling
        #   the debugger. Key MUST be 'Origin'.
        #2) Name: information Type -- for managing/filtering/silencing by name
        #   or type
        #3) Stuff
        #example: Origin:'create_ascii_code_list', 'ascii_code_list':'iteration'
        #   (this info comes from inside a counting loop), [1,2,3,4,5]
        #okay, so maybe I like dictionaries a little too much. Sue me.

        if self.dict_flags["debugTheDebugOutput"]:
            print("debugTheDebugOutput>", "call_origin_dict:", call_origin_dict,
                  "var_name:", variable_info_dict, "user_defined:",
                  user_defined, "varDebugFlag:")

        for var_name in variable_info_dict.keys():
            if self.dict_flags[variable_info_dict[var_name]]:
                print(call_origin_dict["Origin"], ">", "(" + variable_info_dict[
                    var_name] + ")", var_name, ":", user_defined)


def assemble_string():
    """concatenates cycled characters"""
    return


def print_string():
    """dummy function. probably replace with debug_output call"""
    return


def activate_debugging():
    """Initialize debug level flags"""
    debugger = Debugging()
    debugger.set_flag("iteration", False)
    debugger.dict_flags["debugTheDebugOutput"] = False
    debugger.dict_flags["general"] = True
    return debugger


def main():
    """Main needs a docstring?"""
    print("checkpoint 0 (program load)")
    debugger = activate_debugging()
    create_ascii_code_list(debugger)
    print("checkpoint 1 (right now this means done)")
    return 0


if __name__ == '__main__':
    main()

#printables are 32-126. Skip characters we know are not in it. See EOF for list.
#known not used: 32 (space)

#hdparm command
#sudo hdparm --user-master u --security-disable <password> /dev/sdc
