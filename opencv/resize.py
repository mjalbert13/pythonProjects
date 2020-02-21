import cv2
import glob

imList = glob.glob("*.jpg")

for image in imList:
    img = cv2.imread(image, 0)
    rs = cv2.resize(img, (100,100))
    cv2.imshow("Hey", rs)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized"+image, rs)
