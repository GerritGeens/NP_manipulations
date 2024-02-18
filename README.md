<!-- ABOUT THE PROJECT -->

## About The Project

- This is a quoted assignment for Syntra's 1st year data scientist evening course

- The project is about   
  
  - handling images using only numpy arrays  
  
  - documenting and setting up a git repository and an environment in which to run the code
  
  - The following functions are used and documented in the 'tekenfuncties2' package
    
    - verkleur (changes the color of a picture)
    - grid with flips (makes a grid with certain versions of the original image)
    - create_colorful_big_one (makes a grid with certain colored versions of the original image)
    - zoom_image (zooms)
    - rotate_image (rotates the image over an angle)
  
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

## Note

You can try different pictures, the best result is with pictures with a smooth background (eg white), that is not repeated (much) in the picture itself

## Contact

Zoef De Haas -  geens.gerrit@gmail.com
