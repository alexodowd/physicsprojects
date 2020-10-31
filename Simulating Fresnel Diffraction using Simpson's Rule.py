import numpy as np
import matplotlib.pyplot as plt

print("""
      
Welcome to Alex's Simpson's Rule Integrator - Demonstrated via Fresnel Diffraction!""")

L = input("Enter a Wavelength: ")
z = input("Enter desired screen-apperture distance (m): ")
N = input("Number of intervals: ")

L = float(L)
z = float(z)
N = int(N)
k = 2*np.pi/(L)
PointNumber = N + 1
E0 = 1
x = np.linspace(-5e-3, 5e-3, N)

#Simposon's Rule: (∆x/3) = [f(x0) + 4f(x1) + 2f(x2) + 4f(x3) + 2f(x4) + ... + 4f(xn-1) + f(xn)]

def E(f, x1, x2):
    odd = 0
    h = (x2-x1)/N
    for i in range(1, N//2 + 1): #odd x values
        odd += f(x1 + (2*i - 1)*h)
    even = 0
    for i in range(1, N//2): #even x values
        even += f(x1 + h*2*i)
    return (h/3)*(f(x1) + f(x2) + 4*odd + 2*even)

def f(x0):
    return np.real(np.exp(((1j*k)/(2*z))*(x-x0)**2)) * (k*E0)/(2*z*np.pi)

E1D = abs(E(f, -1e-5, 1e-5))**2
plt.plot(x, E1D)
plt.ylabel('Relative Intensity')
plt.xlabel('Screen Coordinate')
plt.title('1-D Fresnel Diffraction')
plt.show()

print("""
      
Please wait whilst the 2D image loads...
(May take ~20 seconds)""")


intensity = np.zeros((N,N))
for i in range(N):
    for j in range(N):                      #x1 - x2                    #y1 - y2
        intensity[i,j] = abs(E(f, -1e-5, 1e-5)[i] * E(f, -1e-5, 1e-5)[j])**2 * (k*E0)/(2*z*np.pi)
    
plt.imshow(intensity)
plt.title("2-D Fresnel Diffraction")
plt.show()

