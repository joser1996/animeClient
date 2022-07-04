from locale import currency
import os, sys
import curses
import mainMenu

def main():
    # curses.wrapper(draw_menus)
	curses.wrapper(mainMenu.draw_main)


if __name__ == "__main__":
    main()
