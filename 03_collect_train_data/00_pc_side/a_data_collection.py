#!/usr/bin/env python3
# -*- coding: utf-8 -*-  

# setting up modules used in the program
import b_futaba_client_interface
from datetime import datetime
from pygame.locals import *
from numpy import load
import numpy as np
import pygame
import socket
import shutil
import glob
import time
import cv2
import sys
import os

class DataCollection(object):

    def __init__(self):

        # check os compatibility
        if os.name != 'nt':

            print ("\nThis codes only compatible with Windows OS!")
            exit()

        # check python environment compatibility
        if sys.version_info[0] < 3:

            print ("\nThis codes only compatible with Python 3 environment!")
            exit()

        # clear screen and print out info
        os.system("cls")

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('192.168.2.105', 8000)) # change '〇.〇.〇.〇' to user's PC IP address
        self.server_socket.listen(0)
        # accept a single connection ('rb' is 'read binary')
        self.connection = self.server_socket.accept()[0].makefile('rb')
        # establish a condition that RPi should be sending images
        self.send_inst = True
        # create labels 
        # aka the Y values; these will be the directional output for override Futaba T10J
        self.k = np.zeros((3, 3), 'float')
        # creates a 3x3 matrix, with 1's along the diagonal, upper left to bottom right:
        # array([[ 1.,  0.,  0.],
        #        [ 0.,  1.,  0.],
        #        [ 0.,  0.,  1.])
        for i in range(3):

            self.k[i, i] = 1

        self.temp_label = np.zeros((1, 3), 'float')
        pygame.init()
        pygame.display.set_mode((250, 250))
        self.collect_images()


    def collect_images(self):

        # frame counts
        saved_frame = 0
        total_frame = 0

        # click counts
        clicks_forward = 0
        clicks_forward_left = 0
        clicks_forward_right = 0

        # specify the main folder path, temporary folder path, subfolder path, temporary subfolder path and file name
        file = "label_array.npz"
        folder = "00_training_data"
        subfolder = "00_unfiltered_image"
        temp_folder = "TEMP_training_data"
        temp_subfolder = "TEMP_unfiltered_image"  

        # if the folder/subfolder path doesn't exist create empty path
        if not os.path.exists(folder + "/" + subfolder):

            os.makedirs(folder + "/" + subfolder)

        # if temp_folder/temp_subfolder exist delete all path
        if os.path.exists(temp_folder):
        
            shutil.rmtree(temp_folder)

        # if temp_folder/temp_subfolder doesn't exist create empty path
        if not os.path.exists(temp_folder + "/" + temp_subfolder):

            os.makedirs(temp_folder + "/" + temp_subfolder)

        print ("Data are going to be collected and saved in 00_training_data folder for filtered")
        print ("image and 00_training_data/00_unfiltered_image folder for unfiltered images.")
        print ("Meanwhile collected user input will be saved in 00_training_data only.\n")

        print("To start recording press arrow keys on Pygame window to move the rover")
        print("To quit press [q] key on Pygame window to end the program.\n")

        label_array = np.zeros((1, 3), 'float')

        # stream video frames one by one
        try:

            stream_bytes = b' '
            frame = 0

            while self.send_inst:

                stream_bytes += self.connection.read(1024)
                # first stream byte for the jpeg video
                first = stream_bytes.find(b'\xff\xd8')
                # last stream byte for the jpeg video
                last = stream_bytes.find(b'\xff\xd9')

                if first != -1 and last != -1:

                    jpg = stream_bytes[first:last + 2]
                    stream_bytes = stream_bytes[last + 2:]

                    # 'image0' original image in color cropped to x = 320 and y = 120 for livestreaming
                    image0 = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)[120:240, :]
                    # 'image1' original image in color cropped to x = 320 and y = 120 for storing
                    image1 = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)[120:240, :]
                    # 'image2' filtered image1 using canny edge for storing
                    image2 = cv2.Canny(image1, 200, 300)

                    # overlay click counts: cv2.putText(clicks_*)
                    clicks_total = clicks_forward + clicks_forward_left + clicks_forward_right
                    cv2.putText(image0, "FW: {}, LT: {}, RT: {}, TOTAL: {}".format(clicks_forward, clicks_forward_left, clicks_forward_right, clicks_total), (10, 30), cv2.FONT_HERSHEY_DUPLEX, .45, (0, 255, 0), 1)

                    # display feeds on host (pc)
                    cv2.imshow("Video Feed", image0)

                    # calculate frame and total frame
                    frame += 1
                    total_frame += 1

                    # get user input to control the rover
                    for event in pygame.event.get():

                        # when the key was pressed down
                        if event.type == KEYDOWN:
                            
                            # register the pressed down key
                            key_input = pygame.key.get_pressed()

                            # get the current time
                            timestr = datetime.now().strftime("%Y%m%d%H%M%S%f")

                            # forward right
                            if key_input[pygame.K_RIGHT]:

                                # save streamed images (image1 = original, image2 = filtered)
                                cv2.imwrite(temp_folder + '/' + temp_subfolder + '/' + '{}.jpg'.format(timestr), image1)
                                cv2.imwrite(temp_folder + '/' + '{}.jpg'.format(timestr), image2)
                                # (→) self.k[2] = [ 0.,  0.,  1.]
                                label_array = np.vstack((label_array, self.k[2]))
                                # move forward & turn right
                                b_futaba_client_interface.forward_right()
                                clicks_forward_right += 1
                                saved_frame += 1
                                print("Right")

                            # forward
                            elif key_input[pygame.K_UP]:

                                # save streamed images (image1 = original, image2 = filtered)
                                cv2.imwrite(temp_folder + '/' + temp_subfolder + '/' + '{}.jpg'.format(timestr), image1)
                                cv2.imwrite(temp_folder + '/' + '{}.jpg'.format(timestr), image2)
                                # (↑) self.k[1] = [ 0.,  1.,  0.]
                                label_array = np.vstack((label_array, self.k[1]))
                                # move forward
                                b_futaba_client_interface.forward()
                                clicks_forward += 1
                                saved_frame += 1
                                print("Forward")

                            # forward left
                            elif key_input[pygame.K_LEFT]:

                                # save streamed images (image1 = original, image2 = filtered)
                                cv2.imwrite(temp_folder + '/' + temp_subfolder + '/' + '{}.jpg'.format(timestr), image1)
                                cv2.imwrite(temp_folder + '/' + '{}.jpg'.format(timestr), image2)
                                # (←) self.k[0] = [ 1.,  0.,  0.]
                                label_array = np.vstack((label_array, self.k[0]))
                                # move forward & turn left
                                b_futaba_client_interface.forward_left()
                                clicks_forward_left += 1
                                saved_frame += 1
                                print("Left")

                            # reverse; not saving images for this
                            elif key_input[pygame.K_DOWN]:
                                
                                # reverse
                                b_futaba_client_interface.reverse()
                                print("Reverse (Input not recorded)")

                            # brake; not saving images for this
                            elif key_input[pygame.K_b]:
                                
                                # brake
                                b_futaba_client_interface.brake()
                                print("Brake (Input not recorded)")

                            # to end the program press [q] key on Pygame window
                            elif key_input[pygame.K_q]:

                                b_futaba_client_interface.close_socket()
                                self.send_inst = False
                                os.system("cls")
                                break

                        # when the key were lifted loop back
                        elif event.type == pygame.KEYUP:
                            
                            time.sleep(0.3)
                            break

            # list all folders/files exist inside the temp_subfolder directory
            temp_subfolder_filelist = os.listdir(temp_folder + "/" + temp_subfolder)
            
            # move temp_subfolder content to subfolder
            for a in temp_subfolder_filelist:

                shutil.move(temp_folder + "/" + temp_subfolder + "/" + a, folder + "/" + subfolder)
            
            #delete temp_subfolder
            shutil.rmtree(temp_folder + "/" + temp_subfolder)

            # move temp_folder content to folder and delete temp_folder
            temp_folder_filelist = os.listdir(temp_folder)
            
            # move temp_folder content to folder
            for b in temp_folder_filelist:

                shutil.move(temp_folder + "/" + b, folder)
            
            #delete temp_folder
            shutil.rmtree(temp_folder)

            # save collected user input in specified folder
            # NOTE: there is no need to create duplicate because the same npz file can be applied on filtered/unfiltered images
            if not os.path.exists(folder + '/' + file):
            
                train_labels = label_array[1:, :]
                np.savez(folder + '/' + file, train_labels = train_labels)

            else:
                
                # save new .npz to tmp file
                train_labels = label_array[1:, :]
                np.savez(folder + '/tmp.npz', train_labels = train_labels)
                # load the original .npz file
                data1 = load(folder + '/' + file)
                lst1 = data1.files

                for item in lst1:    
                    
                    a = (data1[item])
                    data1.close()

                # delete the original .npz file
                os.remove(folder + '/' + file)
                # load the new .npz temp file
                data2 = load(folder + '/tmp.npz')
                lst2 = data2.files
                
                for item in lst2:    
    
                    b = (data2[item])
                    data2.close()

                # delete the new .npz temp file
                os.remove(folder + '/tmp.npz')
                # concatenate 2 tuples into 1 tuple
                c = np.concatenate((a, b), 0)
                # save the concatenate tuple into .npz
                np.savez(folder + '/' + file, train_labels = c)

            # click counter
            print("[Click counter]")
            print("» Forward clicks: ", clicks_forward)
            print("» Forward-left clicks: ", clicks_forward_left)
            print("» Forward-right clicks: ", clicks_forward_right)

            # frame counter
            print("\n[Frame counter]")
            print("» Total frame: ", total_frame)
            print("» Saved frame: ", saved_frame)
            print("» Dropped frame: ", total_frame - saved_frame)

            print ("\nData collection will quit in 5 seconds.")
            time.sleep(5)
            os.system("cls")

        finally:
            
            self.connection.close()
            self.server_socket.close

if __name__ == '__main__':

    DataCollection()