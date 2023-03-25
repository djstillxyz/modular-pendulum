import Kane_Integrate
import numpy as np

from manim import *
from manim.utils.color import Colors
from configparser import ConfigParser

file = 'config.ini'
config = ConfigParser()
config.read(file)

class Animate(Scene):
    
    def construct(self):

        x = Kane_Integrate.x
        y = Kane_Integrate.y
        n = Kane_Integrate.n
        
        bobs = []
        lines = []
        colors = [RED,BLUE,GREEN,YELLOW,ORANGE]

        #Creates updater object for the Strings
        def getline(Point1,Point2):
            start_point = Point1.get_center()
            end_point = Point2.get_center()
            line = Line(start_point,end_point).set_stroke(width=2) 
            return line

        #Create the ball and line objects
        for i in range(n):
            if i == 0:
                bobs.append(Dot())
            bobs.append(Dot(radius=0.05).move_to((i+1.25)*RIGHT+(i+1.25)*UP).set_color(colors[i]))
            lines.append(Line(bobs[i],bobs[i+1]).set_stroke(width = 2))

        #Calls getline for each String
        for i in range(n):
            lines[i].add_updater(lambda mobject, i=i: mobject.become(getline(bobs[i],bobs[i+1])))
        
        #Animation Loop
        for i in range(len(x)):

            Animations = []
            
            for j in range(len(lines)):
                self.remove(bobs[j+1])
                self.add(bobs[j+1],lines[j])
                Animations.append(bobs[j+1].animate.move_to([x[i][j],y[i][j],0]))

            self.play(*Animations, run_time = 1/Kane_Integrate.fps)
            
