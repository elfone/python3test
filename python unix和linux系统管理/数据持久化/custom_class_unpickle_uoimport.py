#!/usr/bin/env python3
__author__ = 'Administrator'
import pickle
# import custom_class

pickle_file = open('custom_class.pkl', 'rb')
my_obj = pickle.load(pickle_file)
print(my_obj)
pickle_file.close()