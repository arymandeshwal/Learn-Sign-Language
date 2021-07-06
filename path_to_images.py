from pathlib import Path
import os
import cv2

def get_path_image(filename):
  
  paths=[]


  base_path=Path(os.getcwd())
  #print(os.listdir(base_path))

  img_path=base_path / filename
  #print(os.listdir(img_path))

  for i in os.listdir(img_path):
    img=os.path.join(img_path,i)
    paths.append(img)
  return paths

##print(get_path_image("resized_colored_small"))
##print(get_path_image("resized_shadow_images"))

