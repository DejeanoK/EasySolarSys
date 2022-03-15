import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure(figsize=(16,9), dpi = 120)
#name : [radius*2, distance to sun, speed, period in day, color]

CYCLE = 8000
size = 1/300
size4 = 1/100
sizes = 1/2100

planets = {
"mercure" : [4880*size4, 1000, 175936,87.969, "darkgoldenrod"],
"venus" : [12104*size4, 2000, 126062,224.7015, "orange"],
"terre" : [12756*size4,3000, 107243,365.256, "deepskyblue"],
"mars" : [6805*size4, 4000, 87226,686.980, "orangered"],
"jupiter" : [142984*size, 5000, 47196,11.862*365, "moccasin"],
"saturne" : [120536*size, 6000, 34962,29.457*365, "tan"],
"uranus" : [51312*size, 7000, 24459, 84.323*365, "turquoise"],
"nepture" : [49922*size, 8000, 24459, 164.79*365, "royalblue"],
"sun" : [1391900*sizes, 0, 0, 1, "yellow"]
}

ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-7500,7500)
ax.set_ylim(-7500,7500)
ax.set_zlim(-7500,7500)
fig.set_facecolor('black')
ax.set_facecolor('black')
ax.w_xaxis.pane.fill = False
ax.w_yaxis.pane.fill = False
ax.w_zaxis.pane.fill = False
plt.axis('off')

class Planet:
    def __init__(self, position,d, periode, dist, col):
        u = np.linspace(0, 2 * np.pi, 12)
        v = np.linspace(0, np.pi, 12)
        self.px = d * np.outer(np.cos(u), np.sin(v))
        self.py = d * np.outer(np.sin(u), np.sin(v))
        self.x =  self.px +  position[0]
        self.y =  self.py + position[1]
        self.z = d * np.outer(np.ones(np.size(u)), np.cos(v)) + position[2]
        self.dist = dist
        self.vang = (2*np.pi)/periode
        self.col = col

    def plot(self,ax):
        ax.plot_surface(self.x, self.y, self.z, color = self.col)

    def move(self,time):
        self.x =  self.dist * np.cos(self.vang * time) + self.px
        self.y =  self.dist * np.sin(self.vang * time) + self.py

txt_time = ax.text(7500,7500,7500,0,color="r")
plan = []
for p in planets:
    pl = Planet([planets[p][1],0,0],planets[p][0], planets[p][3], planets[p][1], planets[p][4])
    pl.plot(ax)
    plan.append(pl)

def animate(i):
    for artist in plt.gca().lines + plt.gca().collections:
        artist.remove()
    for p in plan:
        p.move(i)
        p.plot(ax)
    txt_time.set_text("Jour : " + str(i) + "\nRévolution terreste : " + str(int(i/365)))

anim = animation.FuncAnimation(fig, animate, repeat = False, interval = 15, frames = CYCLE)

plt.show()