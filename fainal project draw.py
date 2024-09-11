import turtle as t 
class ColorfulShape: 
    def __init__(self, sides, length, color=None):
        self.sides = sides
        self.length = length
        self.color = color
    
    def run(self):
        sides = int(input())
        length = int(input())
        color = input()
        360/length

 
    def draw(self):
         for i in range(length):
             t.color(color)
             t.begin_fill()
             
             t.fd(sides)
             t.rt(length)

             t.end_fill()
    
a = ColorfulShape()
a.run()
a.draw()
