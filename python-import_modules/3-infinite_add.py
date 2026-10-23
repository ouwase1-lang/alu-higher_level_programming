#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    total = 0
    for arg in sys.argv[1:]:
        total += int(arg)
    print("{}".format(total))
