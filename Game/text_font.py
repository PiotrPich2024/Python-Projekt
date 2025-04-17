import pygame
from enum import Enum

class symbols(Enum):
    comma = (44,0)
    period = (46,1)
    slash = (47,13)
    open_bracket = (40,5)
    close_bracket = (41,6)
    percent = (37,3)
    mult = (42,11)
    add = (43,9)
    minus = (45,12)
    exclamation = (33,2)
    question = (63,4)
    equals = (61,10)
    lesser = (60,7)
    greater = (62,8)


class TextFont:
    def __init__(self,width,height,gap_width):
        self.letters_img = pygame.image.load('./Pixel art/Fonts/Letters.png').convert()
        self.numbers_img = pygame.image.load('./Pixel art/Fonts/numbers.png').convert()
        self.symbols_img = pygame.image.load('./Pixel art/Fonts/symbols.png').convert()

        self.characters_width = width #13
        self.characters_height = height #16
        self.gap_width = gap_width#1

    def render_digit(self,n,surf,pos):
        digit_sheet_x_pos = n * (13)
        temp_surf = self.numbers_img.subsurface(digit_sheet_x_pos,0,12,16)
        temp_surf = pygame.transform.scale(temp_surf,(self.characters_width,self.characters_height))
        surf.blit(temp_surf,pos)

    def render_character(self,char,surf,pos):
        c = char.lower()
        charcter_sheet_x_pos = ((ord(c) - 97) * (13))
        temp_surf = self.letters_img.subsurface(charcter_sheet_x_pos,0,12,16)
        temp_surf = pygame.transform.scale(temp_surf, (self.characters_width, self.characters_height))
        surf.blit(temp_surf,pos)

    def render_symbol(self,s,surf,pos):
        ascii_s = ord(s)
        if ascii_s == 32:
            return
        symbol_sheet_x_pos = -1
        for e in symbols:
            if e.value[0] == ascii_s:
                symbol_sheet_x_pos = (e.value[1] * (13))
                break
        if symbol_sheet_x_pos == -1:
            print("there is no symbol found in the sheet\n")
            return
        temp_surf = self.symbols_img.subsurface(symbol_sheet_x_pos,0,12,16)
        temp_surf = pygame.transform.scale(temp_surf, (self.characters_width, self.characters_height))
        surf.blit(temp_surf,pos)


    def render_string(self,s,surf,pos):
        temp_surf = pygame.Surface((self.characters_width * len(s), self.characters_height))
        x_pos = 0
        for word in s:
            ascii_c = ord(word)
            if(97 <= ascii_c <= 122 or 65 <= ascii_c <= 90):
                self.render_character(word,temp_surf,(x_pos,0))
            elif 48 <= ascii_c <= 57:
                self.render_digit(ascii_c-48,temp_surf,(x_pos,0))
            else:
                self.render_symbol(word,temp_surf,(x_pos,0))
            x_pos += self.characters_width

        surf.blit(temp_surf,pos)


