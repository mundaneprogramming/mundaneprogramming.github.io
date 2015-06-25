import cv2
import os
DEFAULT_FACES_CASCADE_PATH = '/usr/local/Cellar/opencv/2.4.11_1/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml'
face_cascade_path = DEFAULT_FACES_CASCADE_PATH
face_cascade = cv2.CascadeClassifier(face_cascade_path)
infname = "/tmp/ulm.jpg"
base_outfname = os.path.basename(infname)
scale_factor = 1.2
min_neighbors = 3
min_size = (30, 30)
flags = cv2.cv.CV_HAAR_SCALE_IMAGE
# open the file
image = cv2.imread(os.path.expanduser(infname))
faces = face_cascade.detectMultiScale(image, scaleFactor = scale_factor,
    minNeighbors = min_neighbors, minSize = min_size, flags = flags)

for i, (x, y, w, h) in enumerate(faces):
  img = image[y:y+h, x:x+w]
  outfname = "/tmp/%s.faces--%dx%d_%dx%d.jpg" % (base_outfname, x, y, w, h)
  cv2.imwrite(outfname, img)
  print("Wrote face:", outfname)
