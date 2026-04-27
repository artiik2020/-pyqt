import sys
from PyQt6 import QtCore, QtMultimedia, uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class PianoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("plotter.ui", self)

        self.player = QtMultimedia.QMediaPlayer()
        self.audio_output = QtMultimedia.QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.audio_output.setVolume(50)

        self.btn1.clicked.connect(lambda: self.play_note(1))
        self.btn2.clicked.connect(lambda: self.play_note(2))
        self.btn3.clicked.connect(lambda: self.play_note(3))
        self.btn4.clicked.connect(lambda: self.play_note(4))
        self.btn5.clicked.connect(lambda: self.play_note(5))
        self.btn6.clicked.connect(lambda: self.play_note(6))
        self.btn7.clicked.connect(lambda: self.play_note(7))

    def play_note(self, num):
        self.player.stop()
        self.player.setSource(QtCore.QUrl.fromLocalFile(f"misuc/{num}.mp3"))
        self.player.play()

    def keyPressEvent(self, event):
        key = event.text().lower()
        mapping = {
            'z': 1, 'x': 2, 'c': 3, 'v': 4,
            'b': 5, 'n': 6, 'm': 7
        }
        if key in mapping:
            self.play_note(mapping[key])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PianoWindow()
    window.show()
    sys.exit(app.exec())
