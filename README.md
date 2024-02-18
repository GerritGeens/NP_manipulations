<!-- ABOUT THE PROJECT -->

## About The Project

- This is a quoted assignment for Syntra's 1st year data scientist evening course

- The project is about   
  
  - handling images using only numpy arrays  
  
  - documenting and setting up a git repository and an environment in which to run the code
  
  - The following functions are used and documented in the 'tekenfuncties2' package
  
  - In the opdracht notebook you will find the function calls + the application on an example image
  
  - In the input directory you find some images for demonstration purposes 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

### Prerequisite

1. Anaconda navigator and powershell need to be installed

### Installation

1. Clone the repo

2. ```sh
   git clone https://github.com/GerritGeens/NP_manipulations.git
   ```

3. Open an anaconda powershell en go the root folder of this project 

4. Install and activate correct environment by running the following command from the root folder of the project in the anaconda powershell 
   
   ```sh
   conda env create --file haas.yml
   conda active ZoefDeHaas
   ```

5. Start jupyter notebook and open the code file `
   
   ```js
   jupyter notebook --notebook-dir %rootfolder%\code
   open the opdracht.ipynb notebook
   ```

## Different functions

**show_image** 

shows an image using matplotlib

- image: the image to show 

<br>

**verkleur (image, KLEUR)** 

changes the color of the image (not changing the background color)

- image: the image to change
- KLEUR: the color into which the image has to change (use "R" "G" "B")

<br>


**resize_image(image, new_width, new_height)**

returns a resized image

- image: the image to resize 
- new_width, new_heigth: the widht and heigt to change to 

<br>

**zoom_image (original_image, zoom_point, zoom_factor)**

returns a zoomed image 

- original_image: the image to resize 
- zoom_factor: number describing the zoom factor

<br>

**flip_image (image, direction)**

returns a flipped image 

- image: the image to resize 
- direction: an integer describing the orientation of the flip:
  - 0 for the image not flipped, 
  - 1 for flipping your image left right, 
  - 2 for flipping it upside down 
  - 3 for flipping it both left right and upside down

<br>

**create_colorful_big_one(image, colors)**

returns an image with different subimages (colored versions wrapped around a bigger centered one), described by 'colors'

- image: the basic image
- a list describing what the different colors should be, the size of the list must be a multiple of 4 

<br>


**rotate_image(image, angle)**

returns a rotated version of the image 

- image: the image to rotate
- angle: the rotation angles, in degrees where 90 is rotation to the right 







## Note

You can try different pictures, the best result is with pictures with a smooth background (eg white), that is not repeated (much) in the picture itself

## Contact

Zoef De Haas -  geens.gerrit@gmail.com
