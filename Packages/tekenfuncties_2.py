import numpy as np
import matplotlib.pyplot as plt


def vertaal_letter_in_kleur (letter) :
    """
    translate a an input letter to an RGB channel 
    """
    letter_naar_channel = {
        'R': 0,
        'G': 1,
        'B': 2,
        'r': 0,
        'g': 1,
        'b': 2
    }

    return letter_naar_channel[letter]

def show_image (image) : 
    plt.imshow(image)
    plt.show()
    return 


def bilinear_interpolation(image, y, x):
    """
    Perform bilinear interpolation for a given point (y, x) in the image.
    = calculate the average value depending on the values 'around' the point y,x
    """
    # Get the dimensions of the image
    height, width = image.shape[:2]
    
    # Compute the integer coordinates surrounding the point
    y1, x1 = int(np.floor(y)), int(np.floor(x))
    y2, x2 = min(y1 + 1, height - 1), min(x1 + 1, width - 1)  #stay in the image
    
    # Calculate the fractional part of the coordinates
    dy, dx = y - y1, x - x1
    
    # Perform bilinear interpolation
    interpolated_value = (1 - dx) * (1 - dy) * image[y1, x1] + \
                         dx * (1 - dy) * image[y1, x2] + \
                         (1 - dx) * dy * image[y2, x1] + \
                         dx * dy * image[y2, x2]
    
    return interpolated_value


def verkleur (image, KLEUR) : 
    """
    returns the image with the KLEUR channel set to the maximum
    image = the image to verkleur, KLEUR = a letter reprenting the channel
    """

    np_image_temp = image.copy()
    channel = np_image_temp[:, :, vertaal_letter_in_kleur(KLEUR)] #(points to the right RGB channel)
    channel[:] = 255  # Modify the channel values : set to the maximum

    return np_image_temp


def resize_image(image, new_width, new_height):
    """
    Resizes an image using simple pixel reducing algorithm (no smoothing out) 
        image: A NumPy array representing the image (RGB format).
        new_width: The desired new width of the image.
        new_height: The desired new height of the image.
    """

    # Calculate scaling factors
    width_ratio = new_width / image.shape[1]
    height_ratio = new_height / image.shape[0]

    resized_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    # Iterate over new image pixels and map coordinates to original image
    for y in range(new_height):
        for x in range(new_width):
            # Calculate corresponding coordinates in original image and take that pixel value
            original_x = int(np.floor(x / width_ratio))
            original_y = int(np.floor(y / height_ratio))
            # Check if coordinates are within image bounds
            if 0 <= original_x < image.shape[1] and 0 <= original_y < image.shape[0]:
                resized_image[y, x] = image[original_y, original_x]
    return resized_image

def zoom_image (original_image, zoom_point, zoom_factor):
    """
    returns an image of the same size, zoomed by a factor zoom_factor, centered arount the zoom_point
    (no smoothing out)
    """
    zoomed_image = np.zeros_like(original_image)

    #for every pixel in the new image, search the corresponding point in the original image
    #if over the edge of the image, leave the edge black 
    for y in range(original_image.shape[0]) : 
           for x in range (original_image.shape[1]) :
                overeenkomstige_y = int(round(zoom_point[0] - (original_image.shape[0]/2 - y) / zoom_factor))
                overeenkomstige_x = int(round(zoom_point[1] - (original_image.shape[1]/2 - x) / zoom_factor))
                if (0 <= overeenkomstige_y < original_image.shape[0]) and (0 <= overeenkomstige_x < original_image.shape[1]) :
                    #zoomed_image[y,x] = original_image[overeenkomstige_y, overeenkomstige_x]
                    zoomed_image[y,x] = bilinear_interpolation(original_image, overeenkomstige_y, overeenkomstige_x)
    return zoomed_image 


def flip_image (image, direction) :
    """
            - 0 for image not flipped, 
            - 1 for flipping your image left right, 
            - 2 for flipping it upside down 
            - 3 for flipping it both left right and upside down
    """
    
    #alternative solution is to use the rotator, but this is more efficient since every pixel 'falls' onto another one

    tmp_image = image.copy()
    if direction == 0 :
        return tmp_image 
    elif direction == 1 :
        return np.fliplr(tmp_image)
    elif direction == 2 : 
        return tmp_image[::-1, :]
    elif direction == 3 : 
        return np.fliplr(tmp_image)[::-1, :]
    
    

def grid_with_flips(image, matrix): 
    """
        image (image to be processed)
        matrix : matrix containing the type of flips that you do with your image. 
            - 0 for you image not flipped, 
            - 1 for flipping your image left right, 
            - 2 for flipping it upside down 
            - 3 for flipping it both left right and upside down
    """
    
    np_matrix = np.array(matrix)

    output_height = image.shape[0] * np_matrix.shape[0]
    output_width = image.shape[1] * np_matrix.shape[1]
    output_image = np.ones((output_height, output_width,3), dtype=np.uint8)

    for k in range (np_matrix.shape[0]):
        x_pos_start = k* image.shape[0]
        x_pos_end = (k+1)*image.shape[0]  
        for i in range (np_matrix.shape[1]) :
            y_pos_start = i* image.shape[1]
            y_pos_end =  (i+1)* image.shape[1]
            output_image[x_pos_start:x_pos_end, y_pos_start:y_pos_end] = flip_image(image, matrix[k][i])

    return output_image



def create_colorful_big_one(image, colors):
    """
        returns an image that consists of a big resized one in the middle and normalsized coloured versions of the image around  
        it only works when the input is consistent with a square
        image: the image to manipulate 
        colors: a list of colors ('r', 'g', 'b', to indicate in which colors the normalsized images must come) 
    """

    tmp_image = image.copy()
    if len(colors) % 4 != 0 :
        print("niet het juiste aantal kleintjes")
        return tmp_image
    
    vierkant_zijde = int(len(colors) / 4) + 1
    output_height = round(image.shape[0] * (len(colors) / 4 + 1))
    output_width = round(image.shape[1] * (len(colors) / 4 + 1))

    #create the output canvas at once, then we paste the different elements on the canvas, instead of creating a new image every time
    output_image = np.ones((output_height, output_width,3), dtype=np.uint8)
    
    #midden bovenstuk maken 
    for i in range (vierkant_zijde - 2) :
        output_image[0:image.shape[0], image.shape[1]*(i+1):image.shape[1]*(i+2)] = verkleur(tmp_image, colors[i+1])

    #big one eronder plakken, vergroten met een factor 'vierkant_zijde - 2' 
    vergrootf = vierkant_zijde - 2
    output_image[image.shape[0]: image.shape[0] * (vergrootf+1), image.shape[1] : image.shape[1] * (vergrootf + 1) ] = \
                 resize_image(tmp_image, tmp_image.shape[1]*vergrootf, tmp_image.shape[0]*vergrootf)
    
    #onderste rij eronder plakken 
    for i in range (vierkant_zijde - 2) :
        output_image[image.shape[0]*(vierkant_zijde-1) : image.shape[0]*(vierkant_zijde),
                     image.shape[1]*(i+1):image.shape[1]*(i+2)] = verkleur(tmp_image, colors[3* (vierkant_zijde -1)-1-i])

    #rechterband ernaast plakken
    for i in range (vierkant_zijde) :
        output_image[image.shape[0]*i:image.shape[0]*(i+1),image.shape[1]*(vierkant_zijde-1):image.shape[1]*(vierkant_zijde)] = \
                    verkleur(tmp_image, colors[vierkant_zijde+i-1])

    #linkerband ernaast plakken
    for i in range (vierkant_zijde) :
        output_image[image.shape[0]*i:image.shape[0]*(i+1),0:image.shape[1]] = \
            verkleur(tmp_image, colors[(len(colors)-i) % len(colors)])
        
    return output_image

    

def rotate_image(image, angle):
    """
    Rotate the input image by the specified angle (in degrees).
    """
    # Convert angle to radians
    angle_rad = np.radians(angle)
    
    # Get image dimensions
    height, width = image.shape[:2]
    
    # Calculate the center of the image
    center_y = height / 2
    center_x = width / 2
    
    # Compute the rotation matrix
    rotation_matrix = np.array([[np.cos(angle_rad), -np.sin(angle_rad)],
                                [np.sin(angle_rad), np.cos(angle_rad)]])
    
    # Create output image array
    rotated_image = np.zeros_like(image)
    
    # Iterate over each pixel in the rotated image
    for y in range(height):
        for x in range(width):
            # Apply the inverse rotation to get the corresponding pixel in the original image
            rotated_y, rotated_x = np.dot(rotation_matrix, [y - center_y, x - center_x]) + [center_y, center_x]
            
            # Perform bilinear interpolation to get the pixel value
            if 0 <= rotated_y < height - 1 and 0 <= rotated_x < width - 1:
                rotated_image[y, x] = bilinear_interpolation(image, rotated_y, rotated_x)
    
    return rotated_image
