#MaClasse Mon rectangle

class MyRectangle :
    def __init__(self,X_TopLeft, Y_TopLeft, Height, Width):
        self.X_TopLeft = X_TopLeft
        self.Y_TopLeft = Y_TopLeft
        self.Height = Height
        self.Width = Width
        
    def BottomRight(self) :
        return self.X_TopLeft + self.Width, self.Y_TopLeft + self.Height

    def recWidth(self) :
        return self.Width

    def Aire(self) :
        return self.Width * self.Height                  

Monrectangle = MyRectangle(10,100,4,5)
print(Monrectangle)
print('Les coordonnees du coin en bas à droite sont : ' + str(Monrectangle.BottomRight()))
print('la largeur est : ' + str(Monrectangle.recWidth()))
print('La surface est de : ' + str(Monrectangle.Aire()))
