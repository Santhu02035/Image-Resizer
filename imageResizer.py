

import cv2

img= cv2.imread("millie.jpg")

if img is None:
    print("Error:Image not Found")
    exit()

print("Original image dimensions:",img.shape)

new_width=int(input("Enter new width: "))
new_height=int(input("Enter new height: "))
new_size=(new_width,new_height)

resized_img=cv2.resize(img,new_size)

cv2.imshow("Original Image", img)
cv2.imshow("Resized Image",resized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()