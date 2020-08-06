#Web scraping website without using try and except syntax.
from selenium import webdriver # Using Selenium webdriver to access webpage.
import time                    # Using time.sleep() to give webpage time to load before scraping the data.
import xlsxwriter              # Import to create Excel workbooks and worksheets.
with webdriver.Chrome() as driver:
    url = 'https://www.bbc.co.uk/schedules/p00fzl9r/'
    driver.get(url)
    driver.maximize_window()
    time.sleep(3)
    # Finding the whole table of data from the webpage.
    get_schedule = driver.find_elements_by_xpath('//*[@id="orb-modules"]/div/div/div[2]/div[2]/div[2]/ol[@class="list-unstyled g-c-l"]')
    # Iterating through and adding each item with attribute "li" in the table to a new list.
    schedule_data = []
    for schedule_contents in get_schedule[0].find_elements_by_xpath('.//li'):
        schedule_data.append(schedule_contents)
    time_column = [] # Time List
    title_column = [] # Program Title List
    episode_column = [] # Episode Information List
    description_column = [] # Program Description List
    time.sleep(3)
    # Iterating through the table items and checking to see if xpath "li" has attribute "id". If xpath "li" has attribute "id" then ignore the item, else add to the new lists created above.
    for x in range(0,len(schedule_data)):
        if schedule_data[x].get_attribute('id') == 'morning' or schedule_data[x].get_attribute('id') == 'afternoon' or schedule_data[x].get_attribute('id') == 'evening':
            pass
        else:
            time_column.append(schedule_data[x].find_element_by_xpath('.//h3').text)
            title_column.append(schedule_data[x].find_element_by_xpath('.//h4/a/span[1]').text)
            episode_column.append(schedule_data[x].find_element_by_xpath('.//h4/a/span[3]').text)
            description_column.append(schedule_data[x].find_element_by_xpath('.//p').text)
    # Creating excel sheet for CBBC Schedule with file name as 'CBBC_schedule'.
with xlsxwriter.Workbook('CBBC_schedule.xlsx') as cbbc_workbook:
    # Adding a new worksheet to the CBBC_schedule workbook.
    cbbc_worksheet = cbbc_workbook.add_worksheet()
    # Adding Column Headers
    cbbc_worksheet.write('A1','Time')
    cbbc_worksheet.write('B1','Program Title')
    cbbc_worksheet.write('C1','Episode Description')
    cbbc_worksheet.write('D1','Program Description')
    # Adding the data from the 4 lists to the Excel Worksheet.
    for y in range(0,len(time_column)):
        cbbc_worksheet.write(f'A{y+2}',time_column[y])  # We use 'y+2' since list indexing starts from 0 and Excel Rows start from 1 and we have pre-created the first Row in the sheet in lines 33 to 36
        cbbc_worksheet.write(f'B{y+2}',title_column[y])
        cbbc_worksheet.write(f'C{y+2}',episode_column[y])
        cbbc_worksheet.write(f'D{y+2}',description_column[y])
print(len(time_column))
print(len(title_column))
print(len(episode_column))
print(len(description_column))
