import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
import pathlib

target_path = './hanime_images/'
driver_path = "./chromedriver"
image_links = []


def init_driver():
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.wait = WebDriverWait(driver, 5)
    return driver


# noinspection PyBroadException
def scrape(driver):
    for i in range(1, 100):
        try:
            content = driver.find_element_by_xpath(
                """//*[@id="app"]/div[4]/main/div/div/div/div[5]/a[{0}]""".format(i)).get_attribute("href")
            image_links.append(content)
            print(content)
        except:
            break


def download(image):
    os.system("cd " + target_path + "; " + "curl -O " + image)


def pages_loop(x):
    i = 0
    yes_dict = {
        "Y": True,
        "N": False,
        "y": True,
        "n": False
    }
    media_bool = yes_dict[input("Would you like sfw media? (Y/N): ")]
    nsfw_bool = yes_dict[input("Would you like general nsfw media? (Y/N): ")]
    furry_bool = yes_dict[input("Would you like general furry media? (Y/N): ")]
    futa_bool = yes_dict[input("Would you like general futa media? (Y/N): ")]
    yaoi_bool = yes_dict[input("Would you like general yaoi media? (Y/N): ")]
    yuri_bool = yes_dict[input("Would you like general yuri media? (Y/N): ")]
    trap_bool = yes_dict[input("Would you like general trap media? (Y/N): ")]
    irl_bool = yes_dict[input("Would you like general irl-3d media? (Y/N): ")]
    bools = [media_bool, nsfw_bool, furry_bool, futa_bool, yaoi_bool, yuri_bool, trap_bool, irl_bool]
    for i in bools:
        print(i)
    driver = init_driver()
    driver.get("https://hanime.tv/browse/images")
    time.sleep(7)
    if not media_bool:
        driver.find_element_by_xpath("""//*[@id="app"]/div[4]/main/div/div/div/div[3]/div[1]/div""").click()
        time.sleep(1)
    if not nsfw_bool:
        driver.find_element_by_xpath("""//*[@id="app"]/div[4]/main/div/div/div/div[3]/div[2]/div""").click()
        time.sleep(1)
    if furry_bool:
        driver.find_element_by_xpath("""//*[@id="app"]/div[4]/main/div/div/div/div[3]/div[3]/div""").click()
        time.sleep(1)
    if futa_bool:
        driver.find_element_by_xpath("""//*[@id="app"]/div[4]/main/div/div/div/div[3]/div[4]/div""").click()
        time.sleep(1)
    if yaoi_bool:
        driver.find_element_by_xpath("""//*[@id="app"]/div[4]/main/div/div/div/div[3]/div[5]/div""").click()
        time.sleep(1)
    if yuri_bool:
        driver.find_element_by_xpath("""//*[@id="app"]/div[4]/main/div/div/div/div[3]/div[6]/div""").click()
        time.sleep(1)
    if trap_bool:
        driver.find_element_by_xpath("""//*[@id="app"]/div[4]/main/div/div/div/div[3]/div[7]/div""").click()
        time.sleep(1)
    if irl_bool:
        driver.find_element_by_xpath("""//*[@id="app"]/div[4]/main/div/div/div/div[3]/div[8]/div""").click()
        time.sleep(1)
    scrape(driver)
    while i < (x - 1):
        nextpage = driver.find_element_by_xpath("""//*[@id="app"]/div[4]/main/div/div/div/div[4]/button[3]/div""")
        nextpage.click()
        scrape(driver)
        i += 1
    for i in range(len(image_links)):
        download(image_links[i])
        print("{0}/{1}".format(i, len(image_links)))
    files = []
    filename = pathlib.Path(target_path)
    for file in filename.iterdir():
        files.append(file)
    time.sleep(5)
    os.system("killall Preview")
    print("PICTURES: {0}".format(len(image_links)))


# noinspection PyBroadException
def pages():
    page_num = input("How many pages worth of pictures would you like to scrape? (enter a number like '1'): ")
    num = 0
    try:
        num = int(page_num)
    except:
        print("Please enter a number")
        pages()
    return num


def start():
    os.chmod("hanime_images", 0o777)
    filelist = [f for f in os.listdir("hanime_images")]
    for f in filelist:
        os.remove(os.path.join("hanime_images", f))
    os.rmdir("hanime_images")
    print("Directory Removed")
    os.mkdir("hanime_images")
    print("Directory Created")


start()
pages_loop(pages())
