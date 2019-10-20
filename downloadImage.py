from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

key = input("Enter your key: ")
num_img = int(input("Enter number of image: "))

arguments = {"keywords":key,"limit":num_img,"print_urls":True}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)