from World import MapGrid
from ScanQR import Scanner
from Party import Party
from TextToSpeech import TextToSpeech
from Music import MusicPlayer

from enum import Enum, auto
from pathlib import Path
from time import sleep

MUSIC_PATH = Path("Music")
MAP_PATH = Path("SavedMaps/Tutorial")
PLAY_AUDIO = False
DEBUG_MODE = True


class GameStatus(Enum):
    Action = auto()
    Event = auto()


def main():
    party = Party()
    map = MapGrid(MAP_PATH, party)
    scanner = Scanner()
    status = GameStatus.Action
    tts = TextToSpeech()
    music = MusicPlayer(MUSIC_PATH)

    map.draw_map()
    music.play()
    sleep(3)
    tts.generate_audio(map.opening_dialogue, play_audio=PLAY_AUDIO)
    game_ongoing = True

    while (game_ongoing):
        if not DEBUG_MODE:
            action = scanner.read_input()
        else:
            action = input("Enter:")

        if action is not None:
            if action != "exit":
                feedback = party.action(action)

                if feedback is not None:
                    tts.generate_audio(feedback, play_audio=PLAY_AUDIO)
                map.draw_map()
            else:
                game_ongoing = False
        else:
            tts.generate_audio("Unable to read card, try again.")
            print("Could not read card...")


if __name__ == "__main__":
    main()
