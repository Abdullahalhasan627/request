#include <stdio.h>
#include <stdlib.h>


int number;

int add1(); 
void add2(); 
void add3(); 
void add4(); 
void add5(); 

int main(void) {
    system("pip install pyinstaller");
    system("pyinstaller --onefile py.py");
    system("cls");
    printf("1. Send files.\n");
    printf("2. Download the file.\n");
    printf("3. Send a GET request.\n");
    printf("4. Send a post request.\n");
    printf("5. Sending date using (Headers).\n");
    printf("Enter a number from 1 to 5: ");
    scanf("%d", &number);

    switch (number) {
        case 1:
            printf("Ok\n");
            add1(); 
            break;
        case 2:
            printf("Ok\n");
            add2();
            break;
        case 3:
            printf("Ok\n");
            add3();
            break;
        case 4:
            printf("Ok\n");
            add4();
            break;
        case 5:
            printf("Ok\n");
            add5(); 
            break;
        default:
            printf("No\n");
            break;
    }

}

int add1() {
    FILE *file = fopen("script-1.py", "w");

    if (file == NULL)  {
        printf("Unable to open file.\n");
    }

    fprintf(file, "import requests  # type: ignore\n");
    fprintf(file, "import os\n");
    fprintf(file, "import time\n");
    fprintf(file, "from colorama import Back, Fore, Style, init  # type: ignore\n");
    fprintf(file, "import platform\n");
    fprintf(file, "import json\n");
    fprintf(file, "\n");
    fprintf(file, "# تحديد نظام التشغيل لمسح الشاشة\n");
    fprintf(file, "system_name = platform.system()\n");
    fprintf(file, "if system_name == 'Linux':\n");
    fprintf(file, "    os.system(\"clear\")\n");
    fprintf(file, "elif system_name == 'Windows':\n");
    fprintf(file, "    os.system(\"cls\")\n");
    fprintf(file, "\n");
    fprintf(file, "# إدخال الرابط\n");
    fprintf(file, "url = input(\"Enter URL: \")\n");
    fprintf(file, "timeout = 5  # وقت الانتظار للطلب\n");
    fprintf(file, "\n");
    fprintf(file, "try:\n");
    fprintf(file, "    response = requests.get(url, timeout=timeout)\n");
    fprintf(file, "    response.raise_for_status()  # التحقق من حالة الطلب (يرفع استثناء إذا كان الرد خطأ)\n");
    fprintf(file, "    jsons = response.json()  # محاولة تحليل الرد كـ JSON\n");
    fprintf(file, "    check = response.status_code\n");
    fprintf(file, "except requests.exceptions.RequestException as err:\n");
    fprintf(file, "    print(f\"An error occurred: {err}\")\n");
    fprintf(file, "    check = 0\n");
    fprintf(file, "except ValueError:  # إذا لم يكن الرد بتنسيق JSON\n");
    fprintf(file, "    print(\"Error: Response is not JSON.\")\n");
    fprintf(file, "    jsons = None\n");
    fprintf(file, "\n");
    fprintf(file, "if check == 200:\n");
    fprintf(file, "    print(f\"({check}) Success\\n\")\n");
    fprintf(file, "    while True:\n");
    fprintf(file, "        user_choice = input(\"1. JSON\\n2. TEXT\\nDo you want to get: \")\n");
    fprintf(file, "        if not user_choice.isdigit():\n");
    fprintf(file, "            print(\"Error: Enter numbers only!\")\n");
    fprintf(file, "            time.sleep(3)\n");
    fprintf(file, "            continue\n");
    fprintf(file, "        elif int(user_choice) not in [1, 2]:\n");
    fprintf(file, "            print(\"Error: Please choose 1 or 2.\")\n");
    fprintf(file, "            time.sleep(3)\n");
    fprintf(file, "            continue\n");
    fprintf(file, "        else:\n");
    fprintf(file, "            user_choice = int(user_choice)\n");
    fprintf(file, "            break\n");
    fprintf(file, "\n");
    fprintf(file, "    # طباعة الخيارات بناءً على اختيار المستخدم\n");
    fprintf(file, "    save = input(\"Do you want to save it in a file? (.JSON or .TXT) Yes or No: \").strip().lower()\n");
    fprintf(file, "    \n");
    fprintf(file, "    if user_choice == 1:  # عرض JSON\n");
    fprintf(file, "        if jsons is not None:\n");
    fprintf(file, "            formatted_json = json.dumps(jsons, indent=4, ensure_ascii=False)\n");
    fprintf(file, "            print(Fore.WHITE + Back.BLACK + formatted_json + Style.RESET_ALL)\n");
    fprintf(file, "\n");
    fprintf(file, "            if save in ['yes', 'y']:\n");
    fprintf(file, "                savename = input(\"Enter file name: \").strip()\n");
    fprintf(file, "                with open(savename + '.json', 'w') as file:\n");
    fprintf(file, "                    file.write(formatted_json)\n");
    fprintf(file, "                print(f\"File {savename}.json saved successfully.\")\n");
    fprintf(file, "        else:\n");
    fprintf(file, "            print(\"No JSON content to display.\")\n");
    fprintf(file, "    elif user_choice == 2:  # عرض النص\n");
    fprintf(file, "        print(response.text)\n");
    fprintf(file, "        if save in ['yes', 'y']:\n");
    fprintf(file, "            savename = input(\"Enter file name: \").strip()\n");
    fprintf(file, "            with open(savename + '.txt', 'w') as file:\n");
    fprintf(file, "                file.write(response.text)\n");
    fprintf(file, "            print(f\"File {savename}.txt saved successfully.\")\n");
    fprintf(file, "else:\n");
    fprintf(file, "    print(\"Request failed or server is not reachable.\")\n");


    fclose(file);
    printf("Python file created successfully!\n");

    int result = system("python script-1.py");

    if (result != 0) {
        printf("The python file could noit be run.\n");
    }
}

void add2() {
    FILE *file = fopen("script-2.py", "w");

    if (file == NULL)  {
        printf("Unable to open file.\n");
    }

    fprintf(file, "import webbrowser as web\n");
    fprintf(file, "print(\"Hello from a Python file created by C!\")\n");
    fprintf(file, "url = input('Enter Url: ')\n");
    fprintf(file, "web.open(url)\n");

    fclose(file);
    printf("Python file created successfully!\n");

    int result = system("python script-1.py");

    if (result != 0) {
        printf("The python file could noit be run.\n");
    }
}

void add3() {
    FILE *file = fopen("script-3.py", "w");

    if (file == NULL)  {
        printf("Unable to open file.\n");
    }

    fprintf(file, "import webbrowser as web\n");
    fprintf(file, "print(\"Hello from a Python file created by C!\")\n");
    fprintf(file, "url = input('Enter Url: ')\n");
    fprintf(file, "web.open(url)\n");

    fclose(file);
    printf("Python file created successfully!\n");

    int result = system("python script-1.py");

    if (result != 0) {
        printf("The python file could noit be run.\n");
    }
}

void add4() {
    FILE *file = fopen("script-4.py", "w");

    if (file == NULL)  {
        printf("Unable to open file.\n");
    }

    fprintf(file, "import webbrowser as web\n");
    fprintf(file, "print(\"Hello from a Python file created by C!\")\n");
    fprintf(file, "url = input('Enter Url: ')\n");
    fprintf(file, "web.open(url)\n");

    fclose(file);
    printf("Python file created successfully!\n");

    int result = system("python script-1.py");

    if (result != 0) {
        printf("The python file could noit be run.\n");
    }
}

void add5() {
    FILE *file = fopen("script-5.py", "w");

    if (file == NULL)  {
        printf("Unable to open file.\n");
    }

    fprintf(file, "import webbrowser as web\n");
    fprintf(file, "print(\"Hello from a Python file created by C!\")\n");
    fprintf(file, "url = input('Enter Url: ')\n");
    fprintf(file, "web.open(url)\n");

    fclose(file);
    printf("Python file created successfully!\n");

    int result = system("python script-1.py");

    if (result != 0) {
        printf("The python file could noit be run.\n");
    }
}
