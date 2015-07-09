import cv2
face_cascade_path = '/usr/local/Cellar/opencv/2.4.11_1/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml'
face_cascade = cv2.CascadeClassifier(face_cascade_path)

scale_factor = 1.2
min_neighbors = 3
min_size = (30, 30)
flags = cv2.cv.CV_HAAR_SCALE_IMAGE

image = cv2.imread("ulm.jpg")

faces = face_cascade.detectMultiScale(image, scaleFactor = scale_factor,
    minNeighbors = min_neighbors, minSize = min_size, flags = flags)
for(x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
### write to file
cv2.imwrite("ulm.faces.jpg", image)
