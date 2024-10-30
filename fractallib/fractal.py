from tqdm import tqdm 
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider,Button
import numpy as np


# Global variables
pixel_density = 0.02 #controls zoom level
length = 200 #same as resultion
mandel_or_julia = False


def fractal(z,c,n=20):
    
    """
    Calculates the fractal value for a given complex number z and constant c, this value tells us how fast the number diverges (escapes).
    formula:  Z_n+1 = Z_n^2 + c

    Args:
        z (complex): Z0
        c (complex): The constant used in the fractal formula.
        n (int): The maximum number of iterations, increase with caution.

    Returns:
        int: The number of iterations before z escapes the threshold.
    """

    for i in range(n):
        z = z**2 + c
        if (abs(z)>2):
            return i

    return n


def fractal_matrix(z,c,n=20,offset = (1/2,1/2),mandel_or_julia = True):
    
    """
    Generate a matrix of fractal values for a grid of complex numbers.

    Args:
        z (complex): The starting complex number if mandel_or_julia is set to True, not important otherwise.
        c (complex): The constant used in the fractal formula if mandel_or_julia is set to False, not important otherwise.
        n (int): The maximum number of iterations.
        offset (tuple): The offset for positioning the fractal, this is because the mandelbrot set is not centered while julia is.
        mandel_or_julia (bool): Flag to determine which fractal to compute, True for mandelbrot False for julia.

    Returns:
        np.ndarray: A 2D array of fractal values.
    """
    
    global length, pixel_density

    mat = np.ndarray((length,length))
    if mandel_or_julia:
        for i in tqdm(range(length), desc="loading",leave = False): # loading bar, for resolution = 20000 , n= 50, this took 30min hence why i needed a loading bar
            for j in range(length):
                coords = (j-offset[0]*length)*pixel_density + (i-length*offset[1])*pixel_density*1j 
                mat[i][j] = fractal(z,coords,n)
    else:
        for i in tqdm(range(length), desc="loading" ,leave = False):
            for j in range(length):
                coords = (j-offset[0]*length)*pixel_density + (i-length*offset[1])*pixel_density*1j
                mat[i][j] = fractal(coords,c,n)

    return mat
            


def mandelbrot_matrix(z,n=20):
    
    """
    Generate a Mandelbrot fractal matrix.

    Args:
        z (complex): The starting complex number.
        n (int): The maximum number of iterations.

    Returns:
        np.ndarray: A 2D array of Mandelbrot fractal values.
    """

    return fractal_matrix(z,0,n,offset = (2/3,1/2))



def is_in_mandelbrot(z=0,c=0,n=20):
    
    """
    Check if a complex number is in the Mandelbrot set.

    Args:
        z (complex): The complex number to be evaluated.
        c (complex): The constant used in the fractal formula.
        n (int): The maximum number of iterations.

    Returns:
        bool: True if z is in the Mandelbrot set, False otherwise.
    """

    return fractal(z,c,n) == n

def julia_matrix(c,n=20):
    
    """
    Generate a Julia fractal matrix.

    Args:
        c (complex): The constant used in the fractal formula.
        n (int): The maximum number of iterations.

    Returns:
        np.ndarray: A 2D array of Julia fractal values.
    """

    return fractal_matrix(0,c,n,mandel_or_julia=False)

def is_in_julia(z=0,c=0,n=20):
    
    """
    Check if a complex number is in the Julia set.

    Args:
        z (complex): The complex number to be evaluated.
        c (complex): The constant used in the fractal formula.
        n (int): The maximum number of iterations.

    Returns:
        bool: True if z is in the Julia set, False otherwise.
    """

    return fractal(z,c,n) == n


def get_image(path='result.png',m_or_j = True,z=0,c=0,n=50,resolution = 2000):
    
    """
    Generate and save a fractal image to a specified file.

    Args:
        path (str): The file path to save the image.
        m_or_j (bool): Flag to determine whether to create a Mandelbrot or Julia fractal.
        z (complex): The starting complex number.
        c (complex): The constant used in the fractal formula.
        n (int): The maximum number of iterations.
        resolution (int): The resolution of the generated image.
    """

    global length
    global pixel_density
    
    length = resolution
    pixel_density = 4/length
    dpi = 300

    m = None
    if m_or_j:
        m = mandelbrot_matrix(z,n=n)
    else:
        m = julia_matrix(c,n=n)
    plt.figure(figsize=(3*length/dpi,3*length/dpi))
    plt.imshow(m,vmin=0,vmax=n,cmap='hot',interpolation='nearest')
    plt.axis('off')
    plt.savefig(path,bbox_inches='tight',pad_inches = 0, dpi =dpi)


    
def show_initial(n=20,resolution = 200):
    
    """
    Display the initial interactive plot for generating fractals. should give you a feel for what the image might look like before making the final render.
    you can dynamically change the starting value (z for mandelbrot, c for julia) as well as switch between mandelbrot set and julia set.

    Args:
        n (int): The maximum number of iterations for fractal calculation.
        resolution (int): The resolution of the displayed plot.
    """

    global length
    global pixel_density
    
    length = resolution
    pixel_density = 4/length
    
    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.1, bottom=0.25)
    img = ax.imshow(julia_matrix(0+0j,n=n),vmin=0,vmax=n,cmap='hot',interpolation='nearest')

    real_num = plt.axes([0.2, 0.15, 0.7, 0.03])
    imaginary_num = plt.axes([0.2, 0.1, 0.7, 0.03])
    button_ax = plt.axes([0.1,0.2,0.1,0.05])
    
    slider_real = Slider(real_num, 'real', -2, 2, valinit=0)
    slider_imaginary = Slider(imaginary_num, 'imaginary', -2, 2, valinit=0)
    button_mandel_or_julia = Button(button_ax,'julia_or_mandel')


    def clicked(_):
        global mandel_or_julia
        mandel_or_julia = not mandel_or_julia
        update(0)


    def update(_):
        re = slider_real.val
        im = slider_imaginary.val
        if mandel_or_julia:
            img.set_data(mandelbrot_matrix(re+im*1j,n=n))
        else:
            img.set_data(julia_matrix(re+im*1j,n=n))
        fig.canvas.draw_idle()

    slider_real.on_changed(update)
    slider_imaginary.on_changed(update)
    button_mandel_or_julia.on_clicked(clicked)


    ax.axis('off')
    plt.show()





