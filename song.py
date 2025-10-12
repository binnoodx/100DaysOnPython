import time


lyrics1 = ["I", "wanna", "be", "your", "setting", "lotion", "(wanna", "be)",]
lyrics2 = ["Hold", "your", "hair", "in", "deep", "devotion", "(How", "deep?)",]
lyrics3 = ["At", "least", "as", "deep", "as", "the", "Pacific", "Ocean",]
lyrics4 = ["Now","I","Wanna","be","yours","❣️"]

class Colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'


time.sleep(0.2)
print(Colors.MAGENTA + "\n\n----- Wanna Be Yours -  Arctic Monkeys -----\n" + Colors.MAGENTA)
time.sleep(0.4)

for word in lyrics1:
    print(Colors.RED + word + Colors.RED, end=" ", flush=True)
    time.sleep(0.4)
print("\n")
for word in lyrics2:
    print(Colors.BLUE + word + Colors.BLUE, end=" ", flush=True)
    time.sleep(0.4)
print("\n")
for word in lyrics3:
    print(Colors.CYAN + word + Colors.CYAN, end=" ", flush=True)
    time.sleep(0.4)
print("\n")
for word in lyrics4:
    print(Colors.GREEN + word + Colors.RED, end=" ", flush=True)
    time.sleep(0.4)
print("\n")