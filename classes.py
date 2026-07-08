# print("Hello")
class mathmetical_options:
    def __init__(self, name):
        self.name=name
        print(f'Welcome {name}')
    def sum(self,a,b):
        return a+b

maths=mathmetical_options("Shah Zaib")
sum_num=maths.sum(11,19)
concatenate_name=maths.sum("Shah ", "Zaib")
print(f"Sum of two numbers: {sum_num}")
print(f"Concatenate wo strings: {concatenate_name}")

