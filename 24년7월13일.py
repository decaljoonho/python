##def read_file(file_name) :
##    f = open(file_name, "r")
##    lines = f.readlines()
##    for line in lines :
##        print(line.strip())
##    f.close()
##    
##def write_file(file_name , mode) :
##    f = open(file_name, mode)
##    print("Input(Enter 'q' to exit input) :")
##    while True :
##        data = input()
##        if data == "q" :
##            break
##        f.write(data + "\n")
##    f.close()
##    
##
##
##file_name = input("File name : ")
##mode = input("File mode(r/w/a) : ")
##
##if mode == "r" :
##    read_file(file_name)
##else :
##    write_file(file_name, mode)
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##from PIL import Image
##
##area = (230, 155, 1110, 770)
##size = (640,200)
##
##lion_img = Image.open("Lion.jpg")
##fruit_img = Image.open("fruit.png")
##
##print(lion_img.size, lion_img.format, lion_img.mode)
##print(fruit_img.size, fruit_img.format, fruit_img.mode)
##
##fruit_resz = fruit_img.resize(size)
##lion_cropped = lion_img.crop(area)
##fruit_img.show()
##
##lion_cropped.save("lion_cropped.jpg")
##fruit_resz.save("fruit_resized.png")
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##from PIL import Image
##
##size = (128, 128)
##
##lion_img = Image.open("Lion.jpg")
##lion_rotated = lion_img.rotate(90)
##lion_converted = lion_img.convert('L')
##lion_transpose = lion_img.transpose(Image.FLIP_LEFT_RIGHT)
##lion_img.thumbnail(size)
##
##print("lion_converted.mode =", lion_converted.mode)
##print("lion_img.size =", lion_img.size)
##
##lion_converted.show()
##lion_transpose.show()
##lion_rotated.save("lion_rotated.jpg")
##lion_img.save("lion_thumb.jpg")
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##from PIL import Image
##size = (128, 128)
##
##fruit_img = Image.open("fruit.png")
##fruit_rotated = fruit_img.rotate(270)
##fruit_converted = fruit_img.convert('L')
##fruit_rotated.show()
##fruit_converted.show()
##fruit_rotated.save("fruit_rotated.png")
##fruit_converted.save("fruit_converted.png")
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
##from PIL import Image
##from PIL import ImageDraw
##
##canvas_size = (200, 200)
##rect_area = [(0,0), (100,100)]
##line_cor = [(0,200), (200, 0)]
##circle_area = [(100, 100), (200, 200)]
##
##new_img = Image.new("RGB", canvas_size, "orange")
##draw_imgs = ImageDraw.Draw(new_img)
##draw_imgs.rectangle(rect_area, fill = "red", outline = "yellow")
##draw_imgs.line(line_cor, fill = "blue", width = 4)
##draw_imgs.ellipse(circle_area, fill = "green", outline = "red")
##
##new_img.show()
##new_img.save("Imagedraw.jpg")
##ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

lion_img = Image.open("Lion.jpg")
c3coding_img = Image.open("c3coding_rt.jpg")
c3coding_img.thumbnail((120, 120))
draw = ImageDraw.Draw(lion_img)

stx, sty = (150, 285)
c3x, c3y = c3coding_img.size
msg1 = "The               is"
msg2 = "the best!"

##mfont = ImageFont.truetype(40)
##m2font = ImageFont.truetype(52)
draw.text((70,280), msg1, (255, 255, 0 ))
draw.text((70,330), msg2, (255, 0, 0 ))
lion_img.paste(c3coding_img, (stx, sty, stx+c3x, sty+c3y))

lion_img.show()
lion_img.save("c3lion.jpg")
