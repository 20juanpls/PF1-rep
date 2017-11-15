# global variables (a.k.a. module-level variables)
globe_1 = 111
globe_2 = 222
globe_3 = 333


def main():
    print("_______________________ functions_0.py _______________________")
    # calling print_string function
    input("In this module, we will observe the behavior of functions"
          "\nand the extend of what they can and can't manipulate")
    input("\nWe will also observe how global variables behave in functions"
          "\nwhen accessed or changed, and what happens if you create a local"
          "\nvariable with the same name as a global in a function.")

    input("\nCalling print_string function")
    input("> print_string(<some string>)")
    print_string("\nThis is the First string passed to print_string().")
    print_string("This is the SECOND string passed to print_string().\n")

    # Calling print_string() function form within a for loop
    # notice the value of 'i' in the output
    input("Calling print_string() function form within a for loop"
          "\nnotice the value of 'i' in the output.")
    input(">  for i in range (2, 11, 2):"
          "\n>      print_string('Calling print_string() and i = {}'.format(i))\n")
    for i in range(2, 11, 2):
        print_string('  Calling print_string() and i = {}'.format(i))

    # Variables a-e are used in the call to test_scope_0() below
    a = 'a_here'
    b = [1, 2]
    c = [3, 4]
    d = [5, 6]
    e = 33

    input('\nIn main, before call to test_scope_0:')
    print('> a = {}'.format(a))
    print('> b = {}'.format(b))
    print('> c = {}'.format(c))
    print('> d = {}'.format(d))
    print('> e = {}'.format(e))

    input("\nVariables a - e are used in the call to test_scope_0()"
          "\n|!| - Note that a 'copy' of d is passed")
    input("\n> test_scope_0(a, b, c, d[:], e)")
    input("\n> def test_scope_0(w,x,y,z,zl):"
          "\n>     w = 99"
          "\n>     x[0] = 'changed!'"
          "\n>     y = y[:]"
          "\n>     y[0] = 'changed!'"
          "\n>     z[0] = 'changed!'"
          "\n>     zl = 44")
    input("'a' is a string which is IMMUTABLE")
    input("'b' is a MUTABLE list and is changed")
    input("'c' is a MUTABLE list but a COPY is created in the"
          "\ntest_scope_0() function so changes does NOT persist")
    input("'d' is a MUTABLE list but a COPY is also created.")
    input("'e' is a numeric literal which is immutable")

    test_scope_0(a, b, c, d[:], e)

    input("\nIn main, after call to test_scope_0:")
    input("> a = {}".format(a)+" ; Not changed since 'a' is immutable.")
    input("b[0] was changed by test_scope_0. A list is mutable")
    input("> b = {}".format(b))
    input("> c = {}".format(c)+" ; Not changed since a copy used in the FUNCTION")
    input("> d = {}".format(d)+" ; Not changed since a copy used as an ARGUMENT")
    input("> e = {}".format(e)+" ; Not changed since 'e' is immutable.")

    test_scope_1()

    input("\ntest_scope_2() Accesses global variables for REASSIGNMENT, therefore"
          "\nit MUST use the 'global' keyword!")

    input("\nIn main() BEFORE test_scope_2():")
    input("> globe_1 = {}".format(globe_1))
    input("> globe_2 = {}".format(globe_2))
    input("> globe_3 = {}".format(globe_3))

    test_scope_2()

    input("\nIn main() AFTER test_scope_2() which CHANGES the globals:")
    input("> globe_1 = {}".format(globe_1))
    input("> globe_2 = {}".format(globe_2))
    input("> globe_3 = {}".format(globe_3))

    test_scope_3()
    input("\nIn main() AFTER test_scope_3():")
    input("Changes applied by the test_scope_3 are ONLY applied in"
          "\ntest_scope_3()")
    input("> globe_1 = {}".format(globe_1))
    input("> globe_2 = {}".format(globe_2))
    input("> globe_3 = {}".format(globe_3))


def print_string(string_to_print):
    print(string_to_print)


# w - immutable object w change not reflected in caller
# x - mutable object x was changed and change was reflected in caller
# y - mutable object y was changed and change was NOT reflected in caller
# z - mutable object z was changed and change was NOT reflected in caller
# zl - immutable object zl change not reflected in caller
def test_scope_0(w,x,y,z,zl):
    # Change variables that were passed as arguments
    # 99 is immutable and therefore caller does NOT see change
    w = 99
    # The 'zeroth' element of the list is changed
    # The caller WILL see the change not passed as a copy
    x[0] = 'changed!'
    # Copy of y is created so caller does NOT see changes
    # made by test_scope_0()
    y = y[:]
    y[0] = 'changed!'
    # Passed as copy 'd[:]' so caller does NOT see changes
    z[0] = 'changed!'
    # 44 is immutable and therefore caller does NOT see change
    z1 = 44


def test_scope_1():
    # Show the global variables
    input("\n  test_scope_1() ACCESSES the variables but ONLY for DISPLAY,"
          "\n  NOT for REASSIGNMENT!")
    # Access the globals but ONLY  for display, NOT for reassignment!
    input("\n  In test_scope_1():")
    input("  > globe_1 = {}".format(globe_1))
    input("  > globe_2 = {}".format(globe_2))
    input("  > globe_3 = {}".format(globe_3))


def test_scope_2():
    input("\n  In test_scope_2():")
    input("\n  > global globe_1, globe_2, globe_3"
          "\n  > globe_1, globe_2, globe_3 = 777, 888, 999")
    # Access global variables for reassignment
    # MUST use the 'global' keyword to access the globals for reassignment
    global globe_1, globe_2, globe_3

    # Change the global variables
    globe_1, globe_2, globe_3 = 777, 888, 999

    # Show that the globals were changed
    input("\n  After global statement:")
    input("  Changes applied by test_scope_2 are applied globally since"
          "\n  the global keyword was used!")
    input("  > globe_1 = {}".format(globe_1))
    input("  > globe_2 = {}".format(globe_2))
    input("  > globe_3 = {}".format(globe_3))


def test_scope_3():
    input("\n  Local variables 'shadow' or 'replace' global variables")
    input("  The variables are NOT the same as the global variables that were previously defined")

    globe_1 = 'abc'
    globe_2 = 'abc'
    globe_3 = 'abc'

    input("\n  In test_scope_3():")
    input("  Since the global keyword was NOT used, new local variables"
          "\n  are created with the SAME NAMES as the global variables.")
    input("  > globe_1 = {}".format(globe_1))
    input("  > globe_2 = {}".format(globe_2))
    input("  > globe_3 = {}".format(globe_3))

    input("\n  Call the built-in function 'locals()' to show the variables"
          "\n  that are LOCAL to the test_scope_3 function")
    input("  locals: "+ str(locals()))


if __name__ == '__main__':
    main()

else:
    pass
