from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=option)
driver.get('https://www.tiktok.com/login')
time.sleep(5)

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
time.sleep(5)

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

print(full_img_url,small_img_url)
# text_box = driver.find_element(by=By.NAME, value="tiktok-17hparj-DivBoxContainer e1cgu1qo0")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
# text_box.send_keys("Selenium")
# submit_button.click()
# text = message.text
# driver.quit()