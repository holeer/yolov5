import os, random, shutil
  
  path = input("C:/Users/Lenovo/Desktop/Mark/images")
  new_path = input("C:/Users/Lenovo/Desktop/Mark/")
  
  for root, dirs, files in os.walk(path):
      fileNumber = len(files)
      rate = 0.2
     pickNumber = int(rate * fileNumber)
     sample = random.sample(files, pickNumber)
     for name in sample:
 
         file_path = root + '/' + name
         new_file_path = new_path + '/' + name
         shutil.move(file_path, new_file_path)