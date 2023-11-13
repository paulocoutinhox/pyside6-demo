import sys
from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QWidget,
    QVBoxLayout,
    QFileDialog,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Player")
        self.showMaximized()

        self.videoWidget = QVideoWidget()

        self.mediaPlayer = QMediaPlayer()
        self.mediaPlayer.setVideoOutput(self.videoWidget)

        # Botão para tocar/pausar
        playButton = QPushButton("Play/Pause")
        playButton.clicked.connect(self.play_video)

        # Botão para abrir arquivo de vídeo
        openButton = QPushButton("Open Video")
        openButton.clicked.connect(self.open_file)

        layout = QVBoxLayout()
        layout.addWidget(self.videoWidget)
        layout.addWidget(playButton)
        layout.addWidget(openButton)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def play_video(self):
        if self.mediaPlayer.playbackState() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def open_file(self):
        # Abre um QFileDialog para escolher o vídeo
        filePath, _ = QFileDialog.getOpenFileName(
            self, "Open Video", "", "Video Files (*.mp4 *.avi *.mkv)"
        )
        if filePath:
            self.mediaPlayer.setSource(QUrl.fromLocalFile(filePath))
            self.mediaPlayer.play()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
