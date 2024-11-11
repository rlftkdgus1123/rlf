from ursina import * #ursina의 모든 개체
from ursina.prefabs.first_person_controller import FirstPersonController



app=Ursina()

__ = False




T='warp' #warp


tp_pos=[(75,0,10)]
tp_max=1


class Player(FirstPersonController):
    def __init__(self):
        super().__init__( 
            model = 'cube',
            Collider = 'box',
            color = color.green,
            speed = 30,
            scale = 5
        )



class Coin(Entity):
    def __init__(self,x,z):
        super(). __init__(
            coin = Entity(
                model = 'sphere',
                color = color.yellow,
                scale = (6,6,1),
                position = (x * 8,-8,z* 8),
                double_sided = True,
                Collider = 'box'
            )
        )
    
    def update(self):
        self.coin.rotation_y += 1
        if self.coin.intersects(player):
            destroy




#class Warp(Entity):
    #def __init__(self,i,j):
        #super().__init__(
            #warp = Entity(
               #model='cube',
            #color=color.white,  # 흰색으로 설정
            #scale=(8, 80, 8),
            #position=(8 * i, -8, 8 * j),
            #collider='box'
            #)
                
           # )
        #self.color = color.color(1, 1, 1, 0.5)
        #self.a = player

    #def update(self):
            #self.abcd()
            

    #def abcd(self): #플레이어 충돌 감지
        #if self.intersects(self.a):
            #self.a.position = (95, 3 , 90)



class TP(Entity):
    def __init__(self,i,j,tp_pos,tp_max):
        super().__init__(
            model='cube',
            color=color.red,
            position=(i*8,-8,j*8),
            scale=(8,400,8),
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
    def __init__(self, i, j):
        super().__init__(
            model = 'cube',
            scale = (5, 5, 5),
            color = color.black90,
            position = (i*8, -11, j*8),
            collider = 'box'
        )
        self.player = player
        self.text = Text(
            text = 'Escape complete // GG !!',
            scale = 2,
            origin = (0, 0),
            visible = False
        )
    def update(self):
        self.clear()    
    def clear(self):
        dis = (self.player.position - self.position).length()
        print(dis)
        if dis < 3:
            self.player.enabled = False
            self.text.visible = True



def input(key):
    if key == 'escape':
        app.quit()

player = Player()



#EditorCamera()


#zk = Entity(
     #model = 'ee/covered_car_4k.fbx',
     #texture = 'eee/카.jpg',
     #scale = (0.01) ,
     #collider= 'mesh'

#)


ground = Entity(
    model = 'plane',
    #color = color.blue,
    texture = 'grass',
    position = (0,-10,0),
    scale = (2000,1,2000),
    collider= 'mesh', #mash는 물체의 충돌 설정
    #texture = 'painted_brick_diff_4k.jpg'

)





Sky(texture = "sky_sunset")

MAP = [
    [10,'p',10,'t',15,40,30,60,30,20,40,10,49,28,40,58,29,58,18,14,68,63,58,23],
    [10,__,10,10,__,__,__,60,30,20,40,__,__,28,40,58,__,__,__,__,68,__,__,'e'],
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
 

for i in range( len(MAP) ):
    for j in range( len(MAP[i]) ):

            if MAP[i][j]:
                if MAP[i][j]=='p':
                    player.position = (i*5,0,j*5)
                    continue

                if MAP[i][j] == 'e':
                 exitdoor = Exit(i,j)
                 continue

                #if MAP[i][j] == 'w':
                    #warp = Warp(i,j)
                    #continue

                if MAP[i][j]=='t':
                    tp=TP(i,j,tp_pos,tp_max)
                    continue

                #if MAP[i][j]=='z':
                    #zk.position = (i*6,-9,j*5)
                    #continue
                
                #wp = (8*i,-9,8*j)



                wall = Entity(
                    model ='cube',
                    color = color.red,
                    texture = 'brick',
                    scale = (8,80,8),
                    position = (8*i,-8,8*j),
                    collider = 'box',
                    #texture = 'painted_brick_disp_4k.png'
                    )
                
            else:
                coin = Coin(i,j)
            





app.run()