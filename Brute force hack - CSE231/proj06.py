#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:11:45 2017

@author: jasonkirschsmacbookpro
"""

#Project 6, hacking passwords


from itertools import product
import time
import zipfile

print("Hacking into computer systems is a direct offense of US federal law")
print("You are breaking the Computer Fraud and Abuse Act")
print("The maximum prison sentence for this is one year")

def open_dict_file(): 
    
    dict_reference = input("Enter a dictionary name:")
    try:
        dict_file = open(dict_reference, 'r')
        return dict_file
    except FileNotFoundError:
        print("File not found:")
        dict_file = input("Enter a dictionary name:")

def open_zip_file():
    
    zip_reference = input("Enter a zip name:")
    try:
        zip_file = zipfile.ZipFile(zip_reference)
        return zip_file
    except FileNotFoundError:
        print("File not found:")
        zip_file = input("Enter a zip name:")
        
def brute_force_attack(zip_file):
    for i in range (1,9):
        letters = "abcdefghijklmnopqrstuvwxyz"
        for items in product(str(letters), repeat=8):
            try:
                password = (''.join(items))
                zip_file.extractall(pwd=password.encode())
                return password
            except:
                return 'Password not found'
            
def dictionary_attack(zip_file, dict_file):
    for line in dict_file:
        line = line.strip()
        
        try:
            password = line
            zip.file.extractall(pwd=password.encode())
            return password
        except:
            return 'Password not found'
attack_type = input("What method of attack (dictionary, brute force, q, both): ")
while attack_type != "q" :   
    if attack_type == "dictionary":
        print("Beginning to solve the password")
        start = time.process_time()
        zip_file = open_zip_file()
        dict_file = open_dict_file()
        dictionary_attack(zip_file, dict_file)
        print(dictionary_attack(zip_file, dict_file))
        end = time.process_time()
        time = end - start

        print("The dictionary attack took (seconds):{:.4}".format(time) )
    
        attack_type = input("What method of attack (dictionary, brute force, q, both): ")

    elif attack_type == "brute force":
        print("Beginning to brute force the problem")
        start = time.process_time()
        end = time.process_time()
        time = end - start
        print(brute_force_attack(zip_file))
        print("The brute force attack took(seconds):{:.4}".format(time) )
    
        attack_type = input("What method of attack (dictionary, brute force, q, both): ")
    elif attack_type == "both":
        print("Beginning both attacks")
        start = time.process_time()
        dictionary_attack(zip_file, dict_file) 
        print(dictionary_attack(zip_file, dict_file))
        print("The dictionary attack took (seconds):{:.4}".format(time) )
        if dictionary_attack(zip_file, dict_file) == 'Password not found':
        
            brute_force_attack(zip_file)
            end = time.process_time()
            time = end - start
            print(brute_force_attack(zip_file))
            print("The brute force attack took(seconds):{:.4}".format(time) )
        attack_type = input("What method of attack (dictionary, brute force, q, both): ")

        
        
            
    
    
