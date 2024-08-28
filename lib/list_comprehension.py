#!/usr/bin/env python3

def return_evens(num_list):
    list = [n for n in num_list if n % 2 == 0]
    return list

def make_exclamation(sentence_list):
    list = [string + "!" for string in sentence_list]
    return list