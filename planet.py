import pygame
import math

pygame.init()

width,height=800,800
window=pygame.display.set_mode((width,height))
pygame.display.set_caption("Planet Simulation")

white=(255,255,255)
yellow=(255,255,0)
      
class Planet:
    AU=149.6e6*1000
    G=6.67428e-11
    SCALE=250/AU#1AU=100 px
    TIMESTEP=3600*24#1 DAY

    def __init__(self,x,y,mass,radius,color):
        self.x=x
        self.y=y
        self.mass=mass
        self.radius=radius
        self.color=color

        self.orbit=[]
        self.sun=False
        self.distance_2_sun=0


        self.x_val=0
        self.y_val=0
    
    def draw(self,window):
        x=self.x*self.SCALE+width/2
        y=self.y*self.SCALE+height/2
        pygame.draw.circle(window,self.color,(x,y),self.radius)
        


def main():
    run=True
    clock=pygame.time.Clock()

    sun=Planet(0,0,1.98892e30,30,yellow)
    sun.sun=True

    planets=[sun]

    while(run):
        clock.tick(60)
        window.fill(white)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        
        for planet in planets:
            planet.draw(window)

        pygame.display.update()
    pygame.quit()


main()