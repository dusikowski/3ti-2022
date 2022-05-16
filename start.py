import pygame
import pygame_menu
import lekcja1
def zmianaRozdielczosci(nazwaPola,atrybut):
    lekcja1.zmianaRozdielczosci=atrybut
def zmienKolorWaz1(Value):
    lekcja1.zmienaKolorWaz1(Value)
def zmienKolorWaz2(Value):
    lekcja1.zmienaKolorWaz2(Value)
def main():
    pygame.init()
    OknoMenu=pygame.display.set_mode((800,800))
    pygame.display.set_caption("Menu Snake")
    menu = pygame_menu.Menu('Snake 3TI',800,800,theme=pygame_menu.themes.THEME_DARK)
    menu.add.button("start gry",lekcja1.main,background_color=(0,0,0))
    menu.add.selector("rozmiar ekranu",[('400x400',400),('600x600',600),('800x800',800)],onchange=zmianaRozdielczosci)
    menu.add.color_input("kolor wąż 1",'rgb',default=(25,25,100),onreturn=zmienKolorWaz1)
    menu.add.color_input("kolor wąż 2",'rgb',default=(25,25,100),onreturn=zmienKolorWaz2)

    menu.mainloop(OknoMenu)

main()
