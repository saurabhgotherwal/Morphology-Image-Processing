# Morphology-Image-Processing
This program implements various morphology image processing tasks like removing noise from the image and extracting boundaries.

## Objective:

1. To remove the noise from the given image using two morphology image processing
algorithms.
2. To extract the boundary using morphology image processing algorithm.

## Approach:

### Denoising:
To remove the noise, we are using the following two algorithms:
1. Opening followed by closing
2. Closing followed by opening

The basic idea of the approach is that noise pixels outside the object area are removed by opening
with the structuring element while noise pixels inside the object area are removed by closing with the
structuring element.

For denoising I am using a 3X3 square structuring element with the origin at the centre.

### Boundary Extraction:
For extracting the boundary, we are first eroding the image and subtracting the result from the original
image.
