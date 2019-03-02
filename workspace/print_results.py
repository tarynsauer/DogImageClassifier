#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#
# PROGRAMMER: Taryn Sauer
# DATE CREATED: 3/1/19
# REVISED DATE:
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results
#          dictionary (results_dic).
#         This function inputs:
#            -The results dictionary as results_dic within print_results
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main.
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##

def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    print(f"\n** Results for {model.upper()} Model Architecture:\n")

    for key, value in results_stats_dic.items():
        print(f"{key}: {value}")

    if print_incorrect_dogs:
        print("\n** Incorrect dogs:\n")
        for key, value in results_dic.items():
            if (value[3] == 1) and (value[2] != value[4]):
              print(f"{value[0]} is incorrectly classified as {value[1]}")

    if print_incorrect_breed:
        print("\n** Incorrect breeds:\n")
        for key, value in results_dic.items():
            if (value[3] == 1) and (value[2] == 0):
              print(f"{value[0]} is incorrectly classified as {value[1]}")

    None
