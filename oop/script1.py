import cv2

img = cv2.imread("galaxy.jpg",0)

print(img)
print(img.shape)

resize_img = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow("galaxy", resize_img)
cv2.imwrite("galaxy2.jpg", resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()