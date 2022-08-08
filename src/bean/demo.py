class demo:
    # __name = 'unknown'
    # __age = 0
    # def __init__(self,name,age):
    #     self.__name = name
    #     self.__age = age
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age
    @name.setter
    def name(self,name):
        self.__name = name
    @age.setter
    def age(self,age):
        self.__age = age
        
        
demo_a = demo()
demo_a.name = 'zhangsan'
demo_a.age = 15
demo_b = demo()
print(demo_a.__dict__)
print(demo_a.name)
print(demo_a.age)
print(demo_b.__dict__)