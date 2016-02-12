from pprint import pprint

folder = "/home/iammint/coding/205-CST/Proj1/Project1Images/"

pictures = []

image1 = makePicture(folder + "1.png")
pictures.append(image1)
image2 = makePicture(folder + "2.png")
pictures.append(image2)
image3 = makePicture(folder + "3.png")
pictures.append(image3)
image4 = makePicture(folder + "4.png")
pictures.append(image4)
image5 = makePicture(folder + "5.png")
pictures.append(image5)
image6 = makePicture(folder + "6.png")
pictures.append(image6)
image7 = makePicture(folder + "7.png")
pictures.append(image7)
image8 = makePicture(folder + "8.png")
pictures.append(image8)
image9 = makePicture(folder + "9.png")
pictures.append(image9)

for x in range(0,9):
  show(pictures[x])

height = getHeight(pictures[0])
width = getWidth(pictures[0])

newImage = makeEmptyPicture(width, height)

pixelsImage1 = getPixels(pictures[0])
pixelsImage2 = getPixels(pictures[1])
pixelsImage3 = getPixels(pictures[2])
pixelsImage4 = getPixels(pictures[3])
pixelsImage5 = getPixels(pictures[4])
pixelsImage6 = getPixels(pictures[5])
pixelsImage7 = getPixels(pictures[6])
pixelsImage8 = getPixels(pictures[7])
pixelsImage9 = getPixels(pictures[8])

newImagePixels = getPixels(newImage)

for x in range(0,(height * width)):
  redList = []
  greenList = []
  blueList = []
  
  pixel = pixelsImage1[x]
  redList.append(getRed(pixel))
  greenList.append(getGreen(pixel))
  blueList.append(getBlue(pixel))
  
  pixel = pixelsImage2[x]
  redList.append(getRed(pixel))
  greenList.append(getGreen(pixel))
  blueList.append(getBlue(pixel))
  
  pixel = pixelsImage3[x]
  redList.append(getRed(pixel))
  greenList.append(getGreen(pixel))
  blueList.append(getBlue(pixel))
  
  pixel = pixelsImage4[x]
  redList.append(getRed(pixel))
  greenList.append(getGreen(pixel))
  blueList.append(getBlue(pixel))
  
  pixel = pixelsImage5[x]
  redList.append(getRed(pixel))
  greenList.append(getGreen(pixel))
  blueList.append(getBlue(pixel))
  
  pixel = pixelsImage6[x]
  redList.append(getRed(pixel))
  greenList.append(getGreen(pixel))
  blueList.append(getBlue(pixel))
  
  pixel = pixelsImage7[x]
  redList.append(getRed(pixel))
  greenList.append(getGreen(pixel))
  blueList.append(getBlue(pixel))
  
  pixel = pixelsImage8[x]
  redList.append(getRed(pixel))
  greenList.append(getGreen(pixel))
  blueList.append(getBlue(pixel))
  
  pixel = pixelsImage9[x]
  redList.append(getRed(pixel))
  greenList.append(getGreen(pixel))
  blueList.append(getBlue(pixel))
  
  redList.sort()
  greenList.sort()
  blueList.sort()
  
  setRed(newImagePixels[x], redList[4])
  setGreen(newImagePixels[x], greenList[4])
  setBlue(newImagePixels[x], blueList[4])
  
show(newImage) 







