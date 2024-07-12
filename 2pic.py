# # # from PIL import Image, ImageDraw, ImageChops, ImageFilter
# # # import requests
# # # from io import BytesIO

# # # # URL ของรูปภาพ
# # # image_url = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/33d4c5833251402ba8f107504f983ad5~tplv-b4yrtqhy5a-2.jpeg"
# # # main_image_url = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/0c6fd0772cc94c27ad60066eff434d14~tplv-b4yrtqhy5a-2.jpeg"


# # # # ดาวน์โหลดรูปภาพ
# # # response = requests.get(image_url)
# # # image = Image.open(BytesIO(response.content))

# # # response_main = requests.get(main_image_url)
# # # main_image = Image.open(BytesIO(response_main.content))

# # # # สร้างภาพวงกลม
# # # mask = Image.new("L", image.size, 0)
# # # draw = ImageDraw.Draw(mask)
# # # draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)

# # # # ตัดขอบสีขาวออก
# # # result = Image.new("RGBA", image.size, (255, 255, 255, 0))
# # # result.paste(image, mask=mask)

# # # outer_circle = Image.new("L", main_image.size, 0)
# # # draw_outer = ImageDraw.Draw(outer_circle)
# # # draw_outer.ellipse((0, 0, main_image.size[0], main_image.size[1]), fill=255)

# # # # เช็คว่าขอบของวงกลมภายในตรงกับขอบของวงกลมภายนอกหรือไม่
# # # inner_bbox = result.getbbox()
# # # outer_bbox = outer_circle.getbbox()

# # # if inner_bbox == outer_bbox:
# # #     print("ขอบของวงกลมรูปภายในตรงกับวงกลมรูปภายนอก")
# # # else:
# # #     print("ขอบของวงกลมรูปภายในไม่ตรงกับวงกลมรูปภายนอก")

# # # # หมุนรูปภาพภายในเพื่อเช็คว่าภาพที่หมุนไปกี่องศาจะเป็นภาพที่ตรงกันสมบูรณ์
# # # for angle in range(0, 180, 10):  # หมุนทุก 10 องศา
# # #     rotated_inner = result.rotate(angle)
# # #     rotated_outer = outer_circle.rotate(angle)
    
# # #     inner_bbox_rotated = rotated_inner.getbbox()
# # #     outer_bbox_rotated = rotated_outer.getbbox()

# # #     print(inner_bbox_rotated,outer_bbox_rotated)
    
# # #     if inner_bbox_rotated == outer_bbox_rotated:
# # #         print(f"ภาพที่ตรงกันสมบูรณ์ที่การหมุน: {angle} องศา")
# # #         break  # หากเจอการหมุนที่ตรงกันสมบูรณ์ก็หยุดการวนลูป

# # # # แสดงภาพ
# # # # result.show()
# # # # i = 0
# # # # while i  < 180:
# # # #     inner_rotate_image = result.rotate(i)

# # # #     # # คำนวณตำแหน่งที่จะนำวงกลมที่ได้มาวางบนรูปภาพหลัก
# # # #     # position = ((main_image.width - inner_rotate_image.width) // 2, (main_image.height - inner_rotate_image.height) // 2)

# # # #     # # นำวงกลมมาวางบนรูปภาพหลัก
# # # #     # main_image.paste(inner_rotate_image, position, inner_rotate_image)

# # # #     # position = ((main_image.width - inner_rotate_image.width) // 2, (main_image.height - inner_rotate_image.height) // 2)

# # # #     # คำนวณขอบของวงกลมภายใน
# # # #     inner_bbox = inner_rotate_image.getbbox()

# # # #     # คำนวณขอบของวงกลมภายนอก
# # # #     outer_bbox = main_image.getbbox()
# # # #     # print(outer_bbox)

# # # #     if inner_bbox == outer_bbox:
# # # #         print("ขอบของวงกลมรูปภายในตรงกับวงกลมรูปภายนอก")
# # # #     else:
# # # #         pass
# # # #         # print("ขอบของวงกลมรูปภายในไม่ตรงกับวงกลมรูปภายนอก")

# # # #     # หมุนรูปภาพภายในเพื่อเช็คว่าภาพที่หมุนไปกี่องศาจะเป็นภาพที่ตรงกันสมบูรณ์
# # # #     for angle in range(0, 361, 10):  # หมุนทุก 10 องศา
# # # #         rotated_inner = result.rotate(angle)
# # # #         rotated_outer = main_image.rotate(angle)
        
# # # #         inner_bbox_rotated = rotated_inner.getbbox()
# # # #         outer_bbox_rotated = rotated_outer.getbbox()
        
# # # #         if inner_bbox_rotated == outer_bbox_rotated:
# # # #             print(f"ภาพที่ตรงกันสมบูรณ์ที่การหมุน: {angle} องศา")
# # # #             break  # หากเจอการหมุนที่ตรงกันสมบูรณ์ก็หยุดการวนลูป





# # # #     i+= 1


# # import cv2
# # import numpy as np
# # import requests
# # from PIL import Image, ImageDraw  # Import the Image and ImageDraw classes from Pillow
# # from io import BytesIO
# # from matplotlib import pyplot as plt

# # # Function to download an image from a URL and convert it to a numpy array
# # def download_image(url):
# #     response = requests.get(url)
# #     image = np.array(Image.open(BytesIO(response.content)))
# #     return image

# # # Function to rotate an image around its center
# # def rotate_image(image, angle):
# #     image_pil = Image.fromarray(image)
# #     mask = Image.new("L", image_pil.size, 0)
# #     draw = ImageDraw.Draw(mask)
# #     draw.ellipse((0, 0, image_pil.size[0], image_pil.size[1]), fill=255)

# #     inner_circle = Image.new("RGBA", image_pil.size, (255, 255, 255, 0))
# #     inner_circle.paste(image_pil, mask=mask)

# #     rotated_pil = inner_circle.rotate(angle, resample=Image.BICUBIC, expand=True)
# #     rotated_image = np.array(rotated_pil)
# #     return rotated_image

# # # Function to resize image to match the target size
# # def resize_image(image, target_size):
# #     return cv2.resize(image, (target_size[1], target_size[0]))

# # # URLs of the images
# # image_url = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/33d4c5833251402ba8f107504f983ad5~tplv-b4yrtqhy5a-2.jpeg"
# # main_image_url = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/0c6fd0772cc94c27ad60066eff434d14~tplv-b4yrtqhy5a-2.jpeg"
# # # Download images
# # inner_image = download_image(image_url)
# # outer_image = download_image(main_image_url)

# # # Rotate the inner image by 55 degrees
# # rotated_inner_image = rotate_image(inner_image, 67)

# # # Resize the rotated inner image to match the outer image size
# # rotated_inner_image_resized = resize_image(rotated_inner_image, outer_image.shape)

# # # Convert to grayscale
# # gray_inner = cv2.cvtColor(rotated_inner_image_resized, cv2.COLOR_RGBA2GRAY)
# # gray_outer = cv2.cvtColor(outer_image, cv2.COLOR_BGR2GRAY)

# # # Apply Canny edge detection
# # edges_inner = cv2.Canny(gray_inner, 100, 200)
# # edges_outer = cv2.Canny(gray_outer, 100, 200)

# # # Display edges for both images
# # plt.subplot(121), plt.imshow(edges_inner, cmap='gray')
# # plt.title('Rotated Inner Circle Edges'), plt.xticks([]), plt.yticks([])

# # plt.subplot(122), plt.imshow(edges_outer, cmap='gray')
# # plt.title('Outer Circle Edges'), plt.xticks([]), plt.yticks([])

# # plt.show()

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

# # is_smooth = align_and_check_edges(edges_inner, edges_outer)
# # print(f"The edges form a smooth picture: {is_smooth}")
# from PIL import Image, ImageDraw, ImageFilter
# import requests
# from io import BytesIO
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# import time
# # URL ของรูปภาพ
# inner_image_url = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/cb6f9526f9594194a09df643881cd0e8~tplv-b4yrtqhy5a-2.jpeg"
# outer_image_url = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/8482448d6eeb4977abf869568b33a1e3~tplv-b4yrtqhy5a-2.jpeg"

# # ดาวน์โหลดรูปภาพ
# response = requests.get(inner_image_url)
# inner_image = Image.open(BytesIO(response.content))

# response_main = requests.get(outer_image_url)
# outer_image = Image.open(BytesIO(response_main.content))

# # สร้างภาพวงกลม
# mask = Image.new("L", inner_image.size, 0)
# draw = ImageDraw.Draw(mask)
# draw.ellipse((0, 0, inner_image.size[0], inner_image.size[1]), fill=255)

# mask2 = Image.new("L", outer_image.size, 0)
# draw = ImageDraw.Draw(mask2)
# draw.ellipse((0, 0, outer_image.size[0], outer_image.size[1]), fill=255)

# # ตัดขอบสีขาวออก
# inner_circle = Image.new("RGBA", inner_image.size, (255, 255, 255, 0))
# inner_circle.paste(inner_image, mask=mask)

# outer_circle = Image.new("RGBA", outer_image.size, (255, 255, 255, 0))
# outer_circle.paste(outer_image, mask=mask2)
# # smoothed_inner_circle = inner_circle.filter(ImageFilter.GaussianBlur(radius=0.7))
# # Setup matplotlib
# fig, ax = plt.subplots()
# image_display = ax.imshow(outer_image)
# plt.ion()  # Turn on interactive mode
# plt.show()

# angle = 0
# # while angle < 180:
# #     rotated_inner_circle = inner_circle.rotate(-(angle))
# #     rotated_outer_circle = outer_circle.rotate(angle)
# #     # คำนวณตำแหน่งที่จะนำวงกลมที่ได้มาวางบนรูปภาพหลัก
# #     position = ((rotated_outer_circle.width - rotated_inner_circle.width) // 2, (rotated_outer_circle.height - rotated_inner_circle.height) // 2)

# #     # นำวงกลมมาวางบนรูปภาพหลัก
# #     rotated_outer_circle.paste(rotated_inner_circle, position, rotated_inner_circle)

# #     position = ((rotated_outer_circle.width - rotated_inner_circle.width) // 2, (rotated_outer_circle.height - rotated_inner_circle.height) // 2)


# #     # แสดงภาพหลังจากทำการวางวงกลม
# #     # rotated_outer_circle.show()
# #     # Update the displayed image
# #     plt.title(f'Circle Rotated by {angle} Degrees')
# #     image_display.set_data(rotated_outer_circle)
# #     plt.draw()
# #     plt.pause(0.5)  # Pause to allow the image to update

# #     angle += 1
# # Function to convert a PIL image to a numpy array
# def pil_to_np(image):
#     return np.array(image)

# # Function to calculate edge overlap score
# def calculate_overlap_score(image1, image2):
#     gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
#     gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    
#     edges1 = cv2.Canny(gray1, 100, 200)
#     edges2 = cv2.Canny(gray2, 100, 200)
    
#     overlap = cv2.bitwise_and(edges1, edges2)
#     return cv2.countNonZero(overlap)

# best_angle = 0
# best_score = 0
# results = []
# angle = 0
# # for angle in range(-180, 180, 1):
# while angle < 180:
#     rotated_inner_circle =  inner_circle.rotate(-(angle))
#     rotated_outer_image = outer_circle.rotate(angle)
    
#     # Create a blank canvas for combining the images
#     combined_image = Image.new("RGBA", rotated_outer_image.size)
#     position = ((rotated_outer_image.width - rotated_inner_circle.width) // 2, 
#                 (rotated_outer_image.height - rotated_inner_circle.height) // 2)
    
#     # Ensure the mask matches the size of the rotated inner circle
#     rotated_mask = mask.rotate(-angle, expand=True)
#     rotated_mask = rotated_mask.resize(rotated_inner_circle.size, Image.Resampling.LANCZOS)
   
    
#     # Paste the rotated inner circle onto the rotated outer image
#     combined_image.paste(rotated_outer_image, (0, 0))
#     combined_image.paste(rotated_inner_circle, position, rotated_inner_circle.split()[3])
    
#     # Convert combined image to numpy array for edge detection
#     combined_image_np = pil_to_np(combined_image.convert("RGB"))
    
#     # Calculate overlap score
#     score = calculate_overlap_score(combined_image_np, combined_image_np)
    
#     results.append((angle, score))
#     if score > best_score:
#         best_score = score
#         best_angle = angle

#     angle += 1

# print(f"Best matching angle: {best_angle} degrees with score: {best_score}")
# # Plot the best combined image

# # Sort results to find the best alignment
# results.sort(key=lambda x: x[1], reverse=True)
# for angle, score in results[:10]:  # Print top 10 best results
#     print(f"Angle: {angle} degrees, Score: {score}")


# rotated_inner_circle = inner_circle.rotate(-best_angle)
# rotated_outer_circle = outer_circle.rotate(best_angle)

# rotated_outer_circle.paste(rotated_inner_circle, position, rotated_inner_circle)

# position = ((rotated_outer_circle.width - rotated_inner_circle.width) // 2, (rotated_outer_circle.height - rotated_inner_circle.height) // 2)
# rotated_outer_circle.show()

# # from PIL import Image, ImageDraw, ImageFilter, ImageChops
# # import requests
# # from io import BytesIO
# # import numpy as np
# # import matplotlib.pyplot as plt

# # # URL ของรูปภาพ
# # inner_image_url = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/cb6f9526f9594194a09df643881cd0e8~tplv-b4yrtqhy5a-2.jpeg"
# # outer_image_url = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/8482448d6eeb4977abf869568b33a1e3~tplv-b4yrtqhy5a-2.jpeg"

# # # ดาวน์โหลดรูปภาพ
# # response = requests.get(inner_image_url)
# # inner_image = Image.open(BytesIO(response.content))

# # response_main = requests.get(outer_image_url)
# # outer_image = Image.open(BytesIO(response_main.content))

# # # สร้างภาพวงกลม
# # mask = Image.new("L", inner_image.size, 0)
# # draw = ImageDraw.Draw(mask)
# # draw.ellipse((0, 0, inner_image.size[0], inner_image.size[1]), fill=255)

# # mask2 = Image.new("L", outer_image.size, 0)
# # draw = ImageDraw.Draw(mask2)
# # draw.ellipse((0, 0, outer_image.size[0], outer_image.size[1]), fill=255)

# # # ตัดขอบสีขาวออก
# # inner_circle = Image.new("RGBA", inner_image.size, (255, 255, 255, 0))
# # inner_circle.paste(inner_image, mask=mask)

# # outer_circle = Image.new("RGBA", outer_image.size, (255, 255, 255, 0))
# # outer_circle.paste(outer_image, mask=mask2)

# # # Function to convert a PIL image to a numpy array
# # def pil_to_np(image):
# #     return np.array(image)

# # # Function to calculate edge overlap score
# # def calculate_overlap_score(image1, image2):
# #     # Convert images to grayscale mode
# #     gray1 = image1.convert("L")
# #     gray2 = image2.convert("L")
    
# #     # Find edges using FIND_EDGES filter
# #     edges1 = gray1.filter(ImageFilter.FIND_EDGES)
# #     edges2 = gray2.filter(ImageFilter.FIND_EDGES)
    
# #     # Convert edges images to binary mode
# #     edges1_binary = edges1.convert("1")
# #     edges2_binary = edges2.convert("1")
    
# #     # Calculate overlap using logical_and
# #     overlap = ImageChops.logical_and(edges1_binary, edges2_binary)
    
# #     # Count non-zero pixels as score
# #     score = overlap.getbbox()[2] * overlap.getbbox()[3]  # Width * Height of bounding box
# #     return score
# # best_angle = 0
# # best_score = 0
# # results = []
# # angle_step = 1
# # angle = 0

# # while angle < 180:
# #     rotated_inner_circle = inner_circle.rotate(-angle)
# #     rotated_outer_circle = outer_circle.rotate(angle)
    
# #     # Calculate overlap score
# #     score = calculate_overlap_score(rotated_inner_circle, rotated_outer_circle)
    
# #     results.append((angle, score))
# #     if score > best_score:
# #         best_score = score
# #         best_angle = angle

# #     angle += angle_step

# # print(f"Best matching angle: {best_angle} degrees with score: {best_score}")

# # # Sort results to find the best alignment
# # results.sort(key=lambda x: x[1], reverse=True)
# # for angle, score in results[:10]:  # Print top 10 best results
# #     print(f"Angle: {angle} degrees, Score: {score}")
# # # Plot the best combined image
# # rotated_inner_circle = inner_circle.rotate(best_angle)
# # rotated_outer_circle = outer_circle.rotate(best_angle)

# # # Create a blank canvas for combining the images
# # combined_image = Image.new("RGBA", outer_circle.size)
# # position = ((outer_circle.width - rotated_inner_circle.width) // 2, 
# #             (outer_circle.height - rotated_inner_circle.height) // 2)

# # # Paste the rotated inner circle onto the rotated outer image
# # combined_image.paste(rotated_outer_circle, (0, 0))
# # combined_image.paste(rotated_inner_circle, position, rotated_inner_circle)

# # plt.imshow(combined_image)
# # plt.title(f'Best Matching Angle: {best_angle} Degrees')
# # plt.axis('off')
# # plt.show()
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
    width, height = image.size
    draw.ellipse((5, 5, width-5, height-5), fill=255)
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

# Function to calculate standard deviation of edges
def calculate_edge_smoothness(edges):
    return np.std(edges)

# Function to calculate color histogram similarity
def calculate_color_similarity(image1, image2):
    hist1 = cv2.calcHist([image1], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist2 = cv2.calcHist([image2], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist1 = cv2.normalize(hist1, hist1).flatten()
    hist2 = cv2.normalize(hist2, hist2).flatten()
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    return similarity

# URLs of the images
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

best_angle = 0
best_smoothness = float('inf')
best_color_similarity = 0
angle = 2
arr_smooth= []

scale_factor = 5
new_size = (int(inner_circle.width +    scale_factor), int(inner_circle.height + scale_factor))
resized_inner_circle = inner_circle.resize(new_size, Image.LANCZOS)  # ใช้ Image.LANCZOS เพื่อปรับขนาดอย่างเสถีย

# Loop through angles to find the best match
while angle < 180:
    rotated_inner_circle = resized_inner_circle.rotate(-angle)
    rotated_outer_circle = outer_circle.rotate(angle)

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
    
    # Highlight edges
    highlighted_edges = highlight_edges(combined_image_cv, edges_combined)

    # Find connected components of edges
    labeled_edges, num_labels = label(highlighted_edges, connectivity=2, background=0, return_num=True)

    # Calculate edge smoothness
    smoothness = calculate_edge_smoothness(highlighted_edges)

    # Calculate color similarity
    color_similarity = calculate_color_similarity(pil_to_cv(rotated_inner_circle), pil_to_cv(rotated_outer_circle))

    print(f"Angle: {angle} degrees, Edge Smoothness: {smoothness}, Color Similarity: {color_similarity}, Connected Components: {num_labels}")

    arr_smooth.append([angle, smoothness, color_similarity, num_labels])

    if smoothness < best_smoothness and color_similarity > best_color_similarity:
        best_smoothness = smoothness
        best_color_similarity = color_similarity
        best_angle = angle

    # Update the displayed image
    plt.title(f'Circle Rotated by {angle} Degrees')
    image_display.set_data(cv2.cvtColor(highlighted_edges, cv2.COLOR_BGRA2RGBA))
    plt.axis('off')  # Turn off axis
    plt.draw()
    plt.pause(0.1)  # Pause to allow the image to update

    angle += 1

plt.ioff()  # Turn off interactive mode
plt.show()

degree_arr = np.array(arr_smooth)

# Find the index where the smoothness is minimized and color similarity is maximized
best_index = np.argmin(degree_arr[:, 1])

# Print the results for the best angle
print(f"Best Angle: {degree_arr[best_index, 0]} degrees")
print(f"Best Edge Smoothness: {degree_arr[best_index, 1]}")
print(f"Best Color Similarity: {degree_arr[best_index, 2]}")
print(f"Number of Connected Components: {degree_arr[best_index, 3]}")
print(f"The best angle for the circles to align is: {best_angle} degrees with edge smoothness: {best_smoothness} and color similarity: {best_color_similarity}")

# Sort the results and print the top 5 angles
sorted_indices = np.argsort(degree_arr[:, 1])  # Sort indices by edge smoothness

for i in range(5):
    index = sorted_indices[i]
    value = degree_arr[index, 1]  # Edge smoothness
    angle = degree_arr[index, 0]  # Angle
    color_similarity = degree_arr[index, 2]  # Color similarity
    num_labels = degree_arr[index, 3]  # Number of connected components
    print(f"Rank {i+1}: Angle {angle} degrees, Edge Smoothness {value}, Color Similarity {color_similarity}, Connected Components {num_labels}")
