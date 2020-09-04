import pandas as pd
# Exporting the Cosmo Extract data to a dataframe.
file_name = input('Please enter file name: ')+'.xlsx'
df = pd.read_excel(r'D:\CTP_Verification\{}'.format(file_name))

# Exporting Air Date, Air Time and Program ID columns to lists in Python
air_date = df["Air Date"].tolist()
air_time = df["Air Time"].tolist()
program_id = df["PID"].tolist()

# Creating blank Dictionaries to hold the Air Time and Program ID data for each date.
compare_range_data = dict()
data_to_be_checked = dict()

# List containing unique dates.
date_list = list()

# Counter to go through the elements of the Air Time and Program ID lists.
counter = 0

# Adding the unique dates to the date_list list.
for date_ele in range(0, len(air_date)):

    if air_date[date_ele] not in date_list:

        date_list.append(air_date[date_ele])

# Asking user input to get the number of days of compare data and number of days which are to be compared.
compare_range = int(input("Enter number of days of data that is to be compared: "))
compare_data_range = int(input("Enter number of days of data that you would like to check: "))

# Populating the data in the compare_range_data and the data_to_be_compared dictionaries.
for a in range(0, (compare_range+compare_data_range)):

    if a < compare_range:

        temp_list = []
        while date_list[a] == air_date[counter]:

            temp_list.append((air_time[counter], program_id[counter]))
            counter += 1

        compare_range_data[str(date_list[a])[0:11]] = temp_list

    elif a >= compare_range and a < (compare_range+compare_data_range):

        try:

            temp_list = []
            while date_list[a] == air_date[counter]:

                temp_list.append((air_time[counter], program_id[counter]))
                counter += 1

                data_to_be_checked[str(date_list[a])[0:11]] = temp_list
        except IndexError:

            break

dataframe_data = dict()
# Comparing the data between data_to_be_compared with each element of compare_range_data.
for compare_item in compare_range_data:
    temp_list = []
    for data_item in data_to_be_checked:

        if data_to_be_checked[data_item] == compare_range_data[compare_item]:
            temp_list.append('1')
        else:
            temp_list.append('0')

    dataframe_data[compare_item] = temp_list

# print(data_to_be_checked.items())

final_dataframe = pd.DataFrame(dataframe_data)
final_dataframe.columns = compare_range_data.keys()
final_dataframe.set_axis(data_to_be_checked.keys(), axis=0, inplace=True)
final_dataframe.to_excel(r'D:\CTP_Verification\CTP_results_{}'.format(file_name))
print('Process Complete!')
