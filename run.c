#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fp;
    
    fp = fopen("output.txt","w");
    if (fp == NULL) {
        printf("file cannot open\n");
        exit(1);
    }
    fprintf(fp, "ABCDEFG\n");
    fclose(fp);
    return 0;
}
