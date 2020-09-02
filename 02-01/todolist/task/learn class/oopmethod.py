class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()

####contoh ####
#property
class Kendaraan : #kendaraan  punya apa saja
roda = 0
kecepatan = 0
cc = 0

#method
def nyala(self): #kendaraan bisa apa ?
    pass

def maju(self) :
    pass

def mundur(self) :
    pass

k1 = Kendaraan():
k1.roda = 3
print(k1.roda)


# The previous 2 lines can also be written as
# Person().say_hi()
#Di sini kita melihat diri beraksi. Perhatikan bahwa metode say_hi tidak mengambil parameter tetapi masih memiliki self dalam definisi fungsinya
