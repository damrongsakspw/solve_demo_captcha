# # # from PIL import Image, ImageDraw, ImageFilter
# # # import requests
# # # from io import BytesIO
# # # import matplotlib.pyplot as plt
# # # import cv2
# # # import numpy as np
# # # from skimage.measure import label
# # # # URL ของรูปภาพ
# # # inner_image_url = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/cb6f9526f9594194a09df643881cd0e8~tplv-b4yrtqhy5a-2.jpeg"
# # # outer_image_url = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/8482448d6eeb4977abf869568b33a1e3~tplv-b4yrtqhy5a-2.jpeg"



# # # # Function to calculate standard deviation of edges
# # # def calculate_edge_smoothness(edges):
# # #     return np.std(edges)
# # # # Function to download image from URL
# # # def download_image(url):
# # #     response = requests.get(url)
# # #     return Image.open(BytesIO(response.content))

# # # # Function to create a circular mask
# # # def create_circular_mask(image):
# # #     mask = Image.new("L", image.size, 0)
# # #     draw = ImageDraw.Draw(mask)
# # #     draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)
# # #     return mask

# # # # Function to apply mask to an image
# # # def apply_mask(image, mask):
# # #     circle = Image.new("RGBA", image.size, (255, 255, 255, 0))
# # #     circle.paste(image, mask=mask)
# # #     return circle

# # # # Function to convert a PIL image to OpenCV format
# # # def pil_to_cv(image):
# # #     return cv2.cvtColor(np.array(image), cv2.COLOR_RGBA2BGRA)

# # # # Function to highlight edges on an image
# # # def highlight_edges(image, edges):
# # #     highlighted = image.copy()
# # #     highlighted[edges == 255] = [0, 0, 255, 255]  # Highlight edges with red color
# # #     return highlighted


# # # # ดาวน์โหลดรูปภาพ
# # # response = requests.get(inner_image_url)
# # # inner_image = Image.open(BytesIO(response.content))

# # # response_main = requests.get(outer_image_url)
# # # outer_image = Image.open(BytesIO(response_main.content))

# # # # สร้างภาพวงกลม
# # # mask = Image.new("L", inner_image.size, 0)
# # # draw = ImageDraw.Draw(mask)
# # # width_in, height_in = inner_image.size
# # # draw.ellipse((2, 2, width_in-2, height_in-2), fill=255)
# # # inner_circle = Image.new('RGBA', inner_image.size, (255, 255, 255, 0))
# # # inner_circle.paste(inner_image, mask=mask)

# # # # inner_circle.show()

# # # # inner_circle = inner_image.resize((212, 212), Image.LANCZOS)
# # # # inner_circle = Image.new('RGBA', inner_image.size, (255, 255, 255, 0))
# # # # inner_circle.paste(inner_image, mask=mask)

# # # mask2 = Image.new("L", outer_image.size, 0)
# # # draw = ImageDraw.Draw(mask2)
# # # width_out, height_out = outer_image.size
# # # draw.ellipse((0, 0, width_out, height_out), fill=255)


# # # # ตัดขอบสีขาวออก
# # # # inner_circle = Image.new("RGBA", resized_image.size, (255, 255, 255, 0))
# # # # inner_circle.paste(resized_image, mask=mask)

# # # outer_circle = Image.new("RGBA", outer_image.size, (255, 255, 255, 0))
# # # outer_circle.paste(outer_image, mask=mask2)

# # # # ใช้ Gaussian Blur เพื่อจัดขอบให้ smooth ขึ้น
# # # # smoothed_inner_circle = inner_circle.filter(ImageFilter.GaussianBlur(radius=0.7))

# # # # เพิ่มความชัดของ inner_circle และ outer_circle
# # # # sharpened_inner_circle = smoothed_inner_circle.filter(ImageFilter.SHARPEN(radius=2.0))
# # # # sharpened_outer_circle = outer_circle.filter(ImageFilter.SHARPEN(radius=2.0))


# # # # แสดงรูปภาพ
# # # # plt.imshow(smoothed_inner_circle)
# # # # plt.axis('off')  # ปิดการแสดงเส้นขอบแกน
# # # # plt.show()

# # # # Setup matplotlib
# # # fig, ax = plt.subplots()
# # # image_display = ax.imshow(outer_image)
# # # plt.ion()  # Turn on interactive mode
# # # plt.show()

# # # angle = 0
# # # scale_factor = 5
# # # best_angle = 0
# # # best_smoothness = float('inf')
# # # angle = 5
# # # arr_smooth= []
# # # # Function to convert a PIL image to grayscale
# # # def pil_to_grayscale(image):
# # #     return image.convert("L")

# # # new_size = (int(inner_circle.width +    scale_factor), int(inner_circle.height + scale_factor))
# # # resized_inner_circle = inner_circle.resize(new_size, Image.LANCZOS)  # ใช้ Image.LANCZOS เพื่อปรับขนาดอย่างเสถีย
# # # resized_inner_circle.show()
# # # while angle <180:
# # # # for angle in range(-180, 180, 1):
# # # # กำหนดขนาดใหม่ของวงกลมภายใน

# # #     rotated_inner_circle = resized_inner_circle.rotate(-angle)
  
# # #     rotated_outer_circle = outer_circle.rotate(angle)
# # #     # คำนวณตำแหน่งที่จะนำวงกลมที่ได้มาวางบนรูปภาพหลัก
# # #     position = ((rotated_outer_circle.width - rotated_inner_circle.width) // 2, (rotated_outer_circle.height - rotated_inner_circle.height) // 2)

# # #     # นำวงกลมมาวางบนรูปภาพหลัก
# # #     rotated_outer_circle.paste(rotated_inner_circle, position, rotated_inner_circle)

# # #         # Paste inner circle on outer circle
# # #     combined_image = rotated_outer_circle.copy()
# # #     combined_image.paste(rotated_inner_circle, position, rotated_inner_circle)

# # #      # Convert combined image to OpenCV format for processing
# # #     combined_image_cv = pil_to_cv(combined_image)
    
# # #     # Convert to grayscale
# # #     gray_combined = cv2.cvtColor(combined_image_cv, cv2.COLOR_BGRA2GRAY)
    
    
# # #     # Apply Canny edge detection
# # #     edges_combined = cv2.Canny(gray_combined, 100, 120)
    
# # #     # Calculate edge similarity
# # #     # similarity = calculate_edge_similarity(edges_combined, edges_combined)
    
# # #     # if similarity > best_similarity:
# # #     #     best_similarity = similarity
# # #     #     best_angle = angle
    
# # #     # Highlight edges
# # #     highlighted_edges = highlight_edges(combined_image_cv, edges_combined)

# # #         # หาขอบที่เชื่อมกัน
# # #     labeled_edges, num_labels = label(highlighted_edges, connectivity=2, background=0, return_num=True)

# # #     # print(f"Number of connected components: {num_labels}")

# # #         # Calculate edge smoothness
# # #     smoothness = calculate_edge_smoothness(highlighted_edges)
# # #     print(f"circles to align is: {angle} degrees with edge smoothness: {smoothness}, Number of connected components: {num_labels}")
# # #     arr_smooth.append([angle,smoothness,num_labels])
# # #     if smoothness < best_smoothness:
# # #         best_smoothness = smoothness
# # #         best_angle = angle

# # #     # Update the displayed image
# # #     plt.title(f'Circle Rotated by {angle} Degrees')
# # #     image_display.set_data(cv2.cvtColor(highlighted_edges, cv2.COLOR_BGRA2RGBA))
# # #     plt.axis('off')  # Turn off axis
# # #     plt.draw()
# # #     plt.pause(0.1)  # Pause to allow the image to update

# # #     angle += 0.5

# # # plt.ioff()  # Turn off interactive mode
# # # plt.show()
# # # degree_arr = np.array(arr_smooth)

# # # # Find the index where there are more True and less False values
# # # best_index = np.argmin(degree_arr[:, 1])

# # # # Print the results for the best angle
# # # print(f"Best Angle: {degree_arr[best_index, 0]} degrees")
# # # print(f"Best smooth: {degree_arr[best_index, 1]}")
# # # print(f"The best angle for the circles to align is: {best_angle} degrees with edge smoothness: {best_smoothness}")
# # # # print(f"The best angle for the circles to align is: {best_angle} degrees")

# # # sorted_indices = np.argsort(degree_arr[:, 1])  # เรียงลำดับดัชนีตามค่าของคอลัมน์ที่ 1

# # # # ดูข้อมูล 5 อันดับแรกที่ต่ำสุด
# # # for i in range(5):
# # #     index = sorted_indices[i]
# # #     value = degree_arr[index, 1]  # หรือตำแหน่งคอลัมน์ที่คุณต้องการ
# # #     ang = degree_arr[index, 0]  # หรือตำแหน่งคอลัมน์ที่คุณต้องการ
# # #     print(f"Rank {i+1}: Index {index}, Value {value},angle,{ang}")

# # # # import numpy as np
# # # # import cv2
# # # # import requests
# # # # from io import BytesIO
# # # # from PIL import Image

# # # # def download_image(url):
# # # #     response = requests.get(url)
# # # #     image = Image.open(BytesIO(response.content))
# # # #     return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

# # # # # URLs of the images
# # # # image_url1 = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/cb6f9526f9594194a09df643881cd0e8~tplv-b4yrtqhy5a-2.jpeg"
# # # # image_url2 = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/8482448d6eeb4977abf869568b33a1e3~tplv-b4yrtqhy5a-2.jpeg"

# # # # # Download images
# # # # image1 = download_image(image_url1)
# # # # image2 = download_image(image_url2)

# # # # # Convert images to grayscale
# # # # gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
# # # # gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# # # # # Initialize ORB detector
# # # # orb = cv2.ORB_create()

# # # # # Find keypoints and descriptors with ORB
# # # # keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
# # # # keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)

# # # # # Match descriptors using Brute Force matching
# # # # bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# # # # matches = bf.match(descriptors1, descriptors2)

# # # # # Sort matches by distance
# # # # matches = sorted(matches, key=lambda x: x.distance)

# # # # # Extract matched keypoints
# # # # points1 = np.float32([keypoints1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
# # # # points2 = np.float32([keypoints2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

# # # # # Find Homography
# # # # H, _ = cv2.findHomography(points2, points1, cv2.RANSAC)

# # # # # Warp image2 to image1
# # # # height, width, channels = image1.shape
# # # # warped_image2 = cv2.warpPerspective(image2, H, (width + image2.shape[1], height))

# # # # # Blend the images
# # # # result = cv2.addWeighted(image1, 0.5, warped_image2, 0.5, 0)

# # # # # Display the stitched image
# # # # cv2.imshow('Stitched Image', result)
# # # # cv2.waitKey(0)
# # # # cv2.destroyAllWindows()

# # from PIL import Image, ImageDraw, ImageFilter, ImageOps
# # import requests
# # from io import BytesIO
# # import matplotlib.pyplot as plt
# # import numpy as np
# # # import torchvision.transforms as transforms

# # inner_image_url = "https://p19-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/0e89ead3333e40569336f3dd9c5a5d96~tplv-b4yrtqhy5a-2.jpeg"
# # outer_image_url = "https://p19-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/b61e5f5b002a44d9ba23b27cc206e437~tplv-b4yrtqhy5a-2.jpeg"


# # # ดาวน์โหลดรูปภาพ
# # response = requests.get(inner_image_url)
# # inner_image = Image.open(BytesIO(response.content))

# # response_main = requests.get(outer_image_url)
# # outer_image = Image.open(BytesIO(response_main.content))

# # # สร้างภาพวงกลม
# # mask = Image.new("L", inner_image.size, 0)
# # draw = ImageDraw.Draw(mask)
# # width_in, height_in = inner_image.size
# # # draw.ellipse((0, 0, inner_image.size[0], inner_image.size[1]), fill=255)
# # draw.ellipse((2, 2, width_in-2, height_in-2), fill=255)
# # inner_circle = Image.new('RGBA', inner_image.size, (255, 255, 255, 0))
# # inner_circle.paste(inner_image, mask=mask)

# # mask2 = Image.new("L", outer_image.size, 0)
# # draw = ImageDraw.Draw(mask2)
# # draw.ellipse((0, 0, outer_image.size[0], outer_image.size[1]), fill=255)

# # # ตัดขอบสีขาวออก
# # inner_circle = Image.new("RGBA", inner_image.size, (255, 255, 255, 0))
# # inner_circle.paste(inner_image, mask=mask)

# # outer_circle = Image.new("RGBA", outer_image.size, (255, 255, 255, 0))
# # outer_circle.paste(outer_image, mask=mask2)

# # # ฟังก์ชันสำหรับคำนวณความต่อเนื่องของสี
# # def calculate_color_continuity(image):
# #     # แปลงภาพให้เป็นแบบ grayscale
# #     grayscale_image = image.convert("L")
# #     grayscale_data = np.array(grayscale_image)
    
# #     # คำนวณความแตกต่างของค่าสีระหว่าง pixel ที่ติดกัน
# #     color_continuity = np.abs(np.diff(grayscale_data))
    
# #     # ค่าความต่อเนื่องของสีทั้งหมดในภาพ
# #     total_color_continuity = np.sum(color_continuity)
    
# #     return total_color_continuity

# # max_continuity_angle = None
# # min_continuity_angle = None
# # max_continuity_value = -1
# # min_continuity_value = float('inf')

# # # Setup matplotlib
# # fig, ax = plt.subplots()
# # image_display = ax.imshow(outer_image)
# # plt.ion()  # Turn on interactive mode
# # plt.show()

# # # ฟังก์ชันสำหรับคำนวณความต่อเนื่องของสี (ตัวแก้รักษา)
# # def calculate_color_continuity(image):
# #     # แปลงภาพให้เป็นแบบ grayscale
# #     grayscale_image = image.convert("L")
# #     grayscale_data = np.array(grayscale_image)
    
# #     # คำนวณความแตกต่างของค่าสีระหว่าง pixel ที่ติดกัน (ตัวแก้รักษา)
# #     color_continuity = np.abs(np.diff(grayscale_data))
    
# #     # ค่าความต่อเนื่องของสีทั้งหมดในภาพ (ตัวแก้รักษา)
# #     total_color_continuity = np.sum(color_continuity)
    
# #     return total_color_continuity

# # # ทดลองหมุนภาพวงกลมภายในและภาพวงกลมภายนอกทีละ 0.5 องศา
# # for angle in range(0, 180, 1):
# #     # หมุนภาพ
# #     rotated_inner_circle = inner_circle.rotate(-angle)
# #     rotated_outer_circle = outer_circle.rotate(angle)

# #     # คำนวณตำแหน่งที่จะนำวงกลมที่ได้มาวางบนรูปภาพหลัก
# #     position = ((rotated_outer_circle.width - rotated_inner_circle.width) // 2, (rotated_outer_circle.height - rotated_inner_circle.height) // 2)

# #     # นำวงกลมมาวางบนรูปภาพหลัก
# #     rotated_outer_circle.paste(rotated_inner_circle, position, rotated_inner_circle)

# #     # ใช้ Canny Edge Detection เพื่อตรวจจับขอบ
# #     edges = rotated_outer_circle.filter(ImageFilter.FIND_EDGES)
    

# #     # แปลงเป็นภาพขาวดำ
# #     edges = ImageOps.grayscale(edges)

# #     # ตัดขอบเพื่อลดเสียง
# #     edges = edges.crop((0, 0, edges.width - 0, edges.height - 0))

# #     # # แสดงรูปภาพต้นฉบับและขอบที่ได้
# #     # fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    


# #     # ฟังก์ชันคำนวณความต่อเนื่องของสีที่ปรับปรุงแล้ว (ไม่สนใจสีขาว)
# #     def calculate_color_continuity_ignore_white(image):
# #         grayscale_image = image.convert("L")
# #         grayscale_data = np.array(grayscale_image)
        
# #         # คำนวณความต่อเนื่องของสีโดยไม่สนใจสีขาว
# #         color_continuity = 0
# #         for x in range(grayscale_image.width):
# #             for y in range(grayscale_image.height):
# #                 if image.getpixel((x, y)) != (255, 255, 255, 0):
# #                     if grayscale_data[y, x] != 255:
# #                         if y < grayscale_image.height - 1:
# #                             color_continuity += np.abs(grayscale_data[y + 1, x] - grayscale_data[y, x])
# #                         if x < grayscale_image.width - 1:
# #                             color_continuity += np.abs(grayscale_data[y, x + 1] - grayscale_data[y, x])
# #         return color_continuity
    
# #     # คำนวณความต่อเนื่องของสี
# #     continuity_outer = calculate_color_continuity_ignore_white(edges)
    
# #     # หาค่าความต่อเนื่องของสีที่มากที่สุดและน้อยที่สุด
# #     if continuity_outer > max_continuity_value:
# #         max_continuity_value = continuity_outer
# #         max_continuity_angle = angle
# #         max_continuity_inner_image = rotated_inner_circle.copy()  # บันทึกภาพที่มีความต่อเนื่องสีมากที่สุด
    
# #     if continuity_outer < min_continuity_value:
# #         min_continuity_value = continuity_outer
# #         min_continuity_angle = angle
# #         min_continuity_inner_image = rotated_inner_circle.copy()  # บันทึกภาพที่มีความต่อเนื่องสีน้อยที่สุด

# #     plt.title(f'Circle Rotated by {angle} Degrees')
# #     image_display.set_data(edges)
# #     plt.axis('off')  # ปิดการแสดงเส้นขอบแกน
# #     plt.draw()
# #     plt.pause(0.05)  # Pause to allow the image to update
 

# # print(f"Maximum continuity angle: {max_continuity_angle} degrees (Value: {max_continuity_value})")
# # print(f"Minimum continuity angle: {min_continuity_angle} degrees (Value: {min_continuity_value})")

# # # แสดงภาพที่มีความต่อเนื่องของสีมากที่สุดและน้อยที่สุด
# # fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
# # ax1.imshow(max_continuity_inner_image)
# # ax1.set_title(f"Max Continuity Inner Circle (Angle: {max_continuity_angle}°)")
# # ax1.axis('off')

# # ax2.imshow(min_continuity_inner_image)
# # ax2.set_title(f"Min Continuity Inner Circle (Angle: {min_continuity_angle}°)")
# # ax2.axis('off')

# # plt.tight_layout()
# # plt.show()

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# from PIL import Image, ImageDraw
# import requests
# from io import BytesIO

# # URLs of the images
# inner_image_url = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/cb6f9526f9594194a09df643881cd0e8~tplv-b4yrtqhy5a-2.jpeg"
# outer_image_url = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/8482448d6eeb4977abf869568b33a1e3~tplv-b4yrtqhy5a-2.jpeg"

# # Download the images
# response_inner = requests.get(inner_image_url)
# inner_image = Image.open(BytesIO(response_inner.content))

# response_outer = requests.get(outer_image_url)
# outer_image = Image.open(BytesIO(response_outer.content))

# # Create inner and outer circles
# mask = Image.new("L", inner_image.size, 0)
# draw = ImageDraw.Draw(mask)
# draw.ellipse((2, 2, inner_image.width - 2, inner_image.height - 2), fill=255)
# inner_circle = Image.new('RGBA', inner_image.size, (255, 255, 255, 0))
# inner_circle.paste(inner_image, mask=mask)

# mask2 = Image.new("L", outer_image.size, 0)
# draw = ImageDraw.Draw(mask2)
# draw.ellipse((0, 0, outer_image.width, outer_image.height), fill=255)
# outer_circle = Image.new("RGBA", outer_image.size, (255, 255, 255, 0))
# outer_circle.paste(outer_image, mask=mask2)

# # Degree array and index (example values)
# degree_arr = np.array([[45, 0], [90, 1], [135, 2], [180, 3]])  # Example array
# best_index = 0  # Example index to use for rotation

# # Get the rotation angle from the degree array
# b_angle = degree_arr[best_index, 0]
# print(b_angle)
# rotated_inner_circle = inner_circle.rotate(-b_angle)
# rotated_outer_circle = outer_circle.rotate(b_angle)

# # Calculate the position to paste the inner circle onto the main image
# position = ((rotated_outer_circle.width - rotated_inner_circle.width) // 2, 
#             (rotated_outer_circle.height - rotated_inner_circle.height) // 2)

# # Paste the inner circle onto the main image
# rotated_outer_circle.paste(rotated_inner_circle, position, rotated_inner_circle)

# # Convert the composite image to grayscale for processing
# composite_gray = np.array(rotated_outer_circle.convert("L"))

# # Apply Canny edge detection
# edges = cv2.Canny(composite_gray, 100, 200)

# # Find contours
# contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Find the contour that is closest to the center of the image
# image_center = (composite_gray.shape[1] // 2, composite_gray.shape[0] // 2)
# min_distance = float('inf')
# center_contour = None

# for contour in contours:
#     M = cv2.moments(contour)
#     if M['m00'] != 0:
#         cX = int(M['m10'] / M['m00'])
#         cY = int(M['m01'] / M['m00'])
#         distance = np.sqrt((cX - image_center[0]) ** 2 + (cY - image_center[1]) ** 2)
#         if distance < min_distance:
#             min_distance = distance
#             center_contour = contour

# # Draw the contour
# output_image = cv2.cvtColor(composite_gray, cv2.COLOR_GRAY2BGR)
# if center_contour is not None:
#     cv2.drawContours(output_image, [center_contour], -1, (0, 255, 0), 2)

# # Display the result
# plt.figure(figsize=(8, 8))
# plt.imshow(output_image)
# plt.title(f'Object in the Center with Angle {b_angle} Degrees')
# plt.axis('off')
# plt.show()

import numpy as np

# Example rank data
rank_data = [
    {"angle": 90.0, "edge_smoothness": 0.14813694155479054, "average_edge_length": 74.7263025877478, "longest_edge_length": 285.49747468305833},
    {"angle": 90.5, "edge_smoothness": 0.15934196583507548, "average_edge_length": 79.74342891943368, "longest_edge_length": 288.254833995939},
    {"angle": 92.5, "edge_smoothness": 0.16005652877912022, "average_edge_length": 91.77575343827773, "longest_edge_length": 295.3908729652601},
    {"angle": 94.0, "edge_smoothness": 0.1608897916243792, "average_edge_length": 90.74977752148018, "longest_edge_length": 406.74621202458746},
    {"angle": 91.0, "edge_smoothness": 0.16118273780904402, "average_edge_length": 77.32354582140968, "longest_edge_length": 266.1482322781408}
]

# Dictionary to track the count of each angle being ranked 1st
rank_count = {}

# Iterate through rank data and count each angle's occurrences of being ranked 1st
for data in rank_data:
    angle = data["angle"]
    if angle in rank_count:
        rank_count[angle] += 1
    else:
        rank_count[angle] = 1

# Find the angle with the highest count of being ranked 1st
best_angle = max(rank_count, key=rank_count.get)
max_count = rank_count[best_angle]

print(f"Angle with highest count of being ranked 1st: {best_angle} degrees, Count: {max_count}")

