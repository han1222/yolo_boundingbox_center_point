import cv2


img= cv2.imread("predictions.jpg", cv2.IMREAD_COLOR)


cv2.circle(img, (382,115), 5, (0,0,255), -1)
cv2.circle(img, (126,112), 5, (0,0,255), -1)
cv2.circle(img, (382,312), 5, (0,0,255), -1)
cv2.circle(img, (131,315), 5, (0,0,255), -1)

# ex) 중심점 (447,63)이고 반지름은 63인 원을 빨간색(0,0,255)으로 하여 굵기속성은 -1로 함으로써 도형을 채움형태로 그린다는 의미

cv2.namedWindow('center points')
cv2.imshow("center points", img)
cv2.waitKey(0)

#imwrite를 사용해서 파일로저장가능 첫번째 매개변수로는 저장할 파일이름 두번쨰 매개변수로는 저장할 이미지변수
cv2.imwrite("savedimage.jpg", img)
#프로그램 종료전 윈도우에대한 자원을 해제한다.
cv2.destoryAllWindows() 

 
