import matplotlib.pyplot as plt 
import numpy as np 

#image data
a=np.array([0.7,0.1,0.3,
            0.22,0.433,0.32,
            0.442,0.44,0.344]).reshape(3,3)
"""for the value of "interpolation",check this：
http://matplotlib.org/examples/images_contours_and_fields/interploation_methods.html
"""
plt.imshow(a,interpolation='nearest',cmap='bone',origin='uppper')#生成image图像
plt.colorbar(shrink=0.9)#将colorbar压缩到原来的90%

plt.xticks(())
plt.yticks(())

plt.show()