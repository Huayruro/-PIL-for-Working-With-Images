from PIL import Image 

# use Pillow
# You need to have a sample image named "example.jpg", the program will create 3 new image files

im = Image.open("example.jpg")

new_im = im.resize((640,480))
new_im.save("example_resized.jpg")
 
new_im = im.rotate(90)
new_im.save("example_rotated.jpg")

im.rotate(180).resize((640,480)).save("flipped_and_resized.jpg")
