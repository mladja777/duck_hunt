from PIL import Image
import os

 
def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    saved = 0
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    try:
        cropped_image.save(saved_location)
    except:
        os.remove(saved_location)
        cropped_image.save(saved_location)

 
if __name__ == '__main__':
    image = 'duck.png'
    '''for i in range(7):
        crop(image, (180, 360 + i*16, 196, 360 + i*16 + 16), 'dh' + str(i) + '0.bmp')
        crop(image, (196, 360 + i*16, 212, 360 + i*16 + 16), 'dh' + str(i) + '1.bmp')
        crop(image, (212, 360 + i*16, 228, 360 + i*16 + 16), 'dh' + str(i) + '2.bmp')'''
    '''crop(image, (170, 156, 186, 172), 'duck00.bmp')
    crop(image, (186, 156, 202, 172), 'duck01.bmp')
    crop(image, (170, 172, 186, 188), 'duck10.bmp')
    crop(image, (186, 172, 202, 188), 'duck11.bmp')'''
    crop(image, (0, 0, 16, 16), 'duck00.bmp')
    crop(image, (16, 0, 32, 16), 'duck01.bmp')
    crop(image, (0, 16, 16, 32), 'duck10.bmp')
    crop(image, (16, 16, 32, 32), 'duck11.bmp')

