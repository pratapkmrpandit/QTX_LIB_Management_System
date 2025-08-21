# class Students:
#     class_id="MCA"   #class attribute
#     def __init__(self,name,age):
#         self.name=name   # instance attribute
#         self.age=age     # instance attribute

# s1=Students("pratap kumar",21)
# s2=Students("priyanshu verma",23)
# print(s1.name + " " + str(s1.age))
# print(s2.name + " " + str(s2.age))


class Animal:
    species="dog"
    def __init__(self,name="",month=0):
        self.name=name
        self.month=month

    def sound(self,voice):
        self.voice=voice

a1=Animal()
a1.name="monty"
a1.month=11
a1.voice="barking"
print(a1.name + " "+ str(a1.month)+" "+ a1.voice + " " + a1.species)