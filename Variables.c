#include <stdio.h>
/// @brief 
/// @return 
int main(){
       // Print Text Command!!
       /*
       \a - Alert [Beep, Bell]
       \b - Backspace
       \e - Escape character
       \f - Formfeed Page Break
       \n - Newline [Line feed]
       \r - Carriage Return
       \t - Horizontal Tab
       \v - Vertical Tab
       \\ - Backslash
       \' - Apostrophe, Single Quotation Mark
       \" - Double Quotation Mark
       */
       int x;        //DECLARATION
       x = 123;      //INITIALIZATION
       int y = 321;  //DECLARATION + INITIALIZATION

       int age = 18;             //INTEGER
       float gpa = 1.40;         //FLOATING POINT NUMBER
       char grade = 'B';         //SINGLE CHARACTER
       char name[] = "Luna";     //ARRAY OF CHARACTERS

       printf("Hello there %s.\n",name);
       printf("You are %d years old!\n",age);
       printf("So, your average grade is %c.\n",grade);
       printf("Your GPA is %f, Keep it up!\n",gpa);

       return 0;
}