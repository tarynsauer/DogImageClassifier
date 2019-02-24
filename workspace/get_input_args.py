#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#
# PROGRAMMER: Taryn Sauer
# DATE CREATED: 2/24/19
# REVISED DATE:
# PURPOSE: Create a function that retrieves the following 3 command line inputs
#          from the user using the Argparse Python module. If the user fails to
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
import argparse

def get_input_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--dir', type = str, default = 'pet_images/', help = 'path to the folder of pet images')
    parser.add_argument('--arch', type = str, default = 'vgg', help = 'CNN model architecture')
    parser.add_argument('--dogfile', type = str, default = 'dognames.txt', help = 'text file with dog names')

    return parser.parse_args()
