#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER:
# DATE CREATED:
# REVISED DATE:
# PURPOSE: Create the function get_pet_labels that creates the pet labels from
#          the image's filename. This function inputs:
#           - The Image Folder as image_dir within get_pet_labels function and
#             as in_arg.dir for the function call within the main function.
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main.
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##

from os import listdir

def format_label(pet_image):
    low_pet_image = pet_image.lower()
    word_list_pet_image = low_pet_image.split("_")
    pet_name = ""

    for word in word_list_pet_image:
        if word.isalpha():
            pet_name += word + " "

    return pet_name.strip()

def get_pet_labels(image_dir):
    results_dic = dict()

    filename_list = []
    for f in listdir(image_dir):
        if not f.startswith('.'): filename_list.append(f)

    for idx in range(0, len(filename_list), 1):
      results_dic[filename_list[idx]] = [format_label(filename_list[idx])]

    return results_dic
