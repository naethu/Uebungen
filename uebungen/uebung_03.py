import math

class Figur:
    def __init__(self):
        self.name = "Figur"

    def umfang(self):
        return 0
    
    def __str__(self):
        return self.name
    
class Point(Figur):
    def __init__(self, x, y):
        super().__init__("Punkt")
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punkt({self.x}, {self.y})"
    
class Dreieck(Figur):
    def __init__(self, p1, p2, p3):
        super().__init__("Dreieck")
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def umfang(self):
        a = math.sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)
        b = math.sqrt((self.p3.x - self.p2.x) ** 2 + (self.p3.y - self.p2.y) ** 2)
        c = math.sqrt((self.p1.x - self.p3.x) ** 2 + (self.p1.y - self.p3.y) ** 2)
        return a + b + c

    def __str__(self):
        return f"Dreieck({self.p1}, {self.p2}, {self.p3})"

class Rechteck(Figur):
    def __init__(self, p1, p2):
        super().__init__("Rechteck")
        self.p1 = p1
        self.p2 = p2

    def umfang(self):
        a = abs(self.p2.x - self.p1.x)
        b = abs(self.p2.y - self.p1.y)
        return 2 * (a + b)
    
    def __str__(self):
        return f"Rechteck ({self.p1.x}, {self.p1.y} - {self.p2.x}, {self.p2.y})"

class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__("Kreis")
        self.mittelpunkt = mittelpunkt
        self.radius = radius

    def __str__(self):
        return f"Kreis M={self.mittelpunkt}, r={self.radius}"

    def flaeche(self):
        return self.radius**2 * math.pi
    
    def umfang(self):
        return 2 * self.radius * math.pi

#ab hier teilweise mit ChatGPT gelöst, da ich alleine nicht weiter kam    
class Polygon(Figur):
    def __init__(self, punkte):
        super().__init__("Polygon")
        self.punkte = punkte

    def umfang(self):
        umfang = 0
        for i in range(len(self.punkte)):
            if i == len(self.punkte) - 1:
                umfang += math.sqrt((self.punkte[i].x - self.punkte[0].x)**2 + (self.punkte[i].y - self.punkte[0].y) ** 2)
            else:
                umfang += math.sqrt((self.punkte[i+1].x - self.punkte[i].x) ** 2 + (self.punkte[i+1].y - self.punkte[i].y) ** 2)
            umfang += a
        return umfang
    
    def __str__(self):
        punkte_str = ", ".join(str(punkt) for punkt in self.punkte)
        return f"Polygon({punkte_str})"