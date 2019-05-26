from utils import *


class Classifier:

    def __init__(self, path, scale=1.1, min_size=None, max_size=None, min_neighbors=1):

        self.cascade_classifier = cv2.CascadeClassifier(path)

        self.scale = scale

        self.min_size = min_size

        self.max_size = max_size

        self.min_neighbors = min_neighbors

    def classify(self, image):

        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        return list(map(Rectangle.from_iterable,
                        self.cascade_classifier.detectMultiScale(image,
                                                                 scaleFactor=self.scale, minSize=self.min_size,
                                                                 maxSize=self.max_size,
                                                                 minNeighbors=self.min_neighbors)))


class Classifiers:

    def __init__(self):

        self.classifiers = {}

    def add(self, name, classifier):

        if isinstance(classifier, str):

            classifier = Classifier(classifier)

        self.classifiers[name] = classifier

    def remove(self, name):

        return self.classifiers.pop(name)

    def get(self, name):

        return self.classifiers[name]

    def get_names(self):

        return self.classifiers.keys()

    def get_classifiers(self):

        return self.classifiers.items()

    def get_all(self):

        return self.classifiers

    def classify(self, name, image):

        return self.classifiers[name].classify(image)
