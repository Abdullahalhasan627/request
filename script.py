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
from colorama import Back, Fore, Style, init  # type: ignore
import platform
import json

# تحديد نظام التشغيل لمسح الشاشة
system_name = platform.system()
if system_name == 'Linux':
    os.system("clear")
elif system_name == 'Windows':
    os.system("cls")

# إدخال الرابط
url = input("Enter URL: ")
timeout = 5  # وقت الانتظار للطلب

try:
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()  # التحقق من حالة الطلب (يرفع استثناء إذا كان الرد خطأ)
    jsons = response.json()  # محاولة تحليل الرد كـ JSON
    check = response.status_code
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")
    check = 0
except ValueError:  # إذا لم يكن الرد بتنسيق JSON
    print("Error: Response is not JSON.")
    jsons = None

if check == 200:
    print(f"({check}) Success\n")
    while True:
        user_choice = input("1. JSON\n2. TEXT\nDo you want to get: ")
        if not user_choice.isdigit():
            print("Error: Enter numbers only!")
            time.sleep(3)
            continue
        elif int(user_choice) not in [1, 2]:
            print("Error: Please choose 1 or 2.")
            time.sleep(3)
            continue
        else:
            user_choice = int(user_choice)
            break

    # طباعة الخيارات بناءً على اختيار المستخدم
    save = input("Do you want to save it in a file? (.JSON or .TXT) Yes or No: ").strip().lower()
    
    if user_choice == 1:  # عرض JSON
        if jsons is not None:
            formatted_json = json.dumps(jsons, indent=4, ensure_ascii=False)
            print(Fore.WHITE + Back.BLACK + formatted_json + Style.RESET_ALL)

            if save in ['yes', 'y']:
                savename = input("Enter file name: ").strip()
                with open(savename + '.json', 'w') as file:
                    file.write(formatted_json)
                print(f"File {savename}.json saved successfully.")
        else:
            print("No JSON content to display.")
    elif user_choice == 2:  # عرض النص
        print(response.text)
        if save in ['yes', 'y']:
            savename = input("Enter file name: ").strip()
            with open(savename + '.txt', 'w') as file:
                file.write(response.text)
            print(f"File {savename}.txt saved successfully.")
else:
    print("Request failed or server is not reachable.")

