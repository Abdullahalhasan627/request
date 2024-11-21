#include <stdio.h>
#include <stdlib.h>

int number;

void add(); 

int main(void) {
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

void add1() {
    FILE *file = fopen("script-1.py", "w");

    if (file == NULL)  {
        printf("Unable to open file.\n");
    }

    fprintf(file, "import `requests\n");
    fprintf(file, "\n");
    fprintf(file, "\n");
    fprintf(file, "\n");
    fprintf(file, "\n");
    fprintf(file, "\n");
    fprintf(file, "\n");
    fprintf(file, "\n");
    fprintf(file, "\n");


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
