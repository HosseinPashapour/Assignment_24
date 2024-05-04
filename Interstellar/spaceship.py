
import arcade
from bullet import Bullet

class Spaceship ( arcade.Sprite ) :

    def __init__ ( self , game ) :
        super().__init__( ":resources:images/space_shooter/playerShip1_orange.png" )
        self.width = 48
        self.height = 48
        self.center_x = game.width // 2
        self.center_y = 40
        self.change_x = 0
        self.change_y = 0
        self.speed = 5
        self.screen_range = game.width
        self.bullet_list = []

    def move ( self ) :
        if self.change_x == 1 :
            if self.center_x < self.screen_range :
                self.center_x += self.speed
        
        elif self.change_x == -1 :
            if self.center_x > 0 :
                self.center_x -= self.speed
    
    def fire ( self ) :
        new_bullet = Bullet ( self )
        self.bullet_list.append ( new_bullet )
