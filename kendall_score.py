#!/usr/bin/env python

"""
This script will calculate kendall and p_value for two lists
"""

import scipy
import scipy.stats
import os
import csv

__author__ = "A.J. Preto"
__email__ = "martinsgomes.jose@gmail.com"
__group__ = "Data-Driven Molecular Design"
__group_leader__ = "Irina S. Moreira"
__project__ = "No specific project"

def kendall_and_p_value(input_x, input_y):

	tau, p_value = scipy.stats.kendalltau(input_x, input_y)
	return tau, p_value


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

def iterate_cols(input_file, input_col_1, input_col_2):
	predicted_list = []
	experimental_list = []
	for row in input_file[1:]:
		predicted = float(row[input_col_1])
		experimental =  detect_and_split(row[input_col_2])
		if experimental != None:
			predicted_list.append(predicted)
			experimental_list.append(experimental)
		else:
			continue
	return predicted_list, experimental_list
