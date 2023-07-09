import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import math

#noise1 = PerlinNoise(octaves=4)
noise2 = PerlinNoise(octaves=8)
noise3 = PerlinNoise(octaves=16)
noise4 = PerlinNoise(octaves=32)

xpix, ypix = 512, 512
pic = []
for i in range(xpix):
    row = []
    for j in range(ypix):
        #noise_val = math.exp(i/xpix) #Make terrain slope downwards
        noise_val = math.atan((3*i)/xpix)+(math.pi/2)
        noise_val += 0.5 * noise2([i/xpix, j/ypix])
        noise_val += 0.25 * noise3([i/xpix, j/ypix])
        noise_val += 0.125 * noise4([i/xpix, j/ypix])
        
        #Make terrain flatter near coast
        noise_val = noise_val**6

        row.append(noise_val)
    pic.append(row)

plt.figure(figsize = (4, 4), dpi = 128)
plt.axis('off') #Remove gridlines for ease of use
plt.gca().set_position((0, 0, 1, 1))

plt.pcolormesh(pic, cmap='gray')
plt.show()
