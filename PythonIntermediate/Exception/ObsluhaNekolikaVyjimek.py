try:
    from math import pes
except ImportError:
    print("Podařil se mi ImportError!")

try:
    #assert 1 == 2
    f = open("text_file.txt")
except AssertionError:
    print("Podařil se mi AssertionError!")
except AttributeError:
    print("Podařil se mi AttributeError!")
except IndexError:
    print("Podařil se mi IndexError!")
except FileNotFoundError:
    print("Podařil se mi FileNotFoundError!")
except ModuleNotFoundError:
    print("Podařil se mi ModuleNotFoundError!")
except ImportError:
    print("Podařil se mi ImportError!")
except KeyError:
    print("Podařil se mi KeyError!")
except NameError:
    print("Podařil se mi NameError!")
except ValueError:
    print("Podařil se mi ValueError!")
except ZeroDivisionError:
    print("Podařil se mi ZeroDivisionError!")
except TypeError:
    print("Podařil se mi TypeError!")
except IndentationError:
    print("Podařil se mi IndentationError!")
