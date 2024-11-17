import cv2 as cv
import numpy as np
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import Qt
import sys

class VideoSpecialEffect(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('비디오 특수 효과')
        self.setGeometry(200, 200, 800, 600)
        
        # 레이아웃 설정
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        
        control_layout = QHBoxLayout()
        videoButton = QPushButton('비디오 시작', self)
        self.pickCombo = QComboBox(self)
        self.pickCombo.addItems(['엠보싱', '카툰', '연필 스케치(명암)', '연필 스케치(컬러)', '유화'])
        quitButton = QPushButton('나가기', self)

        control_layout.addWidget(videoButton)
        control_layout.addWidget(self.pickCombo)
        control_layout.addWidget(quitButton)

        self.original_label = QLabel(self)
        self.effect_label = QLabel(self)
        
        image_layout = QHBoxLayout()
        image_layout.addWidget(self.original_label)
        image_layout.addWidget(self.effect_label)

        self.layout.addLayout(control_layout)
        self.layout.addLayout(image_layout)

        videoButton.clicked.connect(self.videoSpecialEffectFunction)
        quitButton.clicked.connect(self.quitFunction)

    def videoSpecialEffectFunction(self):
            self.cap = cv.VideoCapture(0, cv.CAP_DSHOW)
            if not self.cap.isOpened(): sys.exit('카메라 연결 실패')

            while True:
                ret, frame = self.cap.read()
                if not ret: break

                pick_effect = self.pickCombo.currentIndex()
                if pick_effect == 0:
                    femboss = np.array([[-1.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
                    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                    gray16 = np.int16(gray)
                    special_img = np.uint8(np.clip(cv.filter2D(gray16, -1, femboss) + 128, 0, 255))
                elif pick_effect == 1:
                    special_img = cv.stylization(frame, sigma_s=60, sigma_r=0.45)
                elif pick_effect == 2:
                    special_img, _ = cv.pencilSketch(frame, sigma_s=60, sigma_r=0.07, shade_factor=0.02)
                elif pick_effect == 3:
                    _, special_img = cv.pencilSketch(frame, sigma_s=60, sigma_r=0.07, shade_factor=0.02)
                elif pick_effect == 4:
                    special_img = cv.xphoto.oilPainting(frame, 10, 1, cv.COLOR_BGR2Lab)

                original_qimg = self.convert_cv_qt(frame)
                effect_qimg = self.convert_cv_qt(special_img)

                self.original_label.setPixmap(QPixmap.fromImage(original_qimg))
                self.effect_label.setPixmap(QPixmap.fromImage(effect_qimg))

                #cv.imshow('Special effect', special_img)
                cv.waitKey(1)

    def convert_cv_qt(self, cv_img):
        rgb_image = cv.cvtColor(cv_img, cv.COLOR_BGR2RGB) 
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        return convert_to_Qt_format.scaled(320, 240, Qt.AspectRatioMode.KeepAspectRatio)

    def quitFunction(self):
            self.cap.release()
            cv.destroyAllWindows()
            self.close()
        
app = QApplication(sys.argv)
win = VideoSpecialEffect()
win.show()
app.exec()