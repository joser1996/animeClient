import curses

def draw_main(stdscr):
	key = 0
	cursor_x = 0
	cursor_y = 0
	curses.curs_set(0)
	stdscr.clear()
	stdscr.refresh()

	options = ["Anime...", "Genre..."]
	currentOption = 0
	curses.start_color()
	curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
	curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_MAGENTA)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

	while key != ord('q'):
		stdscr.clear()
		height, width = stdscr.getmaxyx()
		
		if key == curses.KEY_DOWN:
			currentOption = currentOption + 1
			currentOption = min(currentOption, len(options) - 1)
		elif key == curses.KEY_UP:
			currentOption = currentOption - 1
			currentOption = max(0, currentOption)
		
		title = "Menu"[:width - 1]
		subtitle = "Search by ..."
		statusbarstr = "Press 'q' to exit | Status Bar | Option: {}".format(currentOption)

		startX_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
		startx_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
		start_y = int((height // 2) - 2)

		stdscr.attron(curses.color_pair(3))
		stdscr.addstr(height - 1, 0, statusbarstr)
		stdscr.addstr(height - 1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
		stdscr.attroff(curses.color_pair(3))

		# Turn on att for title
		stdscr.attron(curses.color_pair(2))
		stdscr.attron(curses.A_BOLD)
		stdscr.addstr(start_y, startX_title, title)
		stdscr.attroff(curses.color_pair(2))
		stdscr.attroff(curses.A_BOLD)
		
		stdscr.addstr(start_y + 1, startx_subtitle, subtitle)

		offset = 2
		
		for i in range(len(options)):
			if currentOption == i:
				stdscr.attron(curses.color_pair(4))
			else:
				stdscr.attron(curses.color_pair(1))

			menuStr = "({})\t {}".format(i, options[i])
			stdscr.addstr(start_y + offset, startx_subtitle, menuStr)
			offset += 2
			
			if currentOption == i - 1:
				stdscr.attroff(curses.color_pair(4))
			else:
				stdscr.attroff(curses.color_pair(1))

		stdscr.refresh()

		key = stdscr.getch()

