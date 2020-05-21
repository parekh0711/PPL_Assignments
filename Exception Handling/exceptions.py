#This code is to demonstrate how to handle various exceptions in python
try:
    # print(1/0)
    #
    # import blahblahblah
    #
    # file_object = open("doesnotexist.txt", "r")
    #
    #
    # keyboard_interrupt=input()
    #
    # dict={}
    # print(dict['error'])
    #
    # print(a)
    #
    # sys.exit(0)
except KeyError:
    print("Sorry, That dictionary does not have this key.")
except ZeroDivisionError:
    print("Let us stay in the domain of Real Numbers")
except ImportError:
    print("Please install before importing")
except IndentationError:
    print("Have a look at your indentation again")
except SystemExit:
    print("Your sys.exit() is working perfectly")
except OSError:
    print("Could not open/read file")
except EOFError:
    print("You have reached EOF but still tried reading")
except KeyboardInterrupt:
    print("It's rude to interrupt people like that")
except AttributeError:
    print("You passed the wrong attribute")
# except:
    # print("You did something wrong which even I didn't expect")
finally:
    print("I am executed no matter what")
