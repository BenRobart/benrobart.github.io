import os
from PIL import Image

def crop_top_pixels(input_folder, pixels_to_remove=52):
    # Create an output directory so we don't overwrite originals
    output_folder = os.path.join(input_folder, "cropped_images")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Supported file extensions
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(valid_extensions):
            img_path = os.path.join(input_folder, filename)
            
            with Image.open(img_path) as img:
                width, height = img.size
                
                # Define the box: (left, upper, right, lower)
                # We start 'upper' at 90 instead of 0
                if height > pixels_to_remove:
                    crop_box = (0, pixels_to_remove, width, height)
                    cropped_img = img.crop(crop_box)
                    
                    # Save the result
                    save_path = os.path.join(output_folder, filename)
                    cropped_img.save(save_path)
                    print(f"Processed: {filename}")
                else:
                    print(f"Skipped {filename}: Image height is less than {pixels_to_remove}px")

# Usage
if __name__ == "__main__":
    # Replace with your folder path
    target_folder = "./crop" 
    crop_top_pixels(target_folder)