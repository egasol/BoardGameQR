from World import MapGrid
from ScanQR import Scanner
from Party import Party
from TextToSpeech import TextToSpeech

from enum import Enum, auto


class GameStatus(Enum):
    Action = auto()
    Event = auto()


def main():
    party = Party()
    map = MapGrid((12, 12), party)
    scanner = Scanner()
    status = GameStatus.Action
    tts = TextToSpeech()

    map.draw_map()

    while (True):
        # action = input("Enter") # Temporary for testing
        action = scanner.read_input()

        if action is not None:
            if action != "exit":
                feedback = party.action(action)

                if feedback is not None:
                    tts.generate_audio(feedback)
                map.draw_map()
            else:
                break
        else:
            tts.generate_audio("Unable to read card, try again.")
            print("Could not read card...")


if __name__ == "__main__":
    main()
