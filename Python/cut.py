from PIL import Image
import os

# 定义待批量裁剪的图像地址
IMAGE_INPUT_PATH = 'E:\沈彬\工程相册\相\原图'
# 定义裁剪后的图像存放地址
IMAGE_OUTPUT_PATH = 'E:\沈彬\工程相册\相\裁剪'

w = 16
h = 9

for each_image in os.listdir(IMAGE_INPUT_PATH):
    # 定义左，上，右和下像素坐标
    BOX_LEFT, BOX_UP, BOX_RIGHT, BOX_DOWN = 0,0,0,0
    # 每个图像全路径
    image_input_fullname = IMAGE_INPUT_PATH + '/' + each_image
    # PIL库打开每一张图
    img = Image.open(image_input_fullname)

    #判断和计算图片大小
    ih = img.height
    iw = img.width
    if ih/iw>h/w:
        BOX_UP = (ih-iw*h/w)/2
        BOX_RIGHT = iw        
        BOX_DOWN = iw*h/w+BOX_UP
    else:
        BOX_LEFT = (iw-ih*w/h)/2
        BOX_RIGHT = ih*w/h+BOX_LEFT
        BOX_DOWN = ih
    print(ih,iw)
    print(BOX_LEFT, BOX_UP, BOX_RIGHT, BOX_DOWN)
    # 从此图像返回一个矩形区域。 盒子是一个4元组定义左，上，右和下像素坐标。
    box = (BOX_LEFT, BOX_UP, BOX_RIGHT, BOX_DOWN)
    # 进行ROI裁剪
    roi_area = img.crop(box)
    # 裁剪后每个图像全路径
    image_output_fullname = IMAGE_OUTPUT_PATH + '/' + each_image
    # 保存处理后的图像
    roi_area.save(image_output_fullname)
    print('{0} crop Done.'.format(each_image))
