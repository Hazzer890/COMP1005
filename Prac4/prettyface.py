#
# prettyface.py
#
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy import misc

face = misc.face(gray=True)
face = ndimage.shift(face, (50,50))
face = ndimage.rotate(face, 30)
face = face[100:-100,100:-100]
plt.imshow(face)
plt.imshow(face, cmap=plt.cm.magma)
plt.show()
