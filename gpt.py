from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
#from ursina.shaders.screenspace_shaders.fxaa import *
import os

os.system('cls')


app=Ursina(
    title='',
    icon='logo.ico',
    borderless=False,
    size=(1000,750)
)

#camera.shader=fxaa_shader

W=True #Wall
__=False #None
P='player' #Player
E='exit' #Exit
T='warp' #warp
H='hhh' #뭘보냐?

tp_pos=[(150,0,5),(75,0,10)]
tp_max=2

class Player(FirstPersonController):
    def __init__(self,i,j):
        super().__init__(
            position=(i*5,5,j*5),
            scale=1,
            collider='box',
            texture='white_cube',
            gravity=1,
            jump_height=0
        )
        
    def input(self, key):
        if held_keys['shift']:
            self.speed=9
        else:
            self.speed=5

class TP(Entity):
    def __init__(self,i,j,tp_pos,tp_max):
        super().__init__(
            model='cube',
            color=color.red,
            position=(i*5,-1,j*5),
            scale=(5,25,5),
            collider='box'
        )
    
        self.player=player
        self.tp_pos=tp_pos

    def warp(self):
        global tp_max
        if self.intersects(self.player):
            tp_max-=1
            self.player.position=self.tp_pos[tp_max]
    
    def update(self):
        self.warp()

class Exit(Entity):
    def __init__(self,i,j):
        super().__init__(
            model='cube',
            color=color.red,
            position=(i*5,-1,j*5),
            scale=(5,25,5),
            collider='box'
        )

        self.player=player
        self.text=Text(
            text='gg lol',
            color=color.green,
            origin=(0,0),
            scale=9,
            visible=False
        )

    def sound(self):
        dis=(self.player.position-self.position).length()
        if tp_max==0:
            a=Audio(
                'kkk',
                volume=256/(dis**2),
                loop=True
            )
    
    def clear(self):
        if self.intersects(self.player):
            self.player.enabled=False
            self.text.visible=True
        
    def update(self):
        self.sound()
        self.clear()

def input(key):
    if key=='escape':
        quit()
    if key=='f11':
        window.fullscreen=not window.fullscreen

EditorCamera()

MAP = [
    [10,P,10,10,15,40,30,60,30,20,40,10,49,28,40,58,29,58,18,14,68,63,58,23],
    [10,T,10,10,__,__,__,60,30,20,40,__,__,28,40,58,__,__,__,__,68,__,__,E],
    [10,__,__,__,__,40,__,__,__,__,__,__,49,28,40,__,__,58,18,__,68,__,58,23],
    [10,__,10,10,__,40,30,60,__,20,40,10,49,__,__,__,29,__,__,__,68,__,__,23],
    [10,__,10,__,__,40,__,__,__,20,40,10,49,__,40,__,29,__,18,14,__,63,__,23],
    [10,__,10,10,__,__,__,60,__,20,40,__,__,__,40,__,__,58,18,__,__,__,__,23],
    [10,__,10,10,__,40,30,__,__,20,40,__,49,28,40,58,__,__,18,__,68,__,58,23],
    [10,__,10,10,__,__,__,__,30,__,__,__,49,__,__,__,29,__,__,__,68,63,58,23],
    [10,__,10,10,15,40,30,60,__,__,40,10,49,__,40,__,29,58,18,__,68,__,__,23],
    [10,__,10,10,15,40,30,60,__,20,40,__,__,__,40,__,__,__,18,__,68,63,__,23],
    [10,__,__,__,__,__,__,__,__,__,__,__,49,28,40,58,29,__,18,__,__,__,__,23],
    [10,11,10,__,15,40,30,60,__,20,40,__,__,28,40,58,29,__,__,14,__,63,58,23],
    [10,11,__,__,15,40,30,__,__,__,40,10,__,28,__,__,__,58,__,14,__,__,__,23],
    [10,11,__,10,15,__,__,60,30,__,40,10,__,__,__,58,__,58,__,14,68,63,__,23],
    [10,11,__,__,__,40,__,60,30,__,__,10,49,28,40,58,__,__,__,14,__,__,__,23],
    [10,11,10,10,__,__,__,60,30,20,__,__,__,__,__,__,__,58,18,__,__,63,58,23],
    [10,11,10,10,15,40,30,60,30,20,40,10,49,28,40,58,29,58,18,14,68,63,58,23]
    
]


for i in range(len(MAP)):
    for j in range(len(MAP[i])):
        if MAP[i][j]:
            if MAP[i][j]=='player':
                player=Player(i,j)
                continue
            if MAP[i][j]=='exit':
                exit=Exit(i,j)
                continue
            if MAP[i][j]=='warp':
                tp=TP(i,j,tp_pos,tp_max)
                continue
            if MAP[i][j]=='hhh':
                hhh=Entity(
                    model='cube',
                    color=color.black90,
                    position=(i*5,-1,j*5),
                    scale=(5,25,5)
                )
                continue
            wall=Entity(
                model='cube',
                color=color.black,
                position=(i*5,-1,j*5),
                scale=(5,25,5),
                collider='box'
            )
            
plane=Entity(
    model='Plane',
    color=color.dark_gray,
    scale=(50000,1,500),
    position=(0,-2,0),
    collider='mesh',
    #texture=''
)

ceiling=Entity(
    model='Plane',
    color=color.black,
    scale=(50000,1,500),
    position=(0,25,0),
    collider='mesh',
    rotation=(0,0,180)
)

pos_print=Text(
    origin=(0,0)
)

def update():
    global ppos
    ppos=[int(oo) for oo in (player.position.x,player.position.y,player.position.z)]
    pos_print.text=ppos

app.run()