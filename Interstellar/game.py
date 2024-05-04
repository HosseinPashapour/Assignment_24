import threading
import time
import arcade
from spaceship import Spaceship
from bullet import Bullet
from enemy import Enemy
from life import Life


class Game ( arcade.Window ) :

    def __init__ ( self ) :
        super().__init__ ( title = "INTERSTELLAR GAME 2024" )
        self.game_background = arcade.load_texture ( ":resources:images/backgrounds/stars.png" )
        self.gameover_background = arcade.load_texture ( "game over.png" )
        self.mode = None
        self.score = 0
        self.me = Spaceship ( self )
        self.enemy_list = []
        self.enemy_speed = 3
        self.timer = time.time ()
        self.life_list = []
        self.life_x = 15
        self.life_number = 3
        self.my_thread=threading.Thread(target=self.creat_enemy)
        for i in range ( self.life_number ) :
            new_life = Life ( self.life_x )
            self.life_list.append ( new_life )
            self.life_x += 25
        self.fire_voice = arcade.load_sound ( ":resources:sounds/laser4.wav" )
        self.explode = arcade.load_sound ( ":resources:sounds/gameover3.wav" )


    def on_draw ( self ) :
        arcade.start_render ()

        if self.mode == "Game_over" :
            arcade.set_background_color ( arcade.color.BLACK )
            arcade.draw_lrwh_rectangle_textured ( 0 , 0 , self.width , self.height , self.gameover_background )
            score_text = f" Final Score : { self.score }"
            arcade.draw_text ( score_text , ( self.width // 2 ) - 90 , 35 , arcade.color.PINK_PEARL , 25)
        
        else :
            arcade.set_background_color ( arcade.color.DARK_BLUE)
            arcade.draw_lrwh_rectangle_textured ( 0 , 0 , self.width , self.height , self.game_background )
        
            self.me.draw ()
        
            for bullet in self.me.bullet_list :
                bullet.draw ()
        
            for enemy in self.enemy_list :
                enemy.draw ()
        
            for life in self.life_list :
                life.draw ()

            score_text = f" Score : { self.score }" 
            arcade.draw_text ( score_text , self.width - 130 , 12 , arcade.color.WHITE , 16 )
        
        arcade.finish_render ()


    def on_key_press ( self , symbol , modifiers ) :
        if symbol == arcade.key.LEFT or symbol == arcade.key.A :
            self.me.change_x = -1
        
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D :
            self.me.change_x = 1
        
        elif symbol == arcade.key.SPACE :
            self.me.fire ()
            arcade.play_sound ( self.fire_voice )


    def on_key_release ( self , symbol , modifiers ) :
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT :
            self.me.change_x = 0


    def creat_enemy(self):
        while True:
            self.enemy_list.append(Enemy(self))
            time.sleep(3)


    def on_update ( self , delta_time ) :

        self.me.move ()

        for bullet in self.me.bullet_list :
            bullet.move ()
        
        for enemy in self.enemy_list :
            enemy.move ()

        for enemy in self.enemy_list :
            if enemy.center_y <= 0 and len ( self.life_list ) > 0 :
                self.enemy_list.remove ( enemy )
                self.life_list.pop ( self.life_number - 1 )
                self.life_number -= 1
        
        for bullet in self.me.bullet_list :
            if bullet.center_y >= self.height :
                self.me.bullet_list.remove ( bullet )

        if time.time () >= self.timer + 3 :
            new_enemy = Enemy ( self , self.enemy_speed )
            self.enemy_list.append ( new_enemy )
            self.enemy_speed += 0.1
            self.timer = time.time ()

        if self.life_number == 0 :
            self.mode = "Game_over"

        for enemy in self.enemy_list :
            if arcade.check_for_collision ( self.me , enemy ) :
                self.mode = "Game_over"

        for enemy in self.enemy_list :
            for bullet in self.me.bullet_list :
                if arcade.check_for_collision ( enemy , bullet ) :
                    self.enemy_list.remove ( enemy )
                    self.me.bullet_list.remove ( bullet )
                    arcade.play_sound ( self.explode )
                    self.score += 1
        

window = Game ()
arcade.run ()