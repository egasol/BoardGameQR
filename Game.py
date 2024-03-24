from World import MapGrid
from ScanQR import Scanner
from Party import Party

from enum import Enum, auto


class GameStatus(Enum):
	Action = auto()


def main():
	party = Party()
	map = MapGrid((12, 12), party)
	scanner = Scanner()
	
	map.draw_map()

	party.action("north")
	map.draw_map()

	party.action("east")
	map.draw_map()

	party.action("south")
	map.draw_map()

	party.action("west")
	map.draw_map()
	

if __name__ =="__main__":
	main()
