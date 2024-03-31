import vlc
from pathlib import Path


class MusicPlayer:
    def __init__(self, music_path):
        self.music_paths = self.get_music(music_path)

        self.player = vlc.Instance('--loop')

        self.playlist = self.player.media_list_new()
        for music in self.music_paths:
            self.playlist.add_media(self.player.media_new(music))

        self.playlist_player = self.player.media_list_player_new()
        self.playlist_player.set_playback_mode(vlc.PlaybackMode.loop)
        self.playlist_player.set_media_list(self.playlist)

    def get_music(self, music_path):
        music_paths = list(music_path.glob("*.mp3"))

        return music_paths

    def play(self):
        self.playlist_player.play()


if __name__ == "__main__":
    music_player = MusicPlayer(Path("Music"))
    input("Press enter key to exit...")
