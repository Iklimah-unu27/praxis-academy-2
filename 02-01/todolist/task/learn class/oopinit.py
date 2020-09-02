class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()
# The previous 2 lines can also be written as
# Person('Swaroop').say_hi()

# disini menggunakan metode_init
#Metode __init__ dijalankan segera setelah sebuah objek kelas dibuat (yaitu dibuat).
# Metode ini berguna untuk melakukan inisialisasi apa pun (yaitu meneruskan nilai awal ke objek Anda) yang ingin Anda lakukan dengan objek Anda. 
# Perhatikan garis bawah ganda di awal dan di akhir nama.