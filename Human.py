from tkinter import Tk, Canvas, ARC, SE, W
 
class Human():
 
    def __init__(self, canvas, name, x, y, gender):
        self.canvas = canvas
        self.__name = name
        self.x = x
        self.y = y
        self.gender = gender
        
        
    def display(self):
        self.__drawHead()
        self.__drawBody()
        self.__drawLeggs()
        self.__drawHands()
        self.__drawEye1()
        self.__drawEye2()
        self.__drawSmile()
        self.__drawName()
        self.__drawPupil1()
        self.__drawPupil2()
        if self.gender == "Мужчина":
            self.__drawMan()
        elif self.gender == "Женщина":
            self.__drawWoman()
        
    def __drawHead(self):
        self.canvas.create_oval(self.x+20, self.y-180, self.x+80, self.y-120, width = 2, fill = "beige")
        
    def __drawBody(self):
        self.canvas.create_line(self.x+50, self.y-120, self.x+50, self.y-50, width = 2)
        
    def __drawLeggs(self):
        self.canvas.create_line(self.x, self.y, self.x+50, self.y-50, self.x+100, self.y, width = 2)
    
    def __drawHands(self):
        self.canvas.create_line(self.x+10, self.y-70, self.x+50, self.y-110, self.x+90, self.y-70, width = 2)

    def __drawEye1(self):
        self.canvas.create_oval(self.x+35, self.y-165, self.x+45, self.y-155, width = 2, fill = "white")
    
    def __drawEye2(self):
        self.canvas.create_oval(self.x+55, self.y-165, self.x+65, self.y-155, width = 2, fill = "white")
        
    def __drawSmile(self):
        self.canvas.create_arc(self.x+40, self.y-150, self.x+60, self.y-135, width = 2, start = 0, extent =-180, fill = "red")
        
    def __drawName(self):
        self.canvas.create_text(self.x+20, self.y-200, text = self.__name, font = "Arial, 16", anchor = W, fill = "black")
     
    def __drawPupil1(self):
        self.canvas.create_oval(self.x+38, self.y-162, self.x+42, self.y-158, width = 2, fill = "blue")
        
    def __drawPupil2(self):
        self.canvas.create_oval(self.x+58, self.y-162, self.x+62, self.y-158, width = 2, fill = "blue")
        
    def __drawMan(self):
        self.canvas.create_line(self.x+35, self.y-185, self.x+35, self.y-175, width = 2)
        self.canvas.create_line(self.x+50, self.y-190, self.x+50, self.y-180, width = 2)
        self.canvas.create_line(self.x+65, self.y-185, self.x+65, self.y-175, width = 2)
        
    def __drawWoman(self):
        self.canvas.create_line(self.x+35, self.y-175, self.x+10, self.y-160, width = 2)
        self.canvas.create_line(self.x+65, self.y-175, self.x+90, self.y-160, width = 2)
