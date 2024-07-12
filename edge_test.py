# # from PIL import Image, ImageDraw
# # import requests
# # from io import BytesIO
# # import cv2
# # import numpy as np
# # from matplotlib import pyplot as plt

# # # Function to download an image from a URL
# # def download_image(url):
# #     response = requests.get(url)
# #     return Image.open(BytesIO(response.content))

# # # Function to convert a PIL image to OpenCV format
# # def pil_to_cv(image):
# #     return cv2.cvtColor(np.array(image), cv2.COLOR_RGBA2BGRA)

# # # URLs of the images
# # image_url = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/33d4c5833251402ba8f107504f983ad5~tplv-b4yrtqhy5a-2.jpeg"
# # main_image_url = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/0c6fd0772cc94c27ad60066eff434d14~tplv-b4yrtqhy5a-2.jpeg"

# # # Download images
# # inner_image = download_image(image_url)
# # outer_image = download_image(main_image_url)

# # # Create circular mask for inner image
# # mask = Image.new("L", inner_image.size, 0)
# # draw = ImageDraw.Draw(mask)
# # draw.ellipse((0, 0, inner_image.size[0], inner_image.size[1]), fill=255)

# # # Apply mask to inner image
# # inner_circle = Image.new("RGBA", inner_image.size, (255, 255, 255, 0))
# # inner_circle.paste(inner_image, mask=mask)

# # # Function to align and check if edges form a smooth picture
# # def align_and_check_edges(edges1, edges2):
# #     # Find contours in the edges
# #     contours1, _ = cv2.findContours(edges1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# #     contours2, _ = cv2.findContours(edges2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
# #     # Draw contours
# #     contoured_image1 = cv2.drawContours(np.zeros_like(edges1), contours1, -1, (255, 255, 255), thickness=cv2.FILLED)
# #     contoured_image2 = cv2.drawContours(np.zeros_like(edges2), contours2, -1, (255, 255, 255), thickness=cv2.FILLED)
    
# #     # Check for overlap by counting non-zero pixels in the AND operation
# #     overlap = cv2.bitwise_and(contoured_image1, contoured_image2)
# #     overlap_count = cv2.countNonZero(overlap)
    
# #     # If there's significant overlap, the edges are considered smooth
# #     return overlap_count > 0.8 * min(cv2.countNonZero(contoured_image1), cv2.countNonZero(contoured_image2))

# # # Convert outer image to grayscale and apply edge detection
# # outer_image_cv = pil_to_cv(outer_image)
# # gray_outer = cv2.cvtColor(outer_image_cv, cv2.COLOR_BGRA2GRAY)
# # edges_outer = cv2.Canny(gray_outer, 100, 200)

# # # Rotate the inner circle and check alignment
# # for angle in range(0, 180, 66):
# #     rotated_inner_circle = inner_circle.rotate(angle, expand=True)
    
# #     # Create a copy of the outer image to paste the rotated circle
# #     combined_image = outer_image.copy()
# #     position = ((outer_image.width - rotated_inner_circle.width) // 2, (outer_image.height - rotated_inner_circle.height) // 2)
# #     combined_image.paste(rotated_inner_circle, position, rotated_inner_circle)
    
# #     # Convert combined image to OpenCV format for processing
# #     combined_image_cv = pil_to_cv(combined_image)
    
# #     # Convert to grayscale
# #     gray_combined = cv2.cvtColor(combined_image_cv, cv2.COLOR_BGRA2GRAY)
    
# #     # Apply Canny edge detection
# #     edges_combined = cv2.Canny(gray_combined, 100, 200)
    
# #     # Display edges of the combined image
# #     plt.imshow(edges_combined, cmap='gray')
# #     plt.title(f'Edges with Inner Circle Rotated by {angle} Degrees')
# #     plt.xticks([]), plt.yticks([])
# #     plt.show()

# #     # Check if edges form a smooth picture
# #     is_smooth = align_and_check_edges(edges_combined, edges_outer)
# #     print(f"The edges form a smooth picture: {is_smooth}")

# #     # Optionally, you can also display the combined image
# #     # combined_image.show()


# from PIL import Image, ImageDraw, ImageFilter
# import requests
# import numpy as np
# from io import BytesIO
# import cv2
# import matplotlib.pyplot as plt
# # URL ของรูปภาพ
# inner_image_url = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/cb6f9526f9594194a09df643881cd0e8~tplv-b4yrtqhy5a-2.jpeg"
# outer_image_url = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/8482448d6eeb4977abf869568b33a1e3~tplv-b4yrtqhy5a-2.jpeg"


# # ดาวน์โหลดรูปภาพ
# response = requests.get(inner_image_url)
# inner_image = Image.open(BytesIO(response.content))

# response_main = requests.get(outer_image_url)
# outer_image = Image.open(BytesIO(response_main.content))

# # สร้างภาพวงกลม
# mask_inner = Image.new("L", inner_image.size, 0)
# draw_inner = ImageDraw.Draw(mask_inner)
# draw_inner.ellipse((0, 0, inner_image.size[0], inner_image.size[1]), fill=255)

# mask_outer  = Image.new("L", outer_image.size, 0)
# draw_outer = ImageDraw.Draw(mask_outer)
# draw_outer.ellipse((0, 0, outer_image.size[0], outer_image.size[1]), fill=255)

# # ตัดขอบสีขาวออก
# inner_circle = Image.new("RGBA", inner_image.size, (255, 255, 255, 0))
# inner_circle.paste(inner_image, mask=mask_inner)

# outer_circle = Image.new("RGBA", outer_image.size, (255, 255, 255, 0))
# outer_circle.paste(outer_image, mask=mask_outer)

# # ใช้ Gaussian Blur เพื่อจัดขอบให้ smooth ขึ้น
# smoothed_inner_circle = inner_circle.filter(ImageFilter.GaussianBlur(radius=0.7))

# # เพิ่มความชัดของ inner_circle และ outer_circle
# # sharpened_inner_circle = smoothed_inner_circle.filter(ImageFilter.SHARPEN(radius=2.0))
# # sharpened_outer_circle = outer_circle.filter(ImageFilter.SHARPEN(radius=2.0))


# # แสดงรูปภาพ
# # plt.imshow(smoothed_inner_circle)
# # plt.axis('off')  # ปิดการแสดงเส้นขอบแกน
# # plt.show()

# # Setup matplotlib
# fig, ax = plt.subplots()
# image_display = ax.imshow(outer_image)
# plt.ion()  # Turn on interactive mode
# plt.show()

# angle = 0
# # scale_factor = 1.2

# # Function to convert a PIL image to OpenCV format
# def pil_to_cv(image):
#     return cv2.cvtColor(np.array(image), cv2.COLOR_RGBA2BGRA)

# degree_arr = []
# while angle < 180:
# # for angle in range(-180, 180, 1):
# # กำหนดขนาดใหม่ของวงกลมภายใน
#     # new_size = (int(inner_circle.width * scale_factor), int(inner_circle.height * scale_factor))
#     # resized_inner_circle = inner_circle.resize(new_size, Image.LANCZOS)  # ใช้ Image.LANCZOS เพื่อปรับขนาดอย่างเสถีย

#     rotated_inner_circle = inner_circle.rotate(-angle)
#     rotated_outer_circle = outer_circle.rotate(angle)


#     # คำนวณตำแหน่งที่จะนำวงกลมที่ได้มาวางบนรูปภาพหลัก
#     position = ((rotated_outer_circle.width - rotated_inner_circle.width) // 2, (rotated_outer_circle.height - rotated_inner_circle.height) // 2)

#     # นำวงกลมมาวางบนรูปภาพหลัก
#     rotated_outer_circle.paste(rotated_inner_circle, position, rotated_inner_circle)

#     # Convert combined image to OpenCV format for processing
#     combined_image_cv = pil_to_cv(rotated_outer_circle)
    
#     # Convert to grayscale
#     gray_combined = cv2.cvtColor(combined_image_cv, cv2.IMREAD_GRAYSCALE)
    
#     # Apply Canny edge detection
#     edges_combined = cv2.Canny(gray_combined, 200, 250)


#     # แสดงภาพหลังจากทำการวางวงกลม
#     # rotated_outer_circle.show()
#     # Update the displayed image
#     plt.title(f'Circle Rotated by {angle} Degrees')
#     image_display.set_data(edges_combined)
#     plt.axis('off')  # ปิดการแสดงเส้นขอบแกน
#     plt.draw()
#     plt.pause(0.5)  # Pause to allow the image to update

#     angle += 1


# # rotated_inner_circle = inner_circle.rotate(-61)
# # rotated_outer_circle = outer_circle.rotate(61)


# # # คำนวณตำแหน่งที่จะนำวงกลมที่ได้มาวางบนรูปภาพหลัก
# # position = ((rotated_outer_circle.width - rotated_inner_circle.width) // 2, (rotated_outer_circle.height - rotated_inner_circle.height) // 2)

# # # นำวงกลมมาวางบนรูปภาพหลัก
# # rotated_outer_circle.paste(rotated_inner_circle, position, rotated_inner_circle)

# # # Convert combined image to OpenCV format for processing
# # combined_image_cv = pil_to_cv(rotated_outer_circle)
    
# # # Convert to grayscale
# # gray_combined = cv2.cvtColor(combined_image_cv, cv2.COLOR_BGRA2GRAY)
    
# # # Apply Canny edge detection
# # edges_combined = cv2.Canny(gray_combined, 50, 300)


# # # แสดงภาพหลังจากทำการวางวงกลม
# # # rotated_outer_circle.show()
# # # Update the displayed image
# # plt.imshow(edges_combined, cmap='gray')
# # plt.title(f'Circle Rotated by {angle} Degrees')
# # # image_display.set_data(edges_combined)
# # plt.axis('off')  # ปิดการแสดงเส้นขอบแกน
# # plt.show()
# # # plt.draw()
# # # plt.pause(0.5)  # Pause to allow the image to update

from PIL import Image, ImageDraw, ImageFilter
import requests
import numpy as np
from io import BytesIO
import cv2
import matplotlib.pyplot as plt
from skimage.measure import label

# Function to download image from URL
def download_image(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

# Function to create a circular mask
def create_circular_mask(image):
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)
    return mask

# Function to apply mask to an image
def apply_mask(image, mask):
    circle = Image.new("RGBA", image.size, (255, 255, 255, 0))
    circle.paste(image, mask=mask)
    return circle

# Function to convert a PIL image to OpenCV format
def pil_to_cv(image):
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGBA2BGRA)

# Function to highlight edges on an image
def highlight_edges(image, edges):
    highlighted = image.copy()
    highlighted[edges == 255] = [0, 0, 255, 255]  # Highlight edges with red color
    return highlighted

# URLs of the images
# inner_image_url = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/cb6f9526f9594194a09df643881cd0e8~tplv-b4yrtqhy5a-2.jpeg"
# outer_image_url = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/8482448d6eeb4977abf869568b33a1e3~tplv-b4yrtqhy5a-2.jpeg"

inner_image_url = "https://p19-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/1cf86d4b1c584aa2b2d3918eae7f56a4~tplv-b4yrtqhy5a-2.jpeg"
outer_image_url = "https://p19-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/b8d9e736e2e14a13ab81a8f000a116b4~tplv-b4yrtqhy5a-2.jpeg"

# Download images
inner_image = download_image(inner_image_url)
outer_image = download_image(outer_image_url)

# Create masks
mask_inner = create_circular_mask(inner_image)
mask_outer = create_circular_mask(outer_image)

# Apply masks
inner_circle = apply_mask(inner_image, mask_inner)
outer_circle = apply_mask(outer_image, mask_outer)

# Smooth the inner circle
smoothed_inner_circle = inner_circle.filter(ImageFilter.GaussianBlur(radius=0.7))

# Setup matplotlib
fig, ax = plt.subplots()
image_display = ax.imshow(outer_image)
plt.ion()  # Turn on interactive mode
plt.show()

# # Function to calculate edge similarity
# def calculate_edge_similarity(edges1, edges2):
#     intersection = np.logical_and(edges1, edges2)
#     union = np.logical_or(edges1, edges2)
#     similarity = np.sum(intersection) / np.sum(union)
#     return similarity

best_angle = 0
best_similarity = 0

# Function to calculate standard deviation of edges
def calculate_edge_smoothness(edges):
    return np.std(edges)

best_angle = 0
best_smoothness = float('inf')
angle = 5
arr_smooth= []
# Loop through angles to find the best match
while angle < 179 :
# for angle in range(62):
    rotated_inner_circle = inner_circle.rotate(-angle)
    rotated_outer_circle = outer_circle.rotate(angle)

    # inner_image_cv = pil_to_cv(rotated_inner_circle)
    # outer_image_cv = pil_to_cv(rotated_outer_circle)

    # inner_combined = cv2.cvtColor(inner_image_cv, cv2.COLOR_BGRA2GRAY)
    # outer_combined = cv2.cvtColor(outer_image_cv, cv2.COLOR_BGRA2GRAY)
    
    

    # edges_inner = cv2.Canny(inner_combined, 200, 250)
    # edges_outer = cv2.Canny(outer_combined, 200, 250)

    # Calculate position to paste inner circle on outer circle
    position = ((rotated_outer_circle.width - rotated_inner_circle.width) // 2, (rotated_outer_circle.height - rotated_inner_circle.height) // 2)

    # Paste inner circle on outer circle
    combined_image = rotated_outer_circle.copy()
    combined_image.paste(rotated_inner_circle, position, rotated_inner_circle)

    # Convert combined image to OpenCV format for processing
    combined_image_cv = pil_to_cv(combined_image)
    
    # Convert to grayscale
    gray_combined = cv2.cvtColor(combined_image_cv, cv2.COLOR_BGRA2GRAY)
    
    
    # Apply Canny edge detection
    edges_combined = cv2.Canny(gray_combined, 100, 150)
    
    # Calculate edge similarity
    # similarity = calculate_edge_similarity(edges_combined, edges_combined)
    
    # if similarity > best_similarity:
    #     best_similarity = similarity
    #     best_angle = angle
    
    # Highlight edges
    highlighted_edges = highlight_edges(combined_image_cv, edges_combined)

        # หาขอบที่เชื่อมกัน
    labeled_edges, num_labels = label(highlighted_edges, connectivity=2, background=0, return_num=True)

    # print(f"Number of connected components: {num_labels}")

        # Calculate edge smoothness
    smoothness = calculate_edge_smoothness(highlighted_edges)
    print(f"circles to align is: {angle} degrees with edge smoothness: {smoothness}, Number of connected components: {num_labels}")
    arr_smooth.append([angle,smoothness,num_labels])
    if smoothness < best_smoothness:
        best_smoothness = smoothness
        best_angle = angle

    # Update the displayed image
    plt.title(f'Circle Rotated by {angle} Degrees')
    image_display.set_data(cv2.cvtColor(highlighted_edges, cv2.COLOR_BGRA2RGBA))
    plt.axis('off')  # Turn off axis
    plt.draw()
    plt.pause(0.1)  # Pause to allow the image to update

    angle += 0.5

plt.ioff()  # Turn off interactive mode
plt.show()
degree_arr = np.array(arr_smooth)

# Find the index where there are more True and less False values
best_index = np.argmin(degree_arr[:, 1])

# Print the results for the best angle
print(f"Best Angle: {degree_arr[best_index, 0]} degrees")
print(f"Best smooth: {degree_arr[best_index, 1]}")
print(f"The best angle for the circles to align is: {best_angle} degrees with edge smoothness: {best_smoothness}")
# print(f"The best angle for the circles to align is: {best_angle} degrees")

sorted_indices = np.argsort(degree_arr[:, 1])  # เรียงลำดับดัชนีตามค่าของคอลัมน์ที่ 1

# ดูข้อมูล 5 อันดับแรกที่ต่ำสุด
for i in range(5):
    index = sorted_indices[i]
    value = degree_arr[index, 1]  # หรือตำแหน่งคอลัมน์ที่คุณต้องการ
    ang = degree_arr[index, 0]  # หรือตำแหน่งคอลัมน์ที่คุณต้องการ
    print(f"Rank {i+1}: Index {index}, Value {value},angle,{ang}")
