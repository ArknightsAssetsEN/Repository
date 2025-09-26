import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt

class YouTubeMiniPopup(QMainWindow):
    def __init__(self, video_id):
        super().__init__()

        self.setWindowTitle("YouTube Mini Popup")

        self.browser = QWebEngineView(self)
        self.setCentralWidget(self.browser)

        url = f"https://www.youtube.com/embed/{video_id}?autoplay=1&controls=0&modestbranding=1&rel=0"
        self.browser.load(QUrl(url))

        # Cố định kích thước nhỏ
        self.setFixedSize(320, 180)

        # Trạng thái ghim
        self.pinned = False  

        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            # ESC -> tắt app
            self.close()
        elif event.key() == Qt.Key_G:
            # G -> toggle ghim
            self.pinned = not self.pinned
            if self.pinned:
                self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
            else:
                self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
            self.show()  # bắt buộc gọi lại để cập nhật flag

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Nhập video ID
    video_id, ok = QInputDialog.getText(None, "Nhập Video ID", "YouTube Video ID:")
    if ok and video_id.strip():
        popup = YouTubeMiniPopup(video_id.strip())
        popup.show()
        sys.exit(app.exec_())
