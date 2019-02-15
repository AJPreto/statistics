import scipy
import scipy.stats
import os
import csv
#!/usr/bin/env python

"""
This script will calculate tau and p_value for two lists.
Can calculate f one way anova and t- test independent
"""


def anova(input_x, input_y):

	tau, p_value = scipy.stats.f_oneway(input_x, input_y)
	return tau, p_value

def t_test(input_x, input_y):

	stat, p_value = scipy.stats.ttest_ind(input_x, input_y)
	return stat, p_value

def open_file(input_file_name, delimiter = ";"):

	opened_file = open(input_file_name, "r").readlines()
	for row in opened_file:
		row = row.replace("\n","")
		yield row.split(delimiter)


def detect_and_split(input_string):

	if "-" in input_string:
		both_values = input_string.split("-")
		average = (float(both_values[0]) + float(both_values[1])) / float(2)
		return average
	if "–" in input_string:
		both_values = input_string.split("–")
		average = (float(both_values[0]) + float(both_values[1])) / float(2)
		return average
	elif input_string == "":
		return None
	else:
		return float(input_string)

def iterate_cols_class(input_file, input_col, target_classes):

	first_class = []
	second_class = []
	for row in input_file[1:]:
		value = float(row[input_col])
		if str(int(row[class_col])) == target_classes[0]:
			first_class.append(value)
		if str(int(row[class_col])) == target_classes[1]:
			second_class.append(value)
	return first_class, second_class


def iterate_cols(input_file, input_col, target_classes):

	first_class = []
	second_class = []

	print(target_classes[0])
	for row in input_file[1:]:
		value = float(row[input_col])
		if (row[other_col] in target_classes[0]) and (str(int(row[class_col])) == target_classes[1][0]):
			first_class.append(value)
		if (row[other_col] in target_classes[0]) and (str(int(row[class_col])) == target_classes[1][1]):
			second_class.append(value)
	return first_class, second_class

def iterate_cols_interface(input_file, input_col, target_classes):

	first_class = []
	second_class = []

	print(target_classes[0])
	for row in input_file[1:]:
		value = float(row[input_col])
		if (row[other_col] in target_classes[0]) and (str(int(row[class_col])) == "3"):
			first_class.append(value)
		if (row[other_col] in target_classes[1]) and (str(int(row[class_col])) == "3"):
			second_class.append(value)
	return first_class, second_class


