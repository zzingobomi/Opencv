# OpenCV 환경설정
1. conda create -n opencv python=3.7
2. conda activate opencv
3. pip install opencv-contrib-python  (4.5.1.48)
4. pip install numpy==1.19.3
5. pip install matplotlib
6. pip install tensorflow==2.1.0 (CUDA 10.1)

# 딥러닝 환경설정
* https://developer.nvidia.com/rdp/cudnn-archive 에서 자신의 CUDA 버전에 맞는 cuDNN 다운로드
* CUDA가 설치된 폴더에 붙여넣기
* 필요 패키지
    - pip install numpy
    - pip install opencv-contrib-python

    - pip install scipy matplotlib pillow
    - pip install imutils h5py requests progressbar2
    - pip install scikit-learn scikit-image