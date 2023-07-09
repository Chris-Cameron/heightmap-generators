import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import math, random

noise1 = PerlinNoise(octaves=4)
noise2 = PerlinNoise(octaves=8)
noise3 = PerlinNoise(octaves=16)
noise4 = PerlinNoise(octaves=32)

xpix, ypix = 1024, 512
pic = []
north_pole = 2*random.random()-1
south_pole = 2*random.random()-1
for i in range(xpix):
    row = []
    for j in range(ypix):
        noise_val = noise1([i/xpix, j/ypix])
        noise_val += 0.5 * noise2([i/xpix, j/ypix])
        noise_val += 0.25 * noise3([i/xpix, j/ypix])
        noise_val += 0.125 * noise4([i/xpix, j/ypix])
        
        #Reduce near dateline
        noise_val += 1
        noise_val = noise_val*(-1*((1-(2*(j/ypix)))**8)+1)
        noise_val -= 1

        #Constant Poles
        north_ratio = max(1-(i/xpix)*10, 0)
        south_ratio = max((i/xpix)*10-9, 0)

        noise_val = north_ratio*north_pole + south_ratio*south_pole + (1-north_ratio-south_ratio)*noise_val
            
        #print(noise_val)

        row.append(noise_val)
    pic.append(row)

plt.figure(figsize = (8, 4), dpi = 128)
plt.axis('off') #Remove gridlines for ease of use
plt.gca().set_position((0, 0, 1, 1))

plt.pcolormesh(pic, cmap='gray')
plt.show()
