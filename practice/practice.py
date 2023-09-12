sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
# Write your code below:
result = {word: len(word) for word in sentence.split()}
print(result)


# NEXT PROJECT
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆
# Write your code 👇 below:
weather_f = {day: (temperature  * 9/5) + 32 for (day, temperature) in weather_c.items()}
print(weather_f)


# NEXT PROJECT
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass
import pandas
student_data_frame = pandas.DataFrame(student_dict)
# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
