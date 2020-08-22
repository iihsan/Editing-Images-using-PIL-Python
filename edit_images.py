from pil import Image       # pil module is used to edit images
import os                   # os module is used to read and write to files and also to read directories

source = r'images/'         # source path of raw images
destination = r'output/'     # destination path of converted images

dirs = os.listdir(source)       # read all directories from the source path

def edit():        # function to edit images
    count =0
    for item in dirs:       # traversing through all directories

        percentage = (count/len(dirs))*100  # just to show percentage of conversion
        print("Editing images ==> "+ str(percentage) + '%') 
        count+=1

        if os.path.isfile(source+item):         # check if directories are files or not, ignore if not files
            img = Image.open(source+item)        # loading images
            file_path, splited_text = os.path.splitext(source+item)         # file_path,splited_text are used to store splitted text, file_path contains full path of images while splited_text will be empty

            file_name = file_path.split('/')[-1]                # spliting the name of file from full path

            img_resize = img.resize((128,128), Image.ANTIALIAS)         # resizing images from 192x192 to 128x128
            img_rotate = img_resize.rotate(90)          # rotating images to 90 degree clock_wise

            if img_rotate.mode != 'RGB':            # converting images to RGB's to save without error
                img_rotate = img_rotate.convert('RGB')

            img_rotate.save(destination + file_name + '.jpeg', 'JPEG', quality=90)          # saving edited images to destination path


if __name__=="__main__":        # main function
    print('Starting....')
    edit()           #calling the edit function to make changes to images
    print('Images edited successfully')