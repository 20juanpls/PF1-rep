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
        input("\n In Parent constructor")
        input(" No object is being created here...")
        input(" This only indicates that the child and grandchild objects will inherit"
              "\n the functions of this Class Parent.")

    # Setter (mutator) function
    def set_value(self, attr):
        input("\n In set_value() in Parent class.")
        input(" set_value() is a Setter (mutator) function,")
        input(" this means that this will SET/CHANGE a value.")
        input(" > def set_value(self, attr):"
              "\n >     Parent.parent_value = attr")
        Parent.parent_value = attr

    # Getter (accessor) function
    def get_value(self):
        input("\n In get_value() in Parent class.")
        input(" get_value() is a Getter (accessor) function,")
        input(" this means that this will GET/RETURN a value")
        input(" > def get_value(self):"
              "\n >     return Parent.parent_value")
        return Parent.parent_value


# Define Child class and inherit from Parent
class Child(Parent):
    # Class-level variable shared by all members of class.
    child_value = 'abc'

    # Constructor of the Child class
    def __init__(self):
        input("\n In Child constructor")
        input(" Calling constructor of the Parent Class (a.k.a super class)")
        input(" > super(Child, self).__init__()")
        super(Child, self).__init__()

    # Setter (mutator function)
    def set_attribute(self, attr):
        input("\n In set_attribute() in child_object.")
        input(" set_attribute() is a Setter (mutator) function,")
        input(" this means that this will SET/CHANGE a value.")
        input(" > def set_attribute(self, attr):"
              "\n >     Child.child_value = attr")
        Child.child_value = attr

    # Getter (accessor) function
    def get_attribute(self):
        input("\n In get_attribute() in child_object.")
        input(" get_attribute() is a Getter (accessor) function,")
        input(" this means that this will GET/RETURN a value")
        input(" > def get_attribute(self):"
              "\n >     return Child.child_value")
        return Child.child_value


# Define Grandchild class and inherit from Child (also parent)
class Grandchild(Child):
    # Constructor of the Child class
    def __init__(self):
        input("\n In Grandchild constructor")
        input(" Calling constructor of the Child Class (a.k.a super class)")
        input(" In which its constructor will Call the constructor of the Parent Class")
        input(" > super(Grandchild, self).__init__()")
        super(Grandchild, self).__init__()

    # Setter (mutator function)
    def set_attributes(self, p_attr, c_attr):
        input("\n In set_attributes() in grandchild_object.")
        input(" set_attributes() is a Setter (mutator) function,")
        input(" this means that this will SET/CHANGE a value.")
        input(" ...Setting class-level variables in super classes...")
        input(" > def set_attributes(self, p_attr, c_attr):"
              "\n >     Parent.parent_value = p_attr"
              "\n >     Child.child_value = c_attr")
        # Setting class-level variables in super classes
        Parent.parent_value = p_attr
        Child.child_value = c_attr

    # Getter (accessor) function
    def get_attribute(self):
        input("\n In get_attributes() in grandchild_object.")
        input(" get_attributes() is a Getter (accessor) function,")
        input(" this means that this will GET/RETURN a value")
        input(" > def get_attributes(self):"
              "\n >     return Parent.parent_value, Child.child_value")
        return Parent.parent_value, Child.child_value


# main() function
def main():
    input("\n################ child_object ################")
    input("\nIn main(), instantiating child_object...")
    input("> child_object = Child()")
    child_object = Child()

    input("\nIn main(), calling GETTER in Parent class from child_object")
    input("NOTE: the getter method is INHERITED from the Parent Class")
    input("> child_object.get_value()")
    child_object.get_value()

    input("\nIn main(), calling GETTER in child_object")
    input("> child_object.get_attribute()")
    child_object.get_attribute()

    input("\nIn main(), calling SETTER in child_object")
    input("> child_object.set_attribute(222)")
    child_object.set_attribute(222)

    input("\nIn main(); calling GETTER in child_object")
    input("> child_object.get_attribute()")
    child_object.get_attribute()

    input("\n################ grandchild_object ################")
    input("\nIn main(), INSTANTIATING grandchild_object...")
    input("NOTE: pay attention to the ORDER of CONSTRUCTORS called")
    grandchild_object = Grandchild()

    input("\nIn main(), printing grandchild_object.parent_value")
    input("NOTE: Accessing a data member INHERITED from the Parent Class")
    input("> print(grandchild_object.parent_value)")
    input(grandchild_object.parent_value)

    input("\nIn main(), calling SETTER in grandchild_object")
    input("> grandchild_object.set_attributes('I\'m the Parent value.',"
          "\n                                   'I\'m the Child value')")
    grandchild_object.set_attributes('I\'m the Parent value.',
                                     'I\'m the Child value')
    input("\nIn main(), calling GETTER in grandchild_object")
    input("Values returned from get_attributes() are assigned to temp1 & temp2")
    input("Calling grandchild_object.get_attributes().")
    input("> temp1, temp2 = grandchild_object.get_attribute()")
    temp1, temp2 = grandchild_object.get_attribute()
    input("These are the values returned from get_attributes():")
    input("temp1 = "+temp1+", temp2 = "+temp2)

    input("\nIn main(), Printing child_object.parent_value")
    input("NOTE: Accessing a data member INHERITED from the Parent Class")
    input("> print(child_object.parent_value)")
    input(child_object.parent_value)


if __name__ == '__main__':
    main()

else:
    pass
