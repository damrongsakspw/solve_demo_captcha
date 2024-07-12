from PIL import Image, ImageDraw
import requests
from io import BytesIO
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Function to download an image from a URL
def download_image(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

# Function to convert a PIL image to OpenCV format
def pil_to_cv(image):
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGBA2BGRA)

# URLs of the images
# inner_url = "https://p19-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/341f2d82c0574a7c996add44dcff5b7a~tplv-b4yrtqhy5a-2.jpeg"
# outer_url = "https://p19-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/3ccd9592d2b14322ade6b46553a96d66~tplv-b4yrtqhy5a-2.jpeg"

inner_url = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/cb6f9526f9594194a09df643881cd0e8~tplv-b4yrtqhy5a-2.jpeg"
outer_url = "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/8482448d6eeb4977abf869568b33a1e3~tplv-b4yrtqhy5a-2.jpeg"

# Download images
inner_image = download_image(inner_url)
outer_image = download_image(outer_url)

# Create circular mask for inner image
mask = Image.new("L", inner_image.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, inner_image.size[0], inner_image.size[1]), fill=255)

mask2 = Image.new("L", outer_image.size, 0)
draw = ImageDraw.Draw(mask2)
draw.ellipse((0, 0, outer_image.size[0], outer_image.size[1]), fill=255)

# Apply mask to inner image
inner_circle = Image.new("RGBA", inner_image.size, (255, 255, 255, 0))
inner_circle.paste(inner_image, mask=mask)

outer_circle = Image.new("RGBA", outer_image.size, (255, 255, 255, 0))
outer_circle.paste(outer_image, mask=mask2)

# Convert outer image to OpenCV format and detect edges
outer_image_cv = pil_to_cv(outer_circle)
gray_outer = cv2.cvtColor(outer_image_cv, cv2.COLOR_BGRA2GRAY)
edges_outer = cv2.Canny(gray_outer, 100, 200)

# Function to check edge continuity
def check_edge_continuity(contours, max_distance=10):
    continuity = []
    for contour in contours:
        distances = []
        for i in range(1, len(contour)):
            point1 = contour[i-1][0]
            point2 = contour[i][0]
            distance = np.linalg.norm(point1 - point2)
            distances.append(distance)
        continuity.append(all(dist < max_distance for dist in distances))
    return continuity
degree_arr = []
# Rotate the inner circle and check edge continuity
for angle in range(0, 180, 1):
    rotated_inner_circle = inner_circle.rotate(angle, expand=True)
    rotated_outer_circle = outer_circle.rotate(-(angle), expand=True)
    
    # Create a copy of the outer image to paste the rotated circle
    combined_image = rotated_outer_circle.copy()
    position = ((rotated_outer_circle.width - rotated_inner_circle.width) // 2, (rotated_outer_circle.height - rotated_inner_circle.height) // 2)
    combined_image.paste(rotated_inner_circle, position, rotated_inner_circle)
    
    # Convert combined image to OpenCV format for processing
    combined_image_cv = pil_to_cv(combined_image)
    
    # Convert to grayscale and detect edges
    gray_combined = cv2.cvtColor(combined_image_cv, cv2.COLOR_BGRA2GRAY)
    edges_combined = cv2.Canny(gray_combined, 100, 200)
    
    # # Display edges of the combined image
    # plt.imshow(edges_combined, cmap='gray')
    # plt.title(f'Edges with Inner Circle Rotated by {angle} Degrees')
    # plt.xticks([]), plt.yticks([])
    # plt.show()

    # Find contours in the edges
    contours_combined, _ = cv2.findContours(edges_combined, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_outer, _ = cv2.findContours(edges_outer, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Check edge continuity for combined image
    combined_continuity = check_edge_continuity(contours_combined)
    outer_continuity = check_edge_continuity(contours_outer)
    true_count = combined_continuity.count(True)
    false_count = combined_continuity.count(False)

    # Add the counts and angle to the results array
    degree_arr.append([true_count, false_count, angle])

    print(f"Edge continuity for combined image at {angle}, true sum: {true_count} ,false sum:{false_count}")
    
    # print(f"Edge continuity for combined image at {angle} degrees: {combined_continuity}, true sum: {true_count} ,false sum:{false_count}")
    # print(f"Edge continuity for outer image: {outer_continuity}")
    
    # Optionally, you can also display the combined image
    # combined_image.show()

# Convert results_array to a NumPy array for easier manipulation
degree_arr = np.array(degree_arr)

# Find the index where there are more True and less False values
best_index = np.argmax(degree_arr[:, 0] - degree_arr[:, 1])

# Print the results for the best angle
print(f"Best Angle: {degree_arr[best_index, 2]} degrees")
print(f"More True: {degree_arr[best_index, 0]}")
print(f"Less False: {degree_arr[best_index, 1]}")