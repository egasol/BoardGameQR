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
        # action = input("Enter") # Temporary for testing
        action = scanner.read_input()

        if action is not None:
            if action != "exit":
                party.action(action)
                map.draw_map()
            else:
                break
        else:
            print("Could not read card...")


if __name__ == "__main__":
    main()
