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

	while (True):
		action = input()

		if action != "exit":
			party.action(action)
			map.draw_map()
		else:
			break


if __name__ =="__main__":
	main()
