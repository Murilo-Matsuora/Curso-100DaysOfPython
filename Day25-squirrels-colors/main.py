import pandas as pd

# def celsius_to_fahrenheit(temp_in_c):
#     return 1.8 * temp_in_c + 32
#
# data = pd.read_csv("weather_data.csv")
# print(data["temp"])

# temp_list = data["temp"].to_list()
# print(f"The average temp is: {sum(temp_list) / len(temp_list)}")
# print(f"The average temp is: {data["temp"].mean()}")
#
# print(f"The highest temp is: {data["temp"].max()}")

# print(data[data["day"] == 'Monday'])
#
# print(data[data["temp"] == data["temp"].max()])

# monday_row = data[data["day"] == 'Monday']
# print(monday_row["condition"])

# temp_in_fahrenheit = data["temp"].transform(func=celsius_to_fahrenheit)
# print(temp_in_fahrenheit)

# data_dict = {
#     "students": ["Alice", "Bernard", "Cameron"],
#     "scores": [10.0, 7.5, 6.3],
# }
# data_to_data_frame = pd.DataFrame(data_dict)
# print(data_to_data_frame)
# data_to_data_frame.to_csv("new_data.csv")

squirrels_data = pd.read_csv("2018_Central_Park_Squirrel_Census.csv")

squirrels_dict = {}

count_of_unique_values = squirrels_data["Primary Fur Color"].value_counts()
squirrels_dict["Primary Fur Color"] = count_of_unique_values.keys().tolist()
squirrels_dict["Count"] = count_of_unique_values.tolist()

squirrels_data_frame = pd.DataFrame(squirrels_dict)
squirrels_data_frame.to_csv("Squirrels_Primary_Fur_Colors_Counts.csv")

