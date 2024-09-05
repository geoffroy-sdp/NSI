class Rectangle:
    def __init__(self, A, B, couleur):
        self.width = A
        self.length = B
        self.color = couleur
        
    def air(self):
        air = self.width * self.length
        return air
    

rect1 = Rectangle(5, 6, 'green')
rect1.couleur = 'blue'
print(rect1.couleur)

rect2 = Rectangle(1234567, 23456789, 'cyan')
rect3 = Rectangle(98765, 765, 'black')

print("\n", rect1.air(), "\n", rect2.air(), "\n", rect3.air(), '\n')