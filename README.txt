# OpenCV 환경설정
1. conda create -n opencv python=3.7
2. conda activate opencv
3. pip install opencv-contrib-python  (4.5.1.48)
4. pip install numpy==1.19.3
5. pip install matplotlib
6. pip install tensorflow==2.1.0 (CUDA 10.1)

# 딥러닝 환경설정
* https://developer.nvidia.com/rdp/cudnn-archive 에서 자신의 CUDA 버전에 맞는 cuDNN 다운로드
    - 현재 tensorflow 2.X 기준으로 CUDA 10.1 까지만 공식지원
* CUDA가 설치된 폴더에 붙여넣기
* Pycharm 사용시 tensorflow.keras intelisense 가 안된다면 Community 2020.3 버전을 사용 (Community 버전 기준)
* 필요 패키지
    - pip install numpy
    - pip install opencv-contrib-python

    - pip install scipy matplotlib pillow
    - pip install imutils h5py requests progressbar2
    - pip install scikit-learn scikit-image

    - pip install graphviz
    - pip install pydot

# 유용한 팁
* Ctrl + Shift + N (파일찾기)
* Back, Forward 단축키 정리 (https://cupjoo.tistory.com/94)
