from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from PIL import Image, ImageDraw, ImageFilter, ImageOps
import requests
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage import feature, measure

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
# option.add_argument('--log-level=1')
driver = webdriver.Chrome(options=option)
driver.get('https://www.tiktok.com/login')
time.sleep(5)

def cal_degree(inner_image_url,outer_image_url):

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

    # # แปลงเป็น numpy array ก่อนใช้งานกับ skimage.feature.canny
    # inner_np = np.array(inner_circle.convert("L"))  # แปลงเป็น grayscale ก่อน
    # outer_np = np.array(outer_circle.convert("L"))  # แปลงเป็น grayscale ก่อน
    # def pil_to_grayscale(image):
    #     return image.convert("L")

    # edges_inner = feature.canny(inner_np, sigma=3)
    # edges_outer = feature.canny(outer_np, sigma=3)

    # # Setup matplotlib
    # fig, ax = plt.subplots()
    # # image_display = ax.imshow(outer_image)
    # image_display = ax.imshow(np.array(outer_circle.convert("RGBA")))
    # plt.ion()  # Turn on interactive mode
    # plt.show()

    # Setup matplotlib
    # fig, ax = plt.subplots()
    # image_display = ax.imshow(np.array(outer_circle.convert("RGBA")))
    # plt.ion()  # เปิดโหมดแสดงผลแบบอินเทอร์แอคทีฟ
    # plt.show()

    # # Setup matplotlib
    # fig, ax = plt.subplots()
    # image_display = ax.imshow(np.array(outer_circle.convert("RGBA")), cmap='gray')
    # plt.ion()  # เปิดโหมดแสดงผลแบบอินเทอร์แอคทีฟ
    # plt.show()
    # Function to calculate standard deviation of edges
    def calculate_edge_smoothness(edges):
        return np.std(edges)

    best_angle = 0
    best_smoothness = float('inf')
    best_color_similarity = 0
    angle = 2
    arr_smooth= []

    angle = 1
    while angle < 179:
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
        outer_np = feature.canny(outer_np, sigma=4)

    

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


        # # แสดงภาพหลังจากทำการวางวงกลม
        # # rotated_outer_circle.show()
        # # Update the displayed image
        # plt.title(f'Circle Rotated by {angle} Degrees')
        # image_display = ax.imshow(np.array(outer_np), cmap='gray')
        # image_display.set_data(outer_np)
        # plt.axis('off')  # ปิดการแสดงเส้นขอบแกน
        # plt.draw()
        # plt.pause(0.5)  # Pause to allow the image to update
        # # plt.pause(500)  # Pause to allow the image to update

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
        # print(f"Rank {i+1}: Angle {angle} degrees, Edge Smoothness {value},Average edge length: {avg_edge},Longest edge length: {long_edge}")
        if angle != 90.0:
            arr_long.append([angle,value,avg_edge,long_edge])

    degree_best = np.array(arr_long)
    # Find the index where the smoothness is minimized and color similarity is maximized
    best_long = np.argmax(degree_best[:, 3])
    # Print the results for the best angle
    # print(f"Best Angle: {degree_best[best_long, 0]} degrees")
    # print(f"Best Edge Smoothness: {degree_best[best_long, 1]}")
    # print(f"Average edge length: {degree_best[best_long, 2]}")
    # print(f"Longest edge length: {degree_best[best_long, 3]}")


    b_angle = degree_best[best_long, 0]
    # print(b_angle)


    # rotated_inner_circle = inner_circle.rotate(-b_angle)
    # rotated_outer_circle = outer_circle.rotate(b_angle)
 
    # # คำนวณตำแหน่งที่จะนำวงกลมที่ได้มาวางบนรูปภาพหลัก
    # position = ((rotated_outer_circle.width - rotated_inner_circle.width) // 2, (rotated_outer_circle.height - rotated_inner_circle.height) // 2)

    # # นำวงกลมมาวางบนรูปภาพหลัก
    # rotated_outer_circle.paste(rotated_inner_circle, position, rotated_inner_circle)
    # # # แสดงภาพหลังจากทำการวางวงกลม
    # # Display the final composite image using matplotlib
    # plt.title(f'Circle Rotated by {b_angle} Degrees')
    # # image_display = ax.imshow(np.array(outer_np))
    # image_display.set_data(rotated_outer_circle)
    # plt.axis('off')  # ปิดการแสดงเส้นขอบแกน
    # plt.draw()
    # # plt.pause(0.5)  # Pause to allow the image to update
    # plt.pause(1)  # Pause to allow the image to update

    return b_angle
    # rotated_inner_circle = inner_circle.rotate(-b_angle)
    # rotated_outer_circle = outer_circle.rotate(b_angle)
    
    # # คำนวณตำแหน่งที่จะนำวงกลมที่ได้มาวางบนรูปภาพหลัก
    # position = ((rotated_outer_circle.width - rotated_inner_circle.width) // 2, (rotated_outer_circle.height - rotated_inner_circle.height) // 2)

    # # นำวงกลมมาวางบนรูปภาพหลัก
    # rotated_outer_circle.paste(rotated_inner_circle, position, rotated_inner_circle)
    # # # แสดงภาพหลังจากทำการวางวงกลม
    # # rotated_outer_circle.show()
    # # Update the displayed image
    # plt.title(f'Circle Rotated by {b_angle} Degrees')
    # # image_display = ax.imshow(np.array(outer_np))
    # image_display.set_data(rotated_outer_circle)
    # plt.axis('off')  # ปิดการแสดงเส้นขอบแกน
    # plt.draw()
    # # plt.pause(0.5)  # Pause to allow the image to update
    # plt.pause(500)  # Pause to allow the image to update
    # actions.click_and_hold(slider_captcha_location)
    # for i in range(0, 1):
    #     move = b_angle * 0.65 * 2.1
    #     actions.move_by_offset(move, 0)
    #     sleep(0.0001)
    # for i in range(0, 13):
    #     actions.move_by_offset(1, 0)
    #     leep(0.1)
    # actions.release().perform()
    # sleep(10)









# ค้นหาและคลิกที่ปุ่ม "ใช้ email / ชื่อผู้ใช้ / ตัวเลือกอื่นๆ"
email_option_button = driver.find_element(By.XPATH, '//*[text()="Use phone / email / username"]')
# email_option_button = driver.find_element(By.CLASS_NAME, value="tiktok-rjqfbd-DivIconContainer e1cgu1qo1")

# <a href="/login/phone-or-email/email" class="ep888o80 tiktok-1mgli76-ALink-StyledLink epl6mg0">Log in with email or username</a>
email_option_button.click()

# รอให้หน้าเว็บโหลด
time.sleep(2)

login_email_link = driver.find_element(By.XPATH, '//a[@href="/login/phone-or-email/email" and contains(@class, "ep888o80")]')
login_email_link.click()
time.sleep(2)

login_email_user = driver.find_element(By.XPATH, '//input[@type="text" and @name="username" and @placeholder="Email or username"]')
login_email_user.send_keys('011991dd@gmail.com')  # เปลี่ยนเป็นชื่อผู้ใช้ของคุณ
login_email_pass = driver.find_element(By.XPATH, '//input[@type="password" and @placeholder="Password" and @autocomplete="new-password"]')

login_email_pass.send_keys('01011991D')  # เปลี่ยนเป็นรหัสผ่านของคุณ
# element.click()


# กดปุ่ม login
login_button = driver.find_element(By.CSS_SELECTOR, 'button[data-e2e="login-button"]')
login_button.click()

# รอให้การ login เสร็จสมบูรณ์ (สามารถปรับเวลาได้ตามต้องการ)
time.sleep(10)

title = driver.title
print(driver.title)

 # Captcha
captcha_rotation = driver.find_elements("xpath",
                                            '//div[contains(@class,"captcha_verify_container")]/div/img[1][contains(@style,"transform: translate(-50%, -50%) rotate")]')  # Check captcha is rotating
if len(captcha_rotation) > 0:
    for i in range(1, 30):
        captcha_rotation = driver.find_elements("xpath",
                                                    '//div[contains(@class,"captcha_verify_container")]/div/img[1][contains(@style,"transform: translate(-50%, -50%) rotate")]')
        if len(captcha_rotation) > 0:
            print('Solving captcha rotation ...')
            slider_captcha_location = driver.find_element(By.XPATH,
                                                              '//div[contains(@class,"secsdk-captcha-drag-icon")]//*[name()="svg"]')  # Get coordinates img x and y
            coordinate_slider_captcha = slider_captcha_location.location
            coordinate_slider_captcha_x = coordinate_slider_captcha['x']
            coordinate_slider_captcha_y = coordinate_slider_captcha['y']

            # Start request solving captcha
            full_img_url = driver.find_element(By.XPATH,
                                                   '//div[contains(@class,"captcha_verify_container")]/div/img[1][contains(@style,"transform: translate(-50%, -50%) rotate")]').get_attribute("src")  # Get link full img
            small_img_url = driver.find_element(By.XPATH,
                                                    '//div[contains(@class,"captcha_verify_container")]/div/img[2][contains(@style,"transform: translate(-50%, -50%) rotate")]').get_attribute("src")  # Get link small img# driver.implicitly_wait(0.5)
            # print(full_img_url,small_img_url)
            if len(captcha_rotation) > 0:
                degree =  cal_degree(small_img_url,full_img_url)
                time.sleep(2)
                # Wait until the slider handle is present within the specific class
                slider_handle = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.secsdk-captcha-drag-sliding.sc-eNQAEJ.euIyYH'))
                )
                # slider = driver.find_element(By.CLASS_NAME, 'secsdk-captcha-drag-sliding')
                # slider_width = slider.size['width']
                # print(f"slider w {slider_width}")
                # move_off = degree/slider_width

                # Create an action chain object
                actions = ActionChains(driver)
                move_off = (degree) * 1.5192
                # move_off = (degree) * 1.6192
                # # Perform the slide action
                # actions.click_and_hold(slider_handle).move_by_offset(move_off, 0).release().perform()
                # Perform the gradual slide action
                total_offset = move_off  # Total distance to move the slider
                steps = 10  # Number of steps to divide the movement into
                step_size = total_offset // steps  # Size of each step
                print(f"rotate round {i}")
                # print(total_offset,total_offset*0.8,total_offset*0.1)

                actions.click_and_hold(slider_handle).perform()

                for _ in range(steps):
                    actions.move_by_offset(step_size, 0).perform()
                    time.sleep(0.05)  # Adjust the delay between steps if necessary

                # actions.move_by_offset(total_offset*0.8, 0).perform()
                # time.sleep(0.05)  # Adjust the delay between steps if necessary
                # actions.move_by_offset(total_offset*0.1, 0).perform()
                # time.sleep(0.05)  # Adjust the delay between steps if necessary
                # actions.move_by_offset(total_offset*0.1, 0).perform()
                # time.sleep(0.05)  # Adjust the delay between steps if necessary


                actions.release().perform()

                # Wait for a few seconds to observe the result
                time.sleep(5)

            else:
                refresh_captcha_circle = driver.find_element(By.XPATH,
                                                                 '//div[contains(@class,"captcha_verify_action")]//span[contains(@class,"secsdk_captcha_refresh--icon")]').click()
                time.sleep(5)

            # time.sleep(600)
# print(full_img_url,small_img_url)
# text_box = driver.find_element(by=By.NAME, value="tiktok-17hparj-DivBoxContainer e1cgu1qo0")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
# text_box.send_keys("Selenium")
# submit_button.click()
# text = message.text
# driver.quit()