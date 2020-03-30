# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:40:18 2019

@author: ana_2
"""

from google_images_download import google_images_download
#instantiate the class
response = google_images_download.googleimagesdownload()
arguments = {"keywords":"lilly,hills","limit":5,"print_urls":True}
paths = response.download(arguments)
#print complete paths to the downloaded images
print(paths)