class Pet:
    def __init__ (a , has_tail ,legs , name , ears):
        a.has_tail = has_tail
        a.legs = legs 
        self.name = name
        self.ears = ears



    def __str__(self) :
        
     return f" y {self.name} { self.legs} ноги и {'есть хвост  ' if self.has_tail else'хвоста нет'}."\
            f"У него {'есть ушки' if self.ears else 'нет ушек'}"

    def sound(self): 
        pass





class Dog(Pet):
    def __init__ (self ,  legs , name , ears):
       super().__init__(name = name , legs = legs , ears = ears , has_tail= True)




dog = Dog(4 , "Чарли", True)
print(Dog)
