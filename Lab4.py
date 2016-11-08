from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
from scipy.ndimage import filters
import scipy.misc
from scipy import fftpack
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm 

im = array(Image.open('Images/cat_small.jpg').convert('L'))
plt.gray()

im3_g = filters.gaussian_filter(im, 3)
im5_g = filters.gaussian_filter(im, 5)
im10_g = filters.gaussian_filter(im, 10)

#Sigma = 3
imx1 = zeros(im3_g.shape)    
filters.sobel(im3_g,1,imx1)    
imy1 = zeros(im3_g.shape)    
filters.sobel(im3_g,0,imy1)    
magnitude_s3 = sqrt(imx1**2+imy1**2)
#Sigma = 5
imx2 = zeros(im5_g.shape)    
filters.sobel(im5_g,1,imx2)    
imy2 = zeros(im5_g.shape)    
filters.sobel(im5_g,0,imy2)    
magnitude_s5 = sqrt(imx2**2+imy2**2)

#Sigma = 10
imx3 = zeros(im10_g.shape)    
filters.sobel(im10_g,1,imx3)    
imy3 = zeros(im10_g.shape)    
filters.sobel(im10_g,0,imy3)    
magnitude_s10 = sqrt(imx3**2+imy3**2)

def getFig():

    ax = []
    ax.append(plt.subplot2grid((2,3), (0,1)))
    ax.append(plt.subplot2grid((2,3), (1,0)))
    ax.append(plt.subplot2grid((2,3), (1,1)))
    ax.append(plt.subplot2grid((2,3), (1,2)))
    return ax

def Task():
    ax = getFig()
    ax[0].imshow(im)
    ax[0].axis('off')
    
    ax[1].imshow(magnitude_s3)
    ax[1].axis('off')

    ax[2].imshow(magnitude_s5)
    ax[2].axis('off')
    
    ax[3].imshow(magnitude_s10)
    ax[3].axis('off')
    
    plt.show()
Task()