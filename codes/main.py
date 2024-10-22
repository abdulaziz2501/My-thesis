import matplotlib . pyplot as plt
from scipy import misc, ndimage
import numpy as np
import time
import imageio


ascent = misc. ascent ()
brain = imageio.imread('rasm1.png')
print (type( brain ) )
print ( brain . shape, brain . dtype)
# save ﬁle
imageio.imwrite('rasm2.png',  brain )
plt . imshow(ascent)
plt . show()
plt . ﬁgure ( ﬁgsize =(10, 3.6) )
# ﬁrst subplot
plt . subplot (131)
plt . imshow(ascent)
plt . subplot (132)
plt . imshow(ascent, cmap=plt.cm.gray)
plt . axis ('off')
plt . subplot (133)
plt . imshow(ascent[200:220, 200:220], cmap=plt.cm.blue, interpolation ='naerest' )
plt . subplots_adjust (wspace=0, hspace =0.,top =0.99, bottom=0.01,left =0.05, right =0.99)
plt . show()
