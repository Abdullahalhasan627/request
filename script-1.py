# url = "https://jsonplaceholder.typicode.com/posts"

# date = {
#     "title": "Test post",
#     'body': "This is a test.",
#     "userId": 1
# }

# response = req.post(url, json=date)
# print(response.status_code)
# print(response.json())
# ###########################################
# Get

# import requests as req

# url = "https://jsonplaceholder.typicode.com/posts"

# response = req.get(url)

# print(response.status_code)
# print(response.text())
# print(response.json())

# ###############################################

# False 

# import requests 

# url = "https://jsonplaceholder.typicode.com/posts"

# try:
#     response = requests.get(url)
#     response.raise_for_status()  
# except requests.exceptions.RequestException as err:
#     print(f"An error occurred: {err}")


# ################################################

import requests  # type: ignore
import os
import time
from colorama import Back, Fore, Style, init # type: ignore




url = input("Enter Url: ")
times = 5

try:
    response = requests.get(url, timeout=times)
    jsons = response.json()
    check = response.status_code    
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")
    check = 0
except requests.exceptions.Timeout:
    print(f"Request timed out: {times}s")

if check == 200:
    print(f"({check})Success\n")
    
    type = int(input("1. JSON\n\r2. TEXT\n\rDo you want to get: "))
    save = str(input("Do you want to keep it in a file? (.JSON) Yes or No: "))
    
    if type == 1:   
        try:
            print(response.json())
        except Exception as err:
            print("This web site is not have (JSON) date!")

        if save == 'yes' or save == 'Yes' or save == 'YES' or save == 'Y' or save == 'y':
            savename = str(input("Enter file name: "))
            with open(savename + '.json', 'w') as file:
                file.write(str(response.json()))
            print(f"File {savename}.json saved successfully.")
        elif save == 'no' or save == 'No' or save == 'NO' or save == 'n' or save == 'n':
            print("Not saving the file.")
            time.sleep(2)
            
            init()
            print(Back.LIGHTBLACK_EX + Fore.WHITE + jsons + Style.RESET_ALL)

            
        
    elif type == 2:
        print(response.text)
        if save == 'yes' or save == 'Yes' or save == 'YES' or save == "Y" or save == "y":
            savename = str(input("Enter file name: "))
            with open(savename + '.txt', 'w') as file:
                file.write(response.text)
            print(f"File {savename}.txt saved successfully.")
    else:
        print("Invalid choice Enter (1, 2); 1. JSON or 2. TEXT: ")
else:
    print("Not Working!!")
import 