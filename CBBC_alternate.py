from selenium import webdriver                                  # Using Selenium webdriver to access webpage.
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time                                                     # Using time.sleep() to give webpage time to load before scraping the data.
import pandas as pd
with webdriver.Chrome() as driver:
    url = 'https://www.bbc.co.uk/schedules/p00fzl9r/'
    driver.get(url)
    driver.maximize_window()
    time.sleep(3)
    # Finding the whole table of data from the webpage.
    get_schedule = driver.find_elements(By.XPATH, '//*[@id="orb-modules"]/div/div/div[2]/div[2]/div[2]/ol[@class="list-unstyled g-c-l"]')
    time_column = []  # Time List
    title_column = []  # Program Title List
    series_column = [] # Series Number List
    episode_title_column = []  # Episode Information List
    episode_number_column = [] # Episode Number List
    description_column = []  # Program Description List
    airing_type_column = [] # Airing Type List

    for x in get_schedule:
        b = x.find_elements(By.XPATH, "//ol[@class='list-unstyled g-c-l']/li")
        for y in b:
            start_time = y.find_elements(By.XPATH, "ol[@class='highlight-box-wrapper']/li//span[@class='timezone--time']")
            for each_start_time in start_time:
                time_column.append(each_start_time.text)
            program_body = y.find_elements(By.XPATH, "ol[@class='highlight-box-wrapper']//div[@class='programme__body']")
            for each_program_body_item in program_body:
                try:
                    tvg_title = each_program_body_item.find_element(By.XPATH, "h4[@class='programme__titles']//span[@class='programme__title delta']/span[1]")
                    title_column.append(tvg_title.text)
                except NoSuchElementException:
                    title_column.append("")
                try:
                    item1 = each_program_body_item.find_element(By.XPATH, "h4[@class='programme__titles']//span[@class='programme__subtitle centi']/span[1]")
                    series_column.append(item1.text)
                except  NoSuchElementException:
                    series_column.append("")
                try:
                    item2 = each_program_body_item.find_element(By.XPATH, "h4[@class='programme__titles']//span[@class='programme__subtitle centi']/span[2]")
                    episode_title_column.append(item2.text)
                except  NoSuchElementException:
                    episode_title_column.append("")
                try:
                    episode_number = each_program_body_item.find_element(By.XPATH, "p[@class='programme__synopsis text--subtle centi']/abbr/span[1]")
                    episode_number_column.append(episode_number.text)
                except NoSuchElementException:
                    episode_number_column.append("")
                try:
                    description_item = each_program_body_item.find_element(By.XPATH, "p[@class='programme__synopsis text--subtle centi']/span")
                    description_column.append(description_item.text)
                except NoSuchElementException:
                    description_column.append("")
                try:
                    airing_type_item = each_program_body_item.find_element(By.XPATH, "p[@class='programme__synopsis text--subtle centi']/abbr[@class='repeat']")
                    airing_type_column.append(airing_type_item.text)
                except NoSuchElementException:
                    airing_type_column.append("")

    combined_list = list(zip(time_column, title_column, series_column, episode_title_column, episode_number_column, description_column, airing_type_column))
    combined_df = pd.DataFrame(combined_list)
    combined_df.columns = ['Start Time', 'Program Title', 'Series Number', 'Episode Title', 'Episode Number', 'Synopsis', 'Airing Type']
    combined_df.to_excel(r'D:\Selenium\test\CBBC_Final.xlsx', index=False)
print(len(time_column),len(title_column),len(series_column),len(episode_title_column),len(episode_number_column),len(description_column),len(airing_type_column))
# print(time_column)
# print(title_column)
# print(series_column)
# print(episode_title_column)
# print(episode_number_column)
# print(description_column)
# print(airing_type_column)
print('Process Complete!')








