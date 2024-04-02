# Tensorflow에서 모델 불러오기
# pip install tensorflow (가상환경 활성화 시킨 다음 설치할 것)

import tensorflow as tf

def load_model():
    model = tf.keras.applications.MobileNetV2(weights='imagenet')
    print('Success to load model')
    return model

model = load_model()