#Stage 0: Import dataset and upload some images

from tensorflow.keras.datasets import fashion_mnist
from imageio import imwrite

(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

for i in range(20, 25):
    imwrite(uri="uploads/{}.png".format(i), im=X_test[i])
