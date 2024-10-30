# fractallib

fractallib is a Python package for generating and visualizing Mandelbrot and Julia fractals. It provides an interactive GUI with adjustable parameters and can export high-resolution images of the generated fractals.

## Table of Contents
- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation

You can install the package using:

```
git clone https://github.com/beloof/fractallib.git
cd fractallib
pip install .
```

## Features

- Generate Mandelbrot and Julia fractals.
- Customize fractal parameters like depth and resolution.
- Interactive GUI with sliders to explore fractal details in real-time.
- Export fractals as high-resolution PNG images.

## Usage

### Basic Mandelbrot Generation

To generate a Mandelbrot fractal matrix, use the following code:

```
from fractallib import get_image

# Generate and save the Mandelbrot fractal
get_image(resolution=2000, n=50)
```

### Generating and Exporting a Julia Fractal

```
from fractallib import get_image

# Generate and save the Julia fractal
get_image(c=-0.4 + 0.6j, resolution=2000, n=50, path='julia_fractal.png')
```


## Examples

Here are some example commands for different types of fractals:

### Basic Mandelbrot Set:

```
fractallib.get_image(resolution=1000, n=100)
```

### High-Resolution Julia Set:

```
fractallib.get_image(c=-0.8 + 0.156j, resolution=3000, n=100, path='high_res_julia.png')
```

### Interactive GUI:

Run an interactive session with sliders to adjust fractal parameters in real-time.

```
fractallib.show_initial(resolution=200, n=20)
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

Special thanks to the Python, matplotlib and numpy communities.

