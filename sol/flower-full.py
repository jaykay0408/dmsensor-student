import cv2 as cv
import sys
import imutils

img = cv.imread("flower.png")

if img is None:
    sys.exit("Could not read the image.")

(h, w, d) = img.shape
print("width=", w, "height=", h, "depth=", d)

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("flower-copy.png", img)

# access the RGB pixel located at x=50, y=100, keepind in mind that
# OpenCV stores images in BGR order rather than RGB
(B, G, R) = img[100, 50]
print("R={}, G={}, B={}".format(R, G, B))

# extract a 100x100 pixel square ROI (Region of Interest) from the
# input image starting at x=320,y=60 at ending at x=420,y=160
roi = img[100:400, 50:350]
cv.imshow("ROI", roi)
cv.waitKey(0)

# resize the image to 200x200px, ignoring aspect ratio
resized = cv.resize(img, (200, 200))
cv.imshow("Fixed Resizing", resized)
cv.waitKey(0)

# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio
r = 300.0 / w
dim = (300, int(h * r))
resized = cv.resize(img, dim)
cv.imshow("Aspect Ratio Resize", resized)
cv.waitKey(0)

# let's rotate an image 45 degrees clockwise using OpenCV by first
# computing the image center, then constructing the rotation matrix,
# and then finally applying the affine warp
center = (w // 2, h // 2)
M = cv.getRotationMatrix2D(center, -45, 1.0)
rotated = cv.warpAffine(img, M, (w, h))
cv.imshow("OpenCV Rotation", rotated)
cv.waitKey(0)

# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
blurred = cv.GaussianBlur(img, (11, 11), 0)
cv.imshow("Blurred", blurred)
cv.waitKey(0)

# draw a 2px thick red rectangle surrounding the face
output = img.copy()
cv.rectangle(output, (50, 100), (350, 400), (0, 0, 255), 2)
cv.imshow("Rectangle", output)
cv.waitKey(0)

# draw a blue 20px (filled in) circle on the image centered at
# x=300,y=150
output = img.copy()
cv.circle(output, (300, 150), 20, (255, 0, 0), -1)
cv.imshow("Circle", output)
cv.waitKey(0)

# draw a 5px thick red line from x=60,y=20 to x=300,y=200
output = img.copy()
cv.line(output, (60, 20), (300, 200), (0, 0, 255), 5)
cv.imshow("Line", output)
cv.waitKey(0)

# draw green text on the image
output = img.copy()
cv.putText(output, "Anyone Python with OpenCV", (10, 25),
	cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv.imshow("Text", output)
cv.waitKey(0)

# convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)
cv.waitKey(0)

# applying edge detection we can find the outlines of objects in
# images
edged = cv.Canny(gray, 250, 500)
cv.imshow("Edged", edged)
cv.waitKey(0)

# threshold the image by setting all pixel values less than 165
# to 0 (black; background) and all pixel values >= 165 to 255
# (while; foreground), thereby segmenting the image
thresh = cv.threshold(gray, 165, 255, cv.THRESH_BINARY)[1]
cv.imshow("Thresh", thresh)
cv.waitKey(0)

# find contours (i.e., outlines) of the foreground objects in the
# thresholded image
cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL,
                       cv.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = img.copy()
# loop over the contours
for c in cnts:
    # draw each contour on the output image with a 3px thick purple
    # outline, then display
    cv.drawContours(output, [c], -1, (240, 0, 159), 3)
cv.imshow("Contours", output)
cv.waitKey(0)