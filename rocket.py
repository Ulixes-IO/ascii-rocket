import color
import time
import os

# define our clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')    

def launch():
    rocket1()
    time.sleep(.2)
    screen_clear()
    rocket2()
    time.sleep(.2)
    screen_clear()
    rocket3()
    time.sleep(.2)
    screen_clear()
    rocket4()
    time.sleep(.2)
    screen_clear()
    rocket5()
    time.sleep(.1)
    screen_clear()
    rocket6()
    time.sleep(.1)
    screen_clear()
    rocket7()
    time.sleep(.05)
    rocket8()
    time.sleep(.05)
    screen_clear()      


def rocket1():
    print((color.Blue)+"         /\\")
    print("        |==|")
    print("        |  |")
    print("        |  |")
    print("        |  |")
    print("       /____\\")
    print("       |    |")
    print("       |    |")
    print("      /| |  |\\")
    print("     / | |  | \\")
    print("    /__|_|__|__\\")
    print("       /_\/_\\"+(color.Reset))


def rocket2():
    print((color.Blue)+"        |==|")
    print("        |  |")
    print("        |  |")
    print("        |  |")
    print("       /____\\")
    print("       |    |")
    print("       |    |")
    print("      /| |  |\\")
    print("     / | |  | \\")
    print("    /__|_|__|__\\")
    print("       /_\/_\\"+(color.Reset))
    print((color.Red)+"       ######"+(color.Reset))


def rocket3():
    print((color.Blue)+"        |  |")
    print("        |  |")
    print("       /____\\")
    print("       |    |")
    print("       |    |")
    print("      /| |  |\\")
    print("     / | |  | \\")
    print("    /__|_|__|__\\")
    print("       /_\/_\\"+(color.Reset))
    print((color.Red)+"       ######")
    print("      ########")
    print("       ######"+(color.Reset))

def rocket4():
    print((color.Blue)+"        |  |")
    print("       /____\\")
    print("       |    |")
    print("       |    |")
    print("      /| |  |\\")
    print("     / | |  | \\")
    print("    /__|_|__|__\\")
    print("       /_\/_\\"+(color.Reset))
    print((color.Red)+"       ######")
    print("      ########")
    print("       ######")
    print("        ####"+(color.Reset))


def rocket5():
    print((color.Blue)+"       |    |")
    print("       |    |")
    print("      /| |  |\\")
    print("     / | |  | \\")
    print("    /__|_|__|__\\")
    print("       /_\/_\\"+(color.Reset))
    print((color.Red)+"       ######")
    print("      ########")
    print("       ######")
    print("        ####")
    print("        ####"+(color.Reset))


def rocket6():
    print((color.Blue)+"      /| |  |\\")
    print("     / | |  | \\")
    print("    /__|_|__|__\\")
    print("       /_\/_\\"+(color.Reset))
    print((color.Red)+"       ######")
    print("      ########")
    print("       ######")
    print("        ####")
    print("        ####")
    print("         ##")
    print("         ##"+(color.Reset))   



def rocket7():
    print((color.Red)+"       ######")
    print("      ########")
    print("       ######")
    print("        ####")
    print("        ####")
    print("         ##")
    print("         ##")   
    print("         ##")
    print("         ##"+(color.Reset))

def rocket8():
    print((color.Red)+"         ##"+(color.Reset))
