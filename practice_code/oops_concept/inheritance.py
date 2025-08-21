class dog :
    def __init__(self,name): 
        self.name=name
    
    def display_name(self):
        print("the name of dog is : " + self.name)

class voice(dog):  #single inheritance also example of hierarchical inheritance with combination 
    def speak(self):
        print("bark")


class bread(voice):      # multiplelevel inheritance
    def display_bread(self):
        print("the bread of dog is Rottweiler")

# mutiple inheritance
class color:      
    def display_color(self):
        print("the color of dog is white")

class combination(color,dog):  # multiple inheritance
    def display_com(self):
        print("the combination to check the multiple inheritance")

d1=voice("monty")
d1.display_name()
d1.speak()
d2=bread("sheru")
d2.display_bread()
d2.display_name()
d3=combination("big bull")
d3.display_color()
d3.display_name()