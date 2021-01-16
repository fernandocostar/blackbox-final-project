import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from keras.models import Model
from keras.preprocessing.image import load_img,img_to_array
from keras.applications.imagenet_utils import preprocess_input

class Solver:

    """
    initiates Solver instance receiving the following parameters:
        model: pre-trained model instance used to predict the nearest images
        imgs: array containing the images ids, used to find those in the given path
        path: directory where the image files can be found
    """
    def __init__(self, model, imgs, path):
        self.model = model
        self.imgs = imgs
        self.images_path = path
        self.image_width = 224
        self.image_height = 224
        self.solver = Model(inputs=self.model.input,outputs=self.model.layers[-2].output)
        self.processed_image = self.pre_process()
        self.sim_table = self.get_prediction_matrix(self.processed_image)

    def __process_img__(self, img, path):

        """
        if path == "":
            path = self.images_path
        """
        try :
            return load_img(self.images_path + img + '.png',
                            target_size=(self.image_width, self.image_height))
        except OSError :
            # image unreadable // remove from list
            self.imgs = [x for x in self.imgs if x != img]
            pass

    def pre_process(self):

        dense_mat = None

        try:

            #get image required dimensions from model
            img_width = self.image_width
            img_height = self.image_height

            pictures_array = []
            for file_name in self.imgs:
                try:
                    original = load_img(self.images_path + file_name + '.png', target_size=(224, 224))
                    numpy_image = img_to_array(original)
                    image = np.expand_dims(numpy_image, axis=0)
                    pictures_array.append(image)
                except Exception as err:
                    print(err)
            images = np.vstack(pictures_array)
            dense_mat = preprocess_input(images)
            return dense_mat

        except Exception as err:
            print("deu erroooo: " + str(err))

    def get_prediction_matrix(self, dense_mat):

        solver = self.solver
        imgs_features = solver.predict(dense_mat)
        cos_similarities = cosine_similarity(imgs_features)
        cos_similarities_df = pd.DataFrame(cos_similarities,
                                           columns=self.imgs[:len(self.imgs)],
                                           index=self.imgs[:len(self.imgs)])
        return cos_similarities_df

    def predict(self, given_img, nb_closest_images = 3):
        original = self.__process_img__(given_img, path="")
        plt.imshow(original)
        plt.show()

        print("-----------------------------------------------------------------------")
        print("most similar manga:")

        closest_imgs = self.sim_table[given_img].sort_values(ascending=False)[1:nb_closest_images+1].index
        closest_imgs_scores = self.sim_table[given_img].sort_values(ascending=False)[1:nb_closest_images+1]
        print(len(closest_imgs))
        for i in range(0,len(closest_imgs)):
            original = self.__process_img__(closest_imgs[i])
            print(closest_imgs[i])
            plt.imshow(original)
            plt.show()
            print("similarity score : ",closest_imgs_scores[i])
        print(closest_imgs_scores)
        print(closest_imgs)
