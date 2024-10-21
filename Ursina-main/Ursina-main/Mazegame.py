from ursina import * #ursina의 모든 객체(함수, 클래스, 변수 등)를 가져온다.
from ursina.prefabs.first_person_controller import FirstPersonController



__ = False


app = Ursina()

class Player(FirstPersonController):
    def __init__(self):
        super().__init__(
            speed = 10,
            model = 'cube',
            collider = 'mesh',
            scale = 1,
            position = (0,0,0)
        )

class Exit(Entity):
    def __init__(self, i, j):
        super().__init__(
            model = 'cube',
            scale = (5, 5, 5),
            color = color.black90,
            position = (i*5, 0, j*5),
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

duck = Entity(
    model = 'model/duck.fbx',
    texture = 'images/duck.jpg',
    scale = 0.1,
    rotation = (0,90,0),
    collider = 'mesh'
)

MAP = [
    [10,__,'p',10,15,40,30,60,30,20,40,10,49,28,40,58,29,58,18,14,68,63,58,23],
    [10,__,10,10,__,__,__,60,30,20,40,__,__,28,40,58,__,__,__,__,68,__,__,'e'],
    [10,__,__,__,__,40,__,__,__,__,__,__,49,28,40,__,__,58,18,__,68,__,58,23],
    [10,__,10,10,__,40,30,60,__,20,40,10,49,__,__,__,29,__,__,__,68,__,__,23],
    [10,__,10,__,__,40,__,__,__,20,40,10,49,__,40,__,29,__,18,14,__,63,__,23],
    [10,__,10,10,__,__,__,60,__,20,40,__,__,__,40,__,__,58,18,__,__,__,__,23],
    [10,__,10,10,__,40,30,__,__,20,40,__,49,28,40,58,__,__,18,__,68,__,58,23],
    [10,'z',10,10,__,__,__,__,30,__,__,__,49,__,__,__,29,__,__,__,68,63,58,23],
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
    for j in range( len( MAP[i] ) ):
        if MAP[i][j]:
            if MAP[i][j] =='p':
                player.position = (i * 5, 0, j * 5)
                continue

            if MAP[i][j] == 'e':
                exitdoor = Exit(i,j)
                continue

            if MAP[i][j] =='d':
                duck.position = (i * 5, 0, j * 5)
                continue
            wall = Entity(
                model = 'cube',
                #color = color.red,
                scale = (5 ,5 ,5),
                position = (i * 5, 1, j * 5),
                collider = 'box',
                texture = 'images/wall.jpg'
                )



ground = Entity(
    model = 'plane',
    color = color.gray,
    position = (0, 0, 0),
    scale = (2000, 1, 2000), 
    collider = 'mesh'#물체의 충돌판정 형태를 설정합니다. mesh: 그물망형태
)

app.run()
