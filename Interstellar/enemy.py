
import random
import arcade

class Enemy ( arcade.Sprite ):
    
    def __init__ ( self , game , speed ) :
        super().__init__( ":resources:images/space_shooter/playerShip1_blue.png" )
        self.width = 48
        self.height = 48
        self.angle = 180
        self.center_x = random.randint ( 0 , game.width )
        self.center_y = game.height
        self.change_x = 0
        self.change_y = -1
        self.speed = speed

    def move ( self ) :
        self.center_y -= self.speed