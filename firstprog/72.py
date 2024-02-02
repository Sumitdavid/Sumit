class Parent:
    def Parent(self):
        print("This is Parent method")

class Child(Parent):
    def Parent(self):
        print("Sagar")
        super().Parent()
    def Child(self):
        print("This is Child method")
        super().Parent()

Child_obj=Child()
Child_obj.Child()
Child_obj.Parent()