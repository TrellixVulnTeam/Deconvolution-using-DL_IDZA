# required libraries
import numpy as np
import pandas as pd
import math
import scipy
import matplotlib.pyplot as plt
from scipy.stats import norm,binom
from scipy.io import loadmat
from scipy.special import digamma, gammaln, gamma
from numpy.linalg import inv
import glob
from scipy import ndimage
from PIL import Image
import os, sys
from scipy import signal

# first dataset load

class Image_data(object):
    """
    all functions related to data loading and creating convoluted images

    """

    def __init__(self, npyfilename, kernel_file_name):

        """
          npyfilename : names of .npy files to load
          kernel_file_name: Kernel to be loaded
         """
        
       
        #self.original_images = np.vstack([np.load(npyfilename1),np.load(npyfilename2)])
        self.original_images = np.load(npyfilename)
        kernel = loadmat(kernel_file_name)
        self.kernel = kernel['A']

        self.total_image_num = self.original_images.shape[0]
        print('original images loaded')
    
    def compute_image_conv(self):
        conv_images = np.zeros_like(self.original_images)
        for i in range(self.total_image_num):
            conv_images[i] = signal.fftconvolve(self.original_images[i],self.kernel,mode = 'same')
        self.conv_images = conv_images
        print('conv images created')

    def load_data(self):
        return self.original_images, self.conv_images
            
    






