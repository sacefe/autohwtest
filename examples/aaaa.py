# module.py
#
#
# # class inside the module
# class MyClass:
#     def myclass(str):
#         print(f"Hello How are you {str} ?")


# Dynamic.py


class Dyclass:
    def __init__(self, module_name, class_name):
        module = __import__(module_name)  # __import__ method used to getmodule
        self.my_class = getattr(module, class_name)  # getting attribute by getattr()
        self.self = self



obj = Dyclass("halcon_pcb_tp001", "ScopeDS1000sGetResource")
obj.my_class.execute(obj.self, True)