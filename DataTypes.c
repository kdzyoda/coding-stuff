#include <stdio.h>
#include <stdbool.h>


int main(){
      char a = 'A';         // SINGLE CHARACTER %c
      char b[] = "Luna";    // ARRAY OF CHARACTERS %s

      float c = 3.141592;                  // 4 BYTES (32 bits of precision) 6-7 digits %f
      double d = 3.141592653589793;        // 8 BYTES (64 bits of precision) 15-16 digits %lf

      bool e = true;                      // 1 BYTE (true or false) %d

      // char f = 100;                    // 1 BYTE (-128 to +127) %d or %c
      char f = 120;                       // 1 BYTE (-128 to +127) %d or %c
      unsigned char g = 255;              // 1 BYTE (0 to +225) %d or %c   
      short int h = 32767;                // 2 BYTES (-32,768 to +32,767) %d
      unsigned short i = 65535;           // 2 BYTES (0 to +65,535) %d

      int j = 2147483647;                 // 4 BYTES (-2,147,483,648 to +2,147,483,647) %d
      unsigned int k = 4294967295L;       // 4 BYTES (0 to +4,294,967,295) %u

      long long int l = 9223372036854775807;                       // 8 bytes (-9 quintillion to +9 quintillion) %lld
      unsigned long long int m = 18446744073709551615U;           // 8 bytes (0 to +18 quintillion) %llu


       printf("%c\n", a);            // char
       printf("%s\n", b);            // character array
       printf("%f\n", c);            // float
       printf("%lf\n", d);           // double
       printf("%d\n", e);            // bool
       printf("%d\n", f);            // char as numeric value
       printf("%c\n", f);            // char as numeric value
       printf("%d\n", g);            // unsigned char as numeric value
       printf("%d\n", h);            // short
       printf("%d\n", i);            // unsigned short
       printf("%d\n", j);            // int
       printf("%u\n", k);            // unsigned int
       printf("%lld\n", l);          // long long int
       printf("%llu\n", m);          // unsigned long long int
       
       return 0;
}