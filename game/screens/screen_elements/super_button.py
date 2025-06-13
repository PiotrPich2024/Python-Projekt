from Game.screens.screen_elements.button_class import Button

class SuperButton(Button):
    def __init__(self,button_surf,button_hover_surf,button_click_surf,pos):
        super().__init__(button_surf,pos)
        self.button_hover_surf = button_hover_surf
        self.button_click_surf = button_click_surf
        self.default_surf = button_surf
        self.current_surf = self.default_surf


        self.clicked = False


    def update(self, mouse_pos, mouse_pressed):
        if not self.clicked and self.is_clicked(mouse_pos):
            # pygame.mouse.get_pressed() zwraca krotke booleanow (x,y,z)
            # gdzie x to lewy przycisk myszy, y to suwak
            # z to prawy
            if mouse_pressed[0]:
                self.clicked = True
                self.current_surf = self.button_click_surf
            else:
                self.current_surf = self.button_hover_surf
        elif self.clicked and self.is_clicked(mouse_pos):
            if not mouse_pressed[0]:
                self.current_surf = self.default_surf
                self.clicked = False
                return True
        else:
            self.current_surf = self.default_surf
            self.clicked = False

        return False

    def render(self, surf):
        surf.blit(self.current_surf, self.pos)


