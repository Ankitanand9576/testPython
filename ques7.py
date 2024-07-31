"""Use the os module to create a new directory. """
import os
os.mkdir(path="test/",input("enter directory name :"))
print(os.listdir())