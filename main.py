from PIL import Image

def create_gif(image_paths, output_gif_path, duration=500):
 images = [Image.open(image_path) for image_path in image_paths]
# Save as GIF
 images[0].save(
 output_gif_path,
 save_all=True,
 append_images=images[1:],
 duration=duration,
 loop=0 # 0 means infinite loop
 )

if __name__ == "__main__":
 # List of image file paths
 image_paths = ["team-pic1.png", "team-pic2.png"] # Add your file paths
# Output GIF path
 output_gif_path = "output.gif"
# Create GIF
 create_gif(image_paths, output_gif_path)

print(f"GIF created and saved at {output_gif_path}")

#images are taken from here https://www.codedex.io/projects/create-a-gif-with-python
#codes are taken from here https://medium.com/@theriyasharma24/creating-gifs-from-images-using-python-88946aa47881