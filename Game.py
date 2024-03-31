from World import MapGrid
from ScanQR import Scanner
from Party import Party
from TextToSpeech import TextToSpeech
from Music import MusicPlayer

from enum import Enum, auto
from pathlib import Path

MUSIC_PATH = Path("Music")


class GameStatus(Enum):
    Action = auto()
    Event = auto()


def main():
    party = Party()
    map = MapGrid((12, 12), party)
    scanner = Scanner()
    status = GameStatus.Action
    tts = TextToSpeech()
    music = MusicPlayer(MUSIC_PATH)

    map.draw_map()
    music.play()

    while (True):
        action = input("Enter:")  # Temporary for testing
        # action = scanner.read_input()

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
