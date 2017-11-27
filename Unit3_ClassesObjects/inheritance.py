# Program demonstrating attributes and behaviors of inheritance
# Define Parent class >Note: a Parent object is NOT created directly in
# this program. However, it is inherited and will be created by a Child
# object and a Grandchild object.
class Parent:
    # Class-level variable shared by all objects of the class.
    # Can be accessed using class name (i.e. Parent.parent_value)
    parent_value = 111

    # Constructor of the Parent class
    def __init__(self):
        print("\nIn Parent constructor")

    # Setter (mutator) function
    def set_value(self, attr):
        input("\nIn set_value() in Parent class.")
        input("set_value() is a Setter (mutator) function,")
        input("this means that this will SET/CHANGE a value.")
        input("> def set_value(self, attr):"
              "\n>     Parent.parent_value = attr")
        Parent.parent_value = attr

    # Getter (accessor) function
    def get_value(self):
        input("\nIn get_value() in Parent class.")
        input("get_value() is a Getter (accessor) function,")
        input("this means that this will GET/RETURN a value")
        input("> def get_value(self):"
              "\n>     return Parent.parent_value")
        return Parent.parent_value

# Define Child class and inherit from Parent
class Child(Parent):
    # Class-level variable shared by all members of class.
    child_value = 'abc'

    # Constructor of the Child class
    def __init__(self):
        print("\nIn Child constructor")
        # Call constructor of the Parent class (a.k.a super class)
        super(Child, self).__init__()

    # Setter (mutator function)
    def set_attribute(self, attr):
        input("\nIn set_attribute() in child_object.")
        input("set_attribute() is a Setter (mutator) function,")
        input("this means that this will SET/CHANGE a value.")
        input("> def set_attribute(self, attr):"
              "\n>     Child.child_value = attr")
        Child.child_value = attr

    # Getter (accessor) function
    def get_attribute(self):
        input("\nIn get_attribute() in child_object.")
        input("get_attribute() is a Getter (accessor) function,")
        input("this means that this will GET/RETURN a value")
        input("> def get_attribute(self):"
              "\n>     return Child.child_value")
        return Child.child_value

# Define Grandchild class and inherit from Child (also parent)
class Grandchild(Child):
    # Constructor of the Child class
    def __init__(self):
        print("\nIn Grandchild constructor")
        # Call constructor of the Child class (a.k.a super class)
        super(Grandchild, self).__init__()

    # Setter (mutator function)
    def set_attributes(self, p_attr, c_attr):
        input("\nIn set_attributes() in grandchild_object.")
        input("set_attributes() is a Setter (mutator) function,")
        input("this means that this will SET/CHANGE a value.")
        input("...Setting class-level variables in super classes...")
        input("> def set_attributes(self, p_attr, c_attr):"
              "\n>     Parent.parent_value = p_attr"
              "\n>     Child.child_value = c_attr")
        # Setting class-level variables in super classes
        Parent.parent_value = p_attr
        Child.child_value = c_attr

    # Getter (accessor) function
    def get_attribute(self):
        input("\nIn get_attributes() in grandchild_object.")
        input("get_attributes() is a Getter (accessor) function,")
        input("this means that this will GET/RETURN a value")
        input("> def get_attributes(self):"
              "\n>     return Parent.parent_value, Child.child_value")
        return Parent.parent_value, Child.child_value

# Not done, still on line 68 (where main starts), BE SURE TO FINNISH THIS
# AND PROGRAM 8 FLOWCHART!!!!!
