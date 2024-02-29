# 3.
# The Liskov Substitution Principle states that subclasses should be substitutable for their base classes.

# This means that, given that class B is a subclass of class A, we should be able to pass an object of
# class B to any method that expects an object of class A and the method should not give any weird output in that case.

# This is the expected behavior, because when we use inheritance we assume that the child class inherits everything
# that the superclass has. The child class extends the behavior but never narrows it down.

#incorrect
class KitchenApp:
    def on(self):
        pass

    def off(self):
        pass

    def set_temperature(self, value):
        pass


class Toster(KitchenApp):
    def on(self):
        print("Toster is on")

    def off(self):
        print("Toster is off")

    def set_temperature(self, value):
        print(f"Temperature is set to {value} degrees...")


class Juicer(KitchenApp):
    def on(self):
        print("Toster is on")

    def off(self):
        print("Toster is off")


#correct
class KitchenApp:
    def on(self):
        pass

    def off(self):
        pass

class KitchenAppWithTemp(KitchenApp):

    def set_temperature(self, value):
        pass


class Toster(KitchenAppWithTemp):
    def on(self):
        print("Toster is on")

    def off(self):
        print("Toster is off")

    def set_temperature(self, value):
        print(f"Temperature is set to {value} degrees...")


class Juicer(KitchenApp):
    def on(self):
        print("Toster is on")

    def off(self):
        print("Toster is off")
