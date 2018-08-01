'''
This module gives them a number and converts to jpg
'''

import cv2
import os

PATH_TO_RAW_DATA = '../raw'
PATH_TO_CLEANED_DATA = '../cleaned'
VALID_IMAGE_TYPES = ['png','jpeg','jpg','bmp']

def process_dir(dir_name):
    '''
    Processes all images in the directory
    '''

    counter = 0
    
    # For all image files in directory
    input_directory = os.path.join(PATH_TO_RAW_DATA, dir_name)
    for file in os.listdir(input_directory):
        if file.split('.')[-1] in VALID_IMAGE_TYPES:
            # Read the image
            full_path = os.path.join(input_directory,file)
            img = cv2.imread(full_path)

            # Write the image back
            destination_dir = os.path.join(PATH_TO_CLEANED_DATA, dir_name)
            if not os.path.exists(destination_dir):
                os.mkdir(destination_dir)
            new_file_path =  os.path.join(destination_dir, '%03d.jpg'%counter)
            cv2.imwrite(new_file_path,img)

            # Update the counter
            counter += 1

    print(dir_name, counter)

if __name__ == '__main__':
    for file in os.listdir(PATH_TO_RAW_DATA):
        if os.path.isdir(os.path.join(PATH_TO_RAW_DATA,file)):
            process_dir(file)
