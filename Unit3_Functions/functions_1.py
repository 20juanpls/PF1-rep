# global variables (a.k.a. module-level variables)
i = 11
j = 22
k = 33

print("_______________________ functions_1.py _______________________")
input("In this module, we'll take a look at how variables & their id's "
      "\nbehave in different situations with functions.")

input("\nThe following print statements (including this one) will display"
      "\nvariables and addresses at any module level.(so they are NOT in main())")
input("> i = {}".format(i))
input("> j = {}".format(j))
input("> k = {}".format(k))
input("> id(i) = {}".format(id(i)))
input("> id(j) = {}".format(id(j)))
input("> id(k) = {}".format(id(k)))


# main() function
def main():
    input("\nIn main():")
    input("\nCalling f1() which will display globals")
    f1()
    input("\nCalling f2() which will CHANGE globals")
    f2()

    input("\nIn main(), globals have been CHANGED")
    input("> i = {}".format(i))
    input("> j = {}".format(j))
    input("> k = {}".format(k))
    input("> id(i) = {}".format(id(i)))
    input("> id(j) = {}".format(id(j)))
    input("> id(k) = {}".format(id(k)))

    input("\nInitializing local variables in main()")
    input("> a, b, c, d = 12, ***Can't change string!***, 14, list(range(1, 5))")
    a, b, c, d = 12, "***Can't change string!***", 14, list(range(1, 5))
    input("\nIn main() locals before passing to f3():")
    input("> a = {}".format(a))
    input("> b = {}".format(b))
    input("> c = {}".format(c))
    input("> d = {}".format(d))
    input("> id(a) = {}".format(id(a)))
    input("> id(b) = {}".format(id(b)))
    input("> id(c) = {}".format(id(c)))
    input("> id(d) = {}".format(id(d)))

    input("\nCalling f3() where variables will be changed within f3(), However...")
    input("ONLY changes to mutable objects will be reflected back in the caller(main()).")
    input("This will return values from f3() to a1, b1, c1, and c1")
    input("> a1, b1, c1, d1 = f3(a, b, c, d)")
    a1, b1, c1, d1 = f3(a, b, c, d)
    input("\nIn main(), immutable locals are UNCHANGED after being passed to f3().")
    input("However, mutable locals CHANGED after passed to f3().")
    input("Note that all addresses REMAIN UNCHANGED")
    input("> a = {}".format(a)+" <- no change, ints are immutable")
    input("> b = {}".format(b)+" <- no change, strings are immutable")
    input("> c = {}".format(c)+" <- no change, ints are immutable")
    input("> d = {}".format(d)+" <- this one changed tho")
    input("> id(a) = {}".format(id(a)))
    input("> id(b) = {}".format(id(b)))
    input("> id(c) = {}".format(id(c)))
    input("> id(d) = {}".format(id(d)))

    input("\nIn main(), returned values from f3():")
    input("> a1 = {}".format(a1))
    input("> b1 = {}".format(b1))
    input("> c1 = {}".format(c1))
    input("> d1 = {}".format(d1))
    input("> id(a1) = {}".format(id(a1)))
    input("> id(b1) = {}".format(id(b1)))
    input("> id(c1) = {}".format(id(c1)))
    input("> id(d1) = {}".format(id(d1)))

    input("\nFunction f4() is used to demonstrate KEYWORD ARGUMENTS.")
    input("If the caller NAMES the argument the SAME AS THE PARAMETERS, the arguments"
          "\nCAN be positioned in ANY ORDER")
    input("\nIn main, calling f4():")
    input("Keyword arguments are in argument list 'out of order'.")
    input("> f4(keyword3=3, keyword2=2, keyword1=1)")
    f4(keyword3=3, keyword2=2, keyword1=1)


def f1():
    input("\n  In f1(), globals:")
    input("  [f1()]> i = {}".format(i))
    input("  [f1()]> j = {}".format(j))
    input("  [f1()]> k = {}".format(k))
    input("  [f1()]> id(i) = {}".format(id(i)))
    input("  [f1()]> id(j) = {}".format(id(j)))
    input("  [f1()]> id(k) = {}".format(id(k)))


def f2():
    input("\n  In f2():")
    input("  Using 'global' keyword to access variables for REASSIGNMENT")
    input("  [f2()]> global i, j, k")
    global i, j, k
    input("  Now changing global variables")
    input("  [f2()]> i, j , k = 44, 55, 66")
    i, j, k = 44, 55, 66

    input("\n  Global variables now changed!:")
    input("\n  In f2(), globals:")
    input("  [f2()]> i = {}".format(i))
    input("  [f2()]> j = {}".format(j))
    input("  [f2()]> k = {}".format(k))
    input("  [f2()]> id(i) = {}".format(id(i)))
    input("  [f2()]> id(j) = {}".format(id(j)))
    input("  [f2()]> id(k) = {}".format(id(k)))


def f3(a, b, c, d):
    input("\n  In f3() before changes")
    input("  Addresses are the same as those in main():")
    input("  [f3()]> a = {}".format(a))
    input("  [f3()]> b = {}".format(b))
    input("  [f3()]> c = {}".format(c))
    input("  [f3()]> d = {}".format(d))
    input("  [f3()]> id(a) = {}".format(id(a)))
    input("  [f3()]> id(b) = {}".format(id(b)))
    input("  [f3()]> id(c) = {}".format(id(c)))
    input("  [f3()]> id(d) = {}".format(id(d)))

    input("\n  Now changing local variables in f3()")
    input("  [f3()]> a, b, c, d[0] = 'aaa', 'bbb', 'ccc', 'changed'")
    a, b, c, d[0] = 'aaa', 'bbb', 'ccc', 'changed'
    input("  Addresses for immutables have changed since NEW objects"
          "\n  for immutables are CREATED in f(3).")
    input("  Addresses for mutables remains the same since the SAME"
          "\n  object is being accessed (and changed).")
    input("  [f3()]> a = {}".format(a))
    input("  [f3()]> b = {}".format(b))
    input("  [f3()]> c = {}".format(c))
    input("  [f3()]> d = {}".format(d))
    input("  [f3()]> id(a) = {}".format(id(a)))
    input("  [f3()]> id(b) = {}".format(id(b)))
    input("  [f3()]> id(c) = {}".format(id(c)))
    input("  [f3()]> id(d) = {}".format(id(d)))

    input("\n  Returning variables changed locally to the caller")
    input("[f3()]> return a, b, c, d")
    return a, b, c, d


def f4(keyword1, keyword2, keyword3):
    input("\n  In f4() showing keyword argument values:")
    input("  [f4()]>keyword1 = {}".format(keyword1))
    input("  [f4()]>keyword2 = {}".format(keyword2))
    input("  [f4()]>keyword3 = {}".format(keyword3))


if __name__ == '__main__':
    main()

else:
    pass
