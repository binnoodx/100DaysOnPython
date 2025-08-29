### __name__ = "__main__"


# while importing module from another file , whole file run. So to prevent from hey function to double run we use if __name__ == __main__ hey() to prevent from double run

from Day44 import hey
hey()
