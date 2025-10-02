import cv2
import pandas as pd
import sys 

# Get the input image path from command line arguments
INPUT_IMAGE = sys.argv[1]
IMAGE_NAME = INPUT_IMAGE[:INPUT_IMAGE.index(".")]
OUTPUT_IMAGE = IMAGE_NAME + "_tagged.jpg"
output_csv_file = sys.argv[2]
# Load the image and store into a variable
# -1 means load unchanged
image = cv2.imread(INPUT_IMAGE, -1)

def image_tagger( tag):
   
    #add the tag to the image
    font = cv2.FONT_HERSHEY_SIMPLEX

    color = (0,0,255) # color is red
    thickness = 2
    height, width, _ = image.shape
    x = int(width) //2
    y = 35
    org = (x, y)


      # Write text on the image
    cv2.putText(image, tag, org, font, 1, color, thickness)

    # Display the image with the tag
    cv2.imshow('Image with Tag', image)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
    #save the image
    
    
    cv2.imwrite(OUTPUT_IMAGE, image)
    print(f"Image saved as '{OUTPUT_IMAGE}'")
    


print("Welcome to the Custom Image Tagger\n")
tag = input("Enter the tag you want to add to the image and hit enter\n")
image_tagger(tag)

data = {'Image': [OUTPUT_IMAGE], 'Tag': [tag]}
# Create the Pandas DataFrame
df = pd.DataFrame(data)

# Export the dataframe to a csv file
df.to_csv('image_tags.csv', index=False)
print("Tag saved to 'image_tags.csv'")

