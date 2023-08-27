#The following code is used to Convert your Images into JPEG Images with your Customized Sizes in a fraction of Seconds
import cv2
import os
input_directory = 'D://VU//EthirNeechal//CV//CNN//amx//sa'
output_directory = 'D://VU//EthirNeechal//CV//CNN//amx//ya'
os.makedirs(output_directory, exist_ok=True)
def resize_images(input_dir, output_dir, target_size):
    # Get a list of all files in the input directory
    image_files = os.listdir(input_dir)
    
    # Initialize a counter for sequential labeling
    label_counter = 0
    
    # Loop through each image file
    for image_file in image_files:
        # Construct the full path to the input image
        input_path = os.path.join(input_dir, image_file)
        
        # Read the image using OpenCV
        image = cv2.imread(input_path)
        
        if image is not None:
            # Resize the image to the target size (100x100 pixels)
            resized_image = cv2.resize(image, target_size)
            
            # Construct the full path to the output image with sequential label
            output_path = os.path.join(output_dir, f'image{label_counter+11}.jpg')
            
            # Save the resized image
            cv2.imwrite(output_path, resized_image)
            
            # Increment the label counter
            label_counter += 1

# Define the target size for resizing (100x100 pixels)
target_size = (100, 100)

# Call the function to resize and save images
resize_images(input_directory, output_directory, target_size)
