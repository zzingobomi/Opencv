# OpenCV 환경설정
1. conda create -n opencv python=3.7
2. conda activate opencv
3. pip install opencv-contrib-python  (4.5.1.48)
4. pip install numpy==1.19.3
5. pip install matplotlib
6. pip install tensorflow==2.2.0 (CUDA 10.1)
7. pip install cudnn==7.6.4

# 딥러닝 환경설정
* 공식 지원문서에서는 2.3.0 도 CUDA 10.1 을 지원한다고 하나 실제로 해본결과 2.2.0 은 GPU를 찾는데 2.3.0 은 GPU 를 못찾는다.
* 2.3.0 에서 CUDA 10.2 를 찾는지는 한번 테스트 해봐야 할듯
* https://developer.nvidia.com/rdp/cudnn-archive 에서 자신의 CUDA 버전에 맞는 cuDNN 다운로드 (현재 7.6.4)
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
* fit_generator 사용시 2.1.0 에서는 'error finalizing GeneratorDataset iterator' 발생
  conda install -c conda-forge hdf5=1.10.5
* os.environ["CUDA_VISIBLE_DEVICES"] = "0"