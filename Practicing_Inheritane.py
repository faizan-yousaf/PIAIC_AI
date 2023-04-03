class Parent():

    def __init__(self): #constructor
        self.Id = None  
        self.Name = None
        self.FatherName = None
        self.Email = Name + "@company.com"

    def speak(self, Language= "urdu"):  #method
        return f"{Name} is speaking {Language} language! "
    
    def eat(self, food):    #method
        return f"{Name} is eating {food}."



class Child(Parent):     #inherted from parent class
    pass

    # p1 = Parent() 
    # p1.Id = 1
    # p1.Name = "Muhammad Faizan"
    # p1.FatherName = "Muhammad Yousaf"

    
    print(p1.Id)
    print(p1.Name)
    print(p1.FatherName)
    print(p1.eat("pizza and Burger"))

    c1.Id = 2
    c1 = Child(Parent)
    c1.Name = "Hamza"
    c1.FatherName = "Faizan"
    c1.Email = Name 
    
    c1.eat("Burger")

    