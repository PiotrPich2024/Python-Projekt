import pygame
from enum import Enum

#informacje o pixel arcie
class fontData:
    width = 12
    height = 16
    gap_width = 1

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

        self.characters_width = width #12
        self.characters_height = height #16
        self.gap_width = gap_width#1

    def render_digit(self,n,surf,pos):
        digit_sheet_x_pos = n * (fontData.width + fontData.gap_width)
        temp_surf = self.numbers_img.subsurface(digit_sheet_x_pos,0,fontData.width,fontData.height)
        temp_surf = pygame.transform.scale(temp_surf,(self.characters_width,self.characters_height))
        surf.blit(temp_surf,pos)

    def render_character(self,char,surf,pos):
        c = char.lower()
        charcter_sheet_x_pos = ((ord(c) - 97) * (fontData.width + fontData.gap_width))
        temp_surf = self.letters_img.subsurface(charcter_sheet_x_pos,0,fontData.width,fontData.height)
        temp_surf = pygame.transform.scale(temp_surf, (self.characters_width, self.characters_height))
        surf.blit(temp_surf,pos)

    def render_symbol(self,s,surf,pos):
        ascii_s = ord(s)
        if ascii_s == 32:
            return
        symbol_sheet_x_pos = -1
        for e in symbols:
            if e.value[0] == ascii_s:
                symbol_sheet_x_pos = (e.value[1] * (fontData.width + fontData.gap_width))
                break
        if symbol_sheet_x_pos == -1:
            print("there is no symbol found in the sheet\n")
            return
        temp_surf = self.symbols_img.subsurface(symbol_sheet_x_pos,0,fontData.width,fontData.height)
        temp_surf = pygame.transform.scale(temp_surf, (self.characters_width, self.characters_height))
        surf.blit(temp_surf,pos)

    def big_brain_moment(self, surf_w,surf_h,s):
        words = s.split()
        max_chars_in_line = surf_w // self.characters_width
        max_lines = surf_h // (self.characters_height + self.gap_width)

        lines = []
        current_line = []

        current_len = 0
        for word in words:
            word_len = len(word)
            if word_len > max_chars_in_line:
                print("za długie słowo!")
                return []
            if current_len + word_len + len(current_line) > max_chars_in_line:
                lines.append(current_line)
                current_line = []
                current_len = 0
            current_line.append(word)
            current_len += word_len + 1

        if current_line:
            lines.append(current_line)

        if len(lines) > max_lines:
            print("zmniejsz czcionkę, słowa się nie mieszczą!")
            return []

        return lines

    def render_string(self,s,surf,pos):
        surf_w, surf_h = surf.get_width(),surf.get_height()
        words_arr = self.big_brain_moment(surf_w,surf_h,s)
        string_height = len(words_arr) * (self.characters_height + self.gap_width)
        temp_surf = pygame.Surface((surf_w, string_height))
        x_pos = 0
        y_pos = 0
        for words in words_arr:
            x_pos = 0
            for word in words:
                for c in word:
                    ascii_c = ord(c)
                    if (97 <= ascii_c <= 122 or 65 <= ascii_c <= 90):
                        self.render_character(c, temp_surf, (x_pos, y_pos))
                    elif 48 <= ascii_c <= 57:
                        self.render_digit(ascii_c - 48, temp_surf, (x_pos, y_pos))
                    else:
                        self.render_symbol(c, temp_surf, (x_pos, y_pos))
                    x_pos += self.characters_width
                x_pos += self.characters_width
            y_pos += self.characters_height + self.gap_width

        surf.blit(temp_surf,pos)




