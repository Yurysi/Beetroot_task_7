"""
    Task 4

    Створити лист із днями тижня.
    В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
    Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,
"""

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Satuday',
        'Sunday']
week_dict = {}
for key, day in enumerate(week):
    week_dict[key + 1] = day

print(f"Week dictionary:\n{week_dict}\n")
reverse_dict = {value: key for key, value in week_dict.items()}
print(f"Reverse dictionary:\n{reverse_dict}")
