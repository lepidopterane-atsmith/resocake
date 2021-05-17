# Lepidopterane
# Resocake Generator (based on Cheescake)
# Interactive doodler. Click to make art

'''
Directions: Click the big art window when the small window is green to make art!
'''
from graphics import *
from random import randint

def main():

    # First I'll initialize a black window:
    win = GraphWin("Click on the screen while the small window is green", 1000,700)
    win.setBackground("black")

    # Indicator window initialization
    indicator = GraphWin("green = ready, red = drawing", 50,50)
    indicator.setBackground("green")

    # Setup initial ghost lines
    left = Line(Point(10,10), Point(10,690))
    right = Line(Point(990,10), Point(990,690))

    lines =[left,right] # this array is really important

    for x in range(50):
        p = win.getMouse() # click
        indicator.setBackground("red") # drawing time!
        
        # Gets the midpoint of each line drawn before the click, and
        # draws a line from each midpoint to the click.
        num = len(lines)
        for i in range(num):
            q = lines[i].getCenter()
            newline = Line(p,q)
            doodle(newline,randcolor(),win)
            lines.append(newline)
        indicator.setBackground("green")
                    
def randcolor():
    r = randint(3,5)

    reso_wires = ["#ff8000","#0080ff", "#80ff00", "#804000","#004080", "#408000"]
    
    color = reso_wires[r]
    return color

def doodle(x,color,win):
    '''
    This is your one-stop drawing function. It colors the line, sends it to the
    window, and it even supports line declaration as the first parameter.  
    '''

    x.setOutline(color)
    x.setWidth(5)
    x.draw(win)

    nodepoints = [x.getP1(), x.getP2()]
    rc = Image(nodepoints[0],"new_clock.png")
    rc.draw(win)

    rd = Image(nodepoints[1],"new_clock.png")
    rd.draw(win)

main()
