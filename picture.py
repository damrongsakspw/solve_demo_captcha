from PIL import Image, ImageDraw, ImageFilter
import requests
from io import BytesIO
import matplotlib.pyplot as plt
# URL ของรูปภาพ
inner_image_url = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/cb6f9526f9594194a09df643881cd0e8~tplv-b4yrtqhy5a-2.jpeg"
outer_image_url = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/8482448d6eeb4977abf869568b33a1e3~tplv-b4yrtqhy5a-2.jpeg"


# ดาวน์โหลดรูปภาพ
response = requests.get(inner_image_url)
inner_image = Image.open(BytesIO(response.content))

response_main = requests.get(outer_image_url)
outer_image = Image.open(BytesIO(response_main.content))

# สร้างภาพวงกลม
mask = Image.new("L", inner_image.size, 0)
draw = ImageDraw.Draw(mask)
width_in, height_in = inner_image.size
# draw.ellipse((0, 0, inner_image.size[0], inner_image.size[1]), fill=255)
draw.ellipse((2, 2, width_in-2, height_in-2), fill=255)
inner_circle = Image.new('RGBA', inner_image.size, (255, 255, 255, 0))
inner_circle.paste(inner_image, mask=mask)

mask2 = Image.new("L", outer_image.size, 0)
draw = ImageDraw.Draw(mask2)
draw.ellipse((0, 0, outer_image.size[0], outer_image.size[1]), fill=255)

# ตัดขอบสีขาวออก
inner_circle = Image.new("RGBA", inner_image.size, (255, 255, 255, 0))
inner_circle.paste(inner_image, mask=mask)

outer_circle = Image.new("RGBA", outer_image.size, (255, 255, 255, 0))
outer_circle.paste(outer_image, mask=mask2)

inner_circle.show()
# ใช้ Gaussian Blur เพื่อจัดขอบให้ smooth ขึ้น
smoothed_inner_circle = inner_circle.filter(ImageFilter.GaussianBlur(radius=0.7))

# เพิ่มความชัดของ inner_circle และ outer_circle
# sharpened_inner_circle = smoothed_inner_circle.filter(ImageFilter.SHARPEN(radius=2.0))
# sharpened_outer_circle = outer_circle.filter(ImageFilter.SHARPEN(radius=2.0))


# แสดงรูปภาพ
plt.imshow(smoothed_inner_circle)
plt.axis('off')  # ปิดการแสดงเส้นขอบแกน
plt.show()

# Setup matplotlib
fig, ax = plt.subplots()
image_display = ax.imshow(outer_image)
plt.ion()  # Turn on interactive mode
plt.show()

angle = 0
scale_factor = 5
# scale_factor = 1.2
# Function to convert a PIL image to grayscale
def pil_to_grayscale(image):
    return image.convert("L")

new_size = (int(inner_circle.width +    scale_factor), int(inner_circle.height + scale_factor))
resized_inner_circle = inner_circle.resize(new_size, Image.LANCZOS)  # ใช้ Image.LANCZOS เพื่อปรับขนาดอย่างเสถีย
while angle <180:
# for angle in range(-180, 180, 1):
# กำหนดขนาดใหม่ของวงกลมภายใน
    # new_size = (int(inner_circle.width * scale_factor), int(inner_circle.height * scale_factor))
    # resized_inner_circle = inner_circle.resize(new_size, Image.LANCZOS)  # ใช้ Image.LANCZOS เพื่อปรับขนาดอย่างเสถีย

    rotated_inner_circle = inner_circle.rotate(-angle)
    rotated_outer_circle = outer_circle.rotate(angle)
    # คำนวณตำแหน่งที่จะนำวงกลมที่ได้มาวางบนรูปภาพหลัก
    position = ((rotated_outer_circle.width - rotated_inner_circle.width) // 2, (rotated_outer_circle.height - rotated_inner_circle.height) // 2)

    # นำวงกลมมาวางบนรูปภาพหลัก
    rotated_outer_circle.paste(rotated_inner_circle, position, rotated_inner_circle)

    # แปลงรูปภาพที่รวมกันแล้วเป็นระดับสีเทา (grayscale)
    # grayscale_combined = pil_to_grayscale(rotated_outer_circle)

    # position = ((rotated_outer_circle.width - rotated_inner_circle.width) // 2, (rotated_outer_circle.height - rotated_inner_circle.height) // 2)


    # แสดงภาพหลังจากทำการวางวงกลม
    # rotated_outer_circle.show()
    # Update the displayed image
    plt.title(f'Circle Rotated by {angle} Degrees')
    image_display.set_data(rotated_outer_circle)
    plt.axis('off')  # ปิดการแสดงเส้นขอบแกน
    plt.draw()
    plt.pause(0.5)  # Pause to allow the image to update

    angle += 1