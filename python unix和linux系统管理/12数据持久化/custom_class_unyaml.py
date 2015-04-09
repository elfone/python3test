#!/usr/bin/env python3
__author__ = 'Administrator'
import yaml
import custom_class

yaml_file = open('custom_class.yaml', 'r')
my_obj = yaml.load(yaml_file)
print(my_obj)
yaml_file.close()