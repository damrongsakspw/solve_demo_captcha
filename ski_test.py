from PIL import Image, ImageDraw, ImageFilter, ImageOps
import requests
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage import feature, measure



# URL ของรูปภาพ
inner_image_url = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/d24db9bda52f43f2831a487dfc85a10c~tplv-b4yrtqhy5a-2.jpeg"
outer_image_url = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/519d529aad1c4152a26612fe2b4381af~tplv-b4yrtqhy5a-2.jpeg"
# ดาวน์โหลดรูปภาพ
response = requests.get(inner_image_url)
inner_image = Image.open(BytesIO(response.content))

response_main = requests.get(outer_image_url)
outer_image = Image.open(BytesIO(response_main.content))

# สร้างภาพวงกลม
mask = Image.new("L", inner_image.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((2, 2, inner_image.width - 2, inner_image.height - 2), fill=255)
inner_circle = Image.new('RGBA', inner_image.size, (255, 255, 255, 0))
inner_circle.paste(inner_image, mask=mask)

mask2 = Image.new("L", outer_image.size, 0)
draw = ImageDraw.Draw(mask2)
draw.ellipse((0, 0, outer_image.width, outer_image.height), fill=255)
outer_circle = Image.new("RGBA", outer_image.size, (255, 255, 255, 0))
outer_circle.paste(outer_image, mask=mask2)

# แปลงเป็น numpy array ก่อนใช้งานกับ skimage.feature.canny
inner_np = np.array(inner_circle.convert("L"))  # แปลงเป็น grayscale ก่อน
outer_np = np.array(outer_circle.convert("L"))  # แปลงเป็น grayscale ก่อน
def pil_to_grayscale(image):
    return image.convert("L")

# edges_inner = feature.canny(inner_np, sigma=3)
# edges_outer = feature.canny(outer_np, sigma=3)

# # Setup matplotlib
# fig, ax = plt.subplots()
# # image_display = ax.imshow(outer_image)
# image_display = ax.imshow(np.array(outer_circle.convert("RGBA")))
# plt.ion()  # Turn on interactive mode
# plt.show()

# Setup matplotlib
fig, ax = plt.subplots()
image_display = ax.imshow(np.array(outer_circle.convert("RGBA")), cmap='gray')
plt.ion()  # เปิดโหมดแสดงผลแบบอินเทอร์แอคทีฟ
plt.show()
# Function to calculate standard deviation of edges
def calculate_edge_smoothness(edges):
    return np.std(edges)

best_angle = 0
best_smoothness = float('inf')
best_color_similarity = 0
angle = 2
arr_smooth= []

angle = 90
while angle < 96:
# for angle in range(-180, 180, 1):
# กำหนดขนาดใหม่ของวงกลมภายใน
    # new_size = (int(inner_circle.width * scale_factor), int(inner_circle.height * scale_factor))
    # resized_inner_circle = inner_circle.resize(new_size, Image.LANCZOS)  # ใช้ Image.LANCZOS เพื่อปรับขนาดอย่างเสถีย

    rotated_inner_circle = inner_circle.rotate(-angle)
    rotated_outer_circle = outer_circle.rotate(angle)

    # # แปลงเป็น numpy array ก่อนใช้งานกับ skimage.feature.canny
    # inner_np = np.array(rotated_inner_circle.convert("L"))  # แปลงเป็น grayscale ก่อน
    # outer_np = np.array(rotated_outer_circle.convert("L"))  # แปลงเป็น grayscale ก่อน
    # edges_inner = feature.canny(inner_np, sigma=3)
    # edges_outer = feature.canny(outer_np, sigma=3)

 
    # คำนวณตำแหน่งที่จะนำวงกลมที่ได้มาวางบนรูปภาพหลัก
    position = ((rotated_outer_circle.width - rotated_inner_circle.width) // 2, (rotated_outer_circle.height - rotated_inner_circle.height) // 2)

    # นำวงกลมมาวางบนรูปภาพหลัก
    rotated_outer_circle.paste(rotated_inner_circle, position, rotated_inner_circle)

    # # แปลงรูปภาพที่รวมกันแล้วเป็นระดับสีเทา (grayscale)
    # grayscale_combined =  np.array(rotated_outer_circle.convert("L")) 
    outer_np = np.array(rotated_outer_circle.convert("L"))  # แปลงเป็น grayscale ก่อน
    outer_np = feature.canny(outer_np, sigma=2)

  

    # Analyze edge continuity
    # Label connected components
    labels = measure.label(outer_np)

    # Measure properties of labeled image regions
    props = measure.regionprops(labels)

    # Calculate the length of each edge
    edge_lengths = [prop.perimeter for prop in props]

    # # Display edge lengths
    # print("Edge lengths:", edge_lengths)
    # print("Average edge length:", np.mean(edge_lengths))
    # print("Longest edge length:", np.max(edge_lengths))


    # Calculate edge smoothness
    smoothness = calculate_edge_smoothness(outer_np)
    arr_smooth.append([angle, smoothness,np.mean(edge_lengths), np.max(edge_lengths)])

    if smoothness < best_smoothness :
        best_smoothness = smoothness
        best_angle = angle
    



#    # display results
#     fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(8, 3))
#     ax[0].imshow(outer_np, cmap='gray')
#     ax[0].set_title('canny filter image $\sigma=3$', fontsize=20)

#     for a in ax:
#         a.axis('off')

#     fig.tight_layout()
#     plt.show()

    #     # ใช้ Canny edge detection เพื่อตรวจจับขอบ
    # edges_inner = feature.canny(grayscale_combined, sigma=3)
    # # edges_outer = feature.canny(outer_np, sigma=3)

    # # position = ((rotated_outer_circle.width - rotated_inner_circle.width) // 2, (rotated_outer_circle.height - rotated_inner_circle.height) // 2)


    # แสดงภาพหลังจากทำการวางวงกลม
    # rotated_outer_circle.show()
    # Update the displayed image
    plt.title(f'Circle Rotated by {angle} Degrees')
    image_display = ax.imshow(np.array(outer_np), cmap='gray')
    image_display.set_data(outer_np)
    plt.axis('off')  # ปิดการแสดงเส้นขอบแกน
    plt.draw()
    plt.pause(0.5)  # Pause to allow the image to update
    # plt.pause(500)  # Pause to allow the image to update
    if angle == 100:
        angle = 90
    angle += 0.5

degree_arr = np.array(arr_smooth)


# Find the index where the smoothness is minimized and color similarity is maximized
best_smooth = np.argmin(degree_arr[:, 1])

# Print the results for the best angle
print(f"Best Angle: {degree_arr[best_smooth, 0]} degrees")
print(f"Best Edge Smoothness: {degree_arr[best_smooth, 1]}")
print(f"Average edge length: {degree_arr[best_smooth, 2]}")
print(f"Longest edge length: {degree_arr[best_smooth, 3]}")

# print(f"The best angle for the circles to align is: {best_angle} degrees with edge smoothness: {best_smoothness}")

# Sort the results and print the top 5 angles
sorted_indices = np.argsort(degree_arr[:, 1])  # Sort indices by edge smoothness

arr_long = []
for i in range(5):   
    index = sorted_indices[i]
    angle = degree_arr[index, 0]  # Angle
    value = degree_arr[index, 1]  # Edge smoothness
    avg_edge  = degree_arr[index, 2]  # Average edge
    long_edge  = degree_arr[index, 3]  # Longest edge length
    print(f"Rank {i+1}: Angle {angle} degrees, Edge Smoothness {value},Average edge length: {avg_edge},Longest edge length: {long_edge}")
    if angle != 90.0:
        arr_long.append([angle,value,avg_edge,long_edge])

degree_best = np.array(arr_long)
# Find the index where the smoothness is minimized and color similarity is maximized
best_long = np.argmax(degree_best[:, 3])
# Print the results for the best angle
print(f"Best Angle: {degree_best[best_long, 0]} degrees")
print(f"Best Edge Smoothness: {degree_best[best_long, 1]}")
print(f"Average edge length: {degree_best[best_long, 2]}")
print(f"Longest edge length: {degree_best[best_long, 3]}")


b_angle = degree_best[best_long, 0]
print(b_angle)
rotated_inner_circle = inner_circle.rotate(-91.5)
rotated_outer_circle = outer_circle.rotate(91.5)
 
# คำนวณตำแหน่งที่จะนำวงกลมที่ได้มาวางบนรูปภาพหลัก
position = ((rotated_outer_circle.width - rotated_inner_circle.width) // 2, (rotated_outer_circle.height - rotated_inner_circle.height) // 2)

# นำวงกลมมาวางบนรูปภาพหลัก
rotated_outer_circle.paste(rotated_inner_circle, position, rotated_inner_circle)
# # แสดงภาพหลังจากทำการวางวงกลม
# rotated_outer_circle.show()
# Update the displayed image
plt.title(f'Circle Rotated by {b_angle} Degrees')
# image_display = ax.imshow(np.array(outer_np))
image_display.set_data(rotated_outer_circle)
plt.axis('off')  # ปิดการแสดงเส้นขอบแกน
plt.draw()
# plt.pause(0.5)  # Pause to allow the image to update
plt.pause(500)  # Pause to allow the image to update
