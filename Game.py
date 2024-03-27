from World import MapGrid
from ScanQR import Scanner
from Party import Party

from enum import Enum, auto


class GameStatus(Enum):
	Action = auto()
	Event = auto()


def main():
	party = Party()
	map = MapGrid((12, 12), party)
	scanner = Scanner()
	status = GameStatus.Action

	map.draw_map()

	while (True):
		action = input() # Temporary for testing
		# scanner.read_input()

		if action != "exit":
			party.action(action)
			map.draw_map()
		else:
			break


if __name__ =="__main__":
	main()
