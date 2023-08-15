
import os
import ctypes

import cv2
from keras.optimizer_v2.gradient_descent import SGD
from numpy import save, load
from keras.optimizers import gradient_descent_v2
sgd: SGD = gradient_descent_v2.SGD(...)
from matplotlib import pyplot
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten
from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

##---------------------------------------------------------------------------------------------------------------------------------------------
# Dosya bilgileri
##---------------------------------------------------------------------------------------------------------------------------------------------
dataSetFolder = "C:/Users/fatih/Downloads/untitled/dataset/"
dataSetTrain = dataSetFolder + "train/"
dataSetTest = dataSetFolder + "test/"
dataSetTestRatio = 0.25
print(os.listdir(dataSetFolder))
imageHeight = 224
imageWidth = 224
Categories = ["Hatalı","Hata Yok"]
Epochs = 1
#tensorflow CNN model
model = Sequential()


def showImages(image_folder, img_width=None, img_height=None):
    i = 0
    pyplot.figure(image_folder)
    for image_full_name in os.listdir(image_folder):
        filename = image_folder + image_full_name
        image_data = cv2.imread(filename)
        if img_width != None and img_height != None:
            image_data = cv2.resize(image_data,(img_width, img_height))
        pyplot.subplot(330 + 1 + i)
        pyplot.title(image_full_name)
        pyplot.imshow(image_data,)
        i += 1
        if(i == 9):break
    # show the figure
    pyplot.show()


"""
loadDatasetWithdata function load dataset from data
"""
def loadDatasetWithdata():
    photos = load(dataSetFolder + "data_photos.npy")
    labels = load(dataSetFolder + "data_labels.npy")
    print(photos.shape,labels.shape)
    return photos,labels
##---------------------------------------------------------------------------------------------------------------------------------------------
#  DEFINE MODEL AND START TRAIN THE MODEL
##---------------------------------------------------------------------------------------------------------------------------------------------

def defineModel():
    ## Feature Learning
    #1.  blok
    model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', input_shape=(imageHeight, imageWidth, 3)))
    model.add(MaxPooling2D((2, 2)))
    #2.  blok
    model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
    model.add(MaxPooling2D((2, 2)))
    #3.  blok
    model.add(Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
    model.add(MaxPooling2D((2, 2)))
    #4.  blok
    model.add(Conv2D(256, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
    model.add(MaxPooling2D((2, 2)))
    #5.  blok
    model.add(Conv2D(512, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
    model.add(MaxPooling2D((2, 2)))
    #6.  blok
    model.add(Conv2D(1024, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
    model.add(MaxPooling2D((2, 2)))


    model.add(Flatten())
    model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
    model.add(Dense(64, activation='relu', kernel_initializer='he_uniform'))
    model.add(Dense(32, activation='relu', kernel_initializer='he_uniform'))

    model.add(Dense(1, activation='sigmoid'))
    opt = SGD(lr=0.0001, momentum=0.99)
    model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
    model.summary()
    return model


def summarizeDiagnostics(info):
    # plot loss
    pyplot.subplot(211)
    pyplot.title('Cross Entropy Loss')
    pyplot.plot(info.history['loss'], color='blue', label='train')
    pyplot.plot(info.history['val_loss'], color='orange', label='test')
    # plot accuracy
    pyplot.subplot(212)
    pyplot.title('Classification Accuracy')
    pyplot.plot(info.history['accuracy'], color='blue', label='train')
    pyplot.plot(info.history['val_accuracy'], color='orange', label='test')
    # save plot to file
    pyplot.savefig('train_info_plot.png')
    pyplot.close()


def runTrainTest(dataSetTrain,dataSetTest):
    # model
    model = defineModel()
    # data generator
    train_datagen = ImageDataGenerator(rescale=1.0 / 255.0, width_shift_range=0.1, height_shift_range=0.1, horizontal_flip=True)
    test_datagen = ImageDataGenerator(rescale=1.0 / 255.0)
    # iteratörler
    train_it = train_datagen.flow_from_directory(dataSetTrain, class_mode='binary', batch_size=64, target_size=(imageHeight, imageWidth))
    test_it = test_datagen.flow_from_directory(dataSetTest, class_mode='binary', batch_size=64, target_size=(imageHeight, imageWidth))
    # fit model
    print("Eğitim Başlıyor")
    history = model.fit(train_it, steps_per_epoch=len(train_it), validation_data=test_it, validation_steps=len(test_it), epochs=Epochs, verbose=1)
    # evaluate model
    _, acc = model.evaluate_generator(test_it, steps=len(test_it), verbose=0)
    print('Sonuç>> %.3f' % (acc * 100.0))
    # serialize weights to HDF5
    model_json = model.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)
    model.save("model.h5")
    model.save_weights("model_weights.h5")
    print("Model Diske Kaydedildi")
    summarizeDiagnostics(history)


##---------------------------------------------------------------------------------------------------------------------------------------------
# LOAD MODEL AND TEST DATASET IMAGES
##---------------------------------------------------------------------------------------------------------------------------------------------
def load_image(img_path, show=False):
    img = image.load_img(img_path, target_size=(imageHeight, imageWidth, 3))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)                                                                                                                                                                                                        # channels)
    img_tensor /= 255.
    return img_tensor


def test_et(img_path):
    model = load_model("model.h5")
    defect_count = 0
    nodefect_count = 0
    i = 0
    j = 0
    onlyfiles = next(os.walk(img_path))[2] #dir is your directory path as string
    imglist = [[[0 for k in range(1)] for j in range(3)] for i in range(len(onlyfiles))]
    for image_full_name in os.listdir(img_path):
        filename = img_path + image_full_name
        new_image = load_image(filename)
        pred = model.predict(new_image)

        if pred > 0.965:
            nodefect_count += 1
            pred_int = 1
        else:
            defect_count += 1
            pred_int = 0
            print(pred)
        result = Categories[pred_int]
        imglist[i][j] = image_full_name
        imglist[i][j+1] = float(pred)
        imglist[i][j+2] = result
        i += 1
        print("Defect: " + str(defect_count))
        print("NoDefect: " + str(nodefect_count))
        print(image_full_name, pred, pred_int, result)

    return imglist

##runTrainTest(dataSetTrain, dataSetTest)


