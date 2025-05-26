import pygame

class Player:
    def __init__(self,width,height,x,y,velocity):
        self.img = pygame.image.load('./pixel_art/player/player.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (width, height))
        self.width = width
        self.height = height
        self.img_pos = [x,y]
        self.velocity = velocity
        self.gunshot_sound = pygame.mixer.Sound('./Game/Sounds/Player/silenced-gunshot-81063.mp3')
        self.gunshot_sound.set_volume(0.1)

    def move_to(self,dest_x,dest_y):
        x,y = self.img_pos[0]+self.width/2,self.img_pos[1]+self.height/2
        x_move,y_move = 0,0
        if dest_x - x != 0:
            x_multiplier = (x -dest_x)/((x -dest_x)**2 + (y - dest_y)**2)**(1/2)
            x_move = min(abs(self.velocity * x_multiplier),abs(dest_x-x))
            x_move *= (dest_x - x)/abs(dest_x - x)

        if dest_y - y != 0:
            y_multiplier = (y-dest_y)/((x -dest_x)**2 + (y - dest_y)**2)**(1/2)
            y_move = min(abs(self.velocity * y_multiplier),abs( dest_y - y))
            y_move *= (dest_y - y) / abs(dest_y - y)

        self.img_pos[0] += x_move
        self.img_pos[1] += y_move

        if x_move == 0 and y_move == 0:
            return True
        return False

    def appear_at(self,dest_x,dest_y):
        self.img_pos[0] = dest_x - self.width/2
        self.img_pos[1] = dest_y - self.height/2

    def render(self,surf):
        surf.blit(self.img,self.img_pos)

