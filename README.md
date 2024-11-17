# photo.py
## 사진에 특수 효과 처리하기
사진을 받아 그 사진에 특수 효과를 처리해 저장하는 것을 구현하고자함.

### 주요 기능
- [스크립트가 제공하는 기능 목록]
  - 사진 읽기
  - 엠보싱
  - 카툰
  - 연필 스케치
  - 유화
  - 저장하기(선택하여)
  - 나가기

# videop.py
## 비디오 영상에 특수 효과 처리하기
비디오 영상을 받아 하나의 창으로 원본 영상과 특수 효과를 동시에 보여주는 것을 구현하고자함.
이 저장소는 다양한 비디오 처리 작업을 수행하는 Python 스크립트(`video.py`)를 포함하고 있습니다.
이 스크립트는 OpenCV, MoviePy 등의 라이브러리를 사용하여 비디오 파일을 조작합니다.

### 주요 기능

- [스크립트가 제공하는 기능 목록]
  - 비디오 시작
  - 엠보싱
  - 카툰
  - 연필 스케치
  - 유화
  - 나가기

# 요구 사항

스크립트를 실행하기 전에 다음과 같은 의존성 라이브러리를 설치해야 합니다:

```bash

pip install opencv-python opencv-contrib-python
pip install numpy
pip install PyQt6
pip install pyinstaller
 pyinstaller --onefile --noconsole .py위치
