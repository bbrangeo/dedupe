# An implementation of Logistic Regression algorithm in python.
# The class use sparse representation of features.
# Author: Xiance Si (sixiance<at>gmail.com)

import math
import numpy

class LogisticRegression:
    # Initialize member variables. We have two member variables
    # 1) weight: a dict obejct storing the weight of all features.
    # 2) bias: a float value of the bias value.
    def __init__(self):
        self.rate = 0.01
        self.weight = {}
        self.bias = 0
        self.alpha = 0.001
        return
    # data is a list of [label, feature]. label is an integer,
    # 1 for positive instance, 0 for negative instance. feature is
    # a dict object, the key is feature name, the value is feature
    # weight.
    #
    # n is the number of training iterations.
    #
    # We use online update formula to train the model.
    def train(self, data, n):
        data = self.convert_to_numpy(data)
        num_features = len(data[0][1][1])
        self.weight = numpy.zeros(num_features)
        self.feature_names = data[0][1][0]

        old_update = 0
        for i in range(n):
            max_update = 0
            for [label, (_, feature)] in data:
                #print feature
                predicted = self.classify(feature)
                rate_n = self.rate - (self.rate * i)/float(n)

                update = (label - predicted) * feature - (self.alpha * self.weight)
                self.weight += rate_n * update

                # for f,v in feature.iteritems():
                #     if f not in self.weight:
                #         self.weight[f] = 0
                #     update = (label - predicted) * v - (self.alpha * self.weight[f])
                #     self.weight[f] += rate_n * update
                #     if abs(update * self.rate) > max_update :
                #         max_update = abs(update * rate_n)
                bias_update = (label - predicted) 
                self.bias += rate_n * bias_update
            #print 'iteration', i, 'done. Max update:', max_update
        return
    # feature is a dict object, the key is feature name, the value
    # is feature weight. Return value is the probability of being
    # a positive instance.
    def classify(self, feature):
        logit = self.bias

        logit += numpy.dot(self.weight, feature)
        # for f,v in feature.iteritems():
        #     coef = 0
        #     if f in self.weight:
        #         coef = self.weight[f]
        #     logit += coef * v 
        return 1.0 / (1.0 + math.exp(-logit))

    def convert_to_numpy(self, training_data):
      fields = training_data[0][1].keys()

      field_dtype = [('names', 'a20', (len(fields)),),
                     ('values', 'f4', (len(fields)),)
                     ]

      training_dtype = [('label', 'i4'),
                        ('field_distances', field_dtype)
                        ]

      training_array = numpy.zeros(len(training_data), dtype=training_dtype)

      for i, example in enumerate(training_data) :
        training_array[i] = ((example[0]),
                           (example[1].keys(),
                            example[1].values())
                           )
      return training_array
