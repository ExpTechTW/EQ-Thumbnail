from PIL import Image, ImageDraw, ImageFont

image_path = input("底圖檔案名稱: ")
text = input("震央位置: ")
max = input("最大震度(0~9): ")
loc = input("本地震度(0~9): ")

image = Image.open(image_path).point(lambda p: p * 0.4)

overlay_max = Image.open('./resource/{}.png'.format(max)).resize((150, 150))
overlay_loc = Image.open('./resource/{}.png'.format(loc)).resize((150, 150))

draw = ImageDraw.Draw(image)

font = ImageFont.truetype("font.ttf", 150)

(width, height), (ox, oy) = font.font.getsize(text)

image_width, image_height = image.size
x = (image_width - width) / 2
y = image_height - height - 50

def d_text(text,x,y):
    text_color = (255, 255, 255)
    outline_color = (0, 0, 0)

    outline_positions = [
        (x - 5, y - 5),(x + 5, y - 5),
        (x - 5, y + 5),(x + 5, y + 5),
        (x - 5, y),(x + 5, y),
        (x, y - 5),(x, y + 5),
    ]

    for outline_position in outline_positions:
        draw.text(outline_position, text, fill=outline_color, font=font)
    draw.text((x, y), text, fill=text_color, font=font)

d_text(text,x,y)
d_text("最大震度",550,300)
d_text("本地震度",550,550)

image.paste(overlay_max, (1200, 305), overlay_max)
image.paste(overlay_loc, (1200, 555), overlay_loc)

output_path = 'output.jpg'
image.save(output_path)

image.show()
