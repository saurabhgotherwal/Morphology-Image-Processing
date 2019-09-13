# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 08:45:20 2018

@author: HP
"""
import numpy as np
import cv2 as cv


def GetPadddedImage(image):       
    imagePadded = np.asarray([[ 0 for x in range(0,image.shape[1] + 2)] for y in range(0,image.shape[0] + 2)], dtype =np.uint8)
    imagePadded[1:(imagePadded.shape[0]-1), 1:(imagePadded.shape[1]-1)] = image 
    return imagePadded 

def IsKernelHittingImage(imagePortion, kernel):
    result = np.logical_and(imagePortion, kernel)
    isHitting = (True in result) == True 
    return isHitting

def IsKernelFullyHittingImage(imagePortion, kernel):
    result = np.logical_and(imagePortion, kernel)
    isHitting = (False in result) == True 
    return np.logical_not(isHitting)

def DilateImage(image, kernel, kernelCenter):
    dilatedImage = np.zeros(image.shape,dtype = np.uint8)
    imagePortion = np.zeros(kernel.shape,dtype = np.uint8)
    imagePadded = GetPadddedImage(image) 
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            imagePortion = imagePadded[i:i+imagePortion.shape[0],j:j+imagePortion.shape[1]]
            isHitting = IsKernelHittingImage(imagePortion,kernel)
            if(isHitting):
                dilatedImage[i][j] = 255
            else:
                dilatedImage[i][j] = image[i][j]                
                
    return dilatedImage

def ErodeImage(image, kernel, kernelCenter):
    erodedImage = np.zeros(image.shape,dtype = np.uint8)
    imagePortion = np.zeros(kernel.shape,dtype = np.uint8)
    imagePadded = GetPadddedImage(image) 
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            imagePortion = imagePadded[i:i+imagePortion.shape[0],j:j+imagePortion.shape[1]]
            isHitting = IsKernelFullyHittingImage(imagePortion,kernel)
            if(isHitting):
                erodedImage[i][j] = 255
                           
    return erodedImage

def Opening(image, kernel, kernelCenter):
    outputImage = np.zeros(image.shape,dtype = np.uint8)    
    erodedImage = np.zeros(image.shape,dtype = np.uint8)
    
    erodedImage = ErodeImage(image, kernel, kernelCenter)
    outputImage = DilateImage(erodedImage, kernel, kernelCenter)
    
    return outputImage

def Closing(image, kernel, kernelCenter):
    outputImage = np.zeros(image.shape,dtype = np.uint8)    
    dilatedImage = np.zeros(image.shape,dtype = np.uint8)
    
    dilatedImage = DilateImage(image, kernel, kernelCenter)
    outputImage = ErodeImage(dilatedImage, kernel, kernelCenter)    
    
    return outputImage


def GetBoundary(image, kernel, kernelCenter):
    outputImage = np.zeros(image.shape,dtype = np.uint8)    
    erodedImage = np.zeros(image.shape,dtype = np.uint8)
    
    erodedImage = ErodeImage(image, kernel, kernelCenter)
    
    outputImage = image - erodedImage
    
    return outputImage

img = cv.imread('noise.jpg',0)
kernel = np.asarray([[255,255,255],[255,255,255],[255,255,255]])
kernelCenter = np.asarray([1,1])

closedImage_1 = Closing(img,kernel, kernelCenter)
openedImage_1 = Opening(closedImage_1,kernel, kernelCenter)

img = cv.imread('noise.jpg',0)
kernel = np.asarray([[255,255,255],[255,255,255],[255,255,255]])
kernelCenter = np.asarray([1,1])

openedImage_2 = Opening(img,kernel, kernelCenter)
closedImage_2 = Closing(openedImage_2,kernel, kernelCenter)

boundary_1 = GetBoundary(openedImage_1, kernel, kernelCenter)

boundary_2 = GetBoundary(closedImage_2, kernel, kernelCenter)

cv.imwrite('res_noise1.jpg',openedImage_1)

cv.imwrite('res_noise2.jpg',closedImage_2)

cv.imwrite('res_bound1.jpg',boundary_1)

cv.imwrite('res_bound2.jpg',boundary_2)