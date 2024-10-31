# fractallib/__main__.py
import argparse
from .fractal import get_image, show_initial

def main():
    parser = argparse.ArgumentParser(description="Generate fractal images with fractallib.")
    parser.add_argument(
        "type", choices=["mandelbrot", "julia"], help="Type of fractal to generate (mandelbrot or julia)"
    )
    parser.add_argument(
        "--real", type=float, default=0, help="Real part of complex constant (only for Julia set)"
    )
    parser.add_argument(
        "--imaginary", type=float, default=0, help="Imaginary part of complex constant (only for Julia set)"
    )
    parser.add_argument(
        "-o", "--output", type=str, default="result.png", help="Output file path for the generated image"
    )
    parser.add_argument(
        "-n", "--iterations", type=int, default=50, help="Maximum number of iterations"
    )
    parser.add_argument(
        "-r", "--resolution", type=int, default=2000, help="Resolution of the generated image"
    )
    parser.add_argument(
        "--show", action="store_true", help="Show an interactive preview of the fractal"
    )

    args = parser.parse_args()

    if args.show:
        show_initial(n=args.iterations, resolution=args.resolution)
    else:
        c = complex(args.real, args.imaginary)
        m_or_j = args.type == "mandelbrot"
        get_image(
            path=args.output, 
            m_or_j=m_or_j, 
            z=0 if m_or_j else None, 
            c=c if not m_or_j else None, 
            n=args.iterations, 
            resolution=args.resolution
        )
        print(f"Fractal image saved to {args.output}")

if __name__ == "__main__":
    main()
