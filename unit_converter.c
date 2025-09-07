#include <stdio.h>

int main(){
    double kms, miles;
    double inches, feet;
    double cms, pounds;
    double kgs, metres;
    int num;
    for(int a=1; a>0; a++){
        printf("Following are the options:\n1)kms to miles\n2)inches to foot\n3)cms to inches\n4)pounds to kgs\n5)inches to metres\nTo go for conversion, enter the number that conversion is listed as\nTo quit, press 9\n");
        printf("Enter a value: ");
        scanf("%d", &num);
        if(num==1){
            printf("Enter value in kms: ");
            scanf("%lf", &kms);
            miles = kms/1.609;
            printf("The entered value in miles is %lf\n\n", miles);
        }
        if(num==2){
            printf("Enter value in inches: ");
            scanf("%lf", &inches);
            feet = inches/12;
            printf("The entered value in feet is %lf\n\n", feet);    
        }
        if(num==3){
            printf("Enter value in cms: ");
            scanf("%lf", &cms);
            inches = cms/2.24;
            printf("The entered value in inches is %lf\n\n", inches);
        }
        if(num==4){
            printf("Enter value in pounds: ");
            scanf("%lf", &pounds);
            kgs = pounds/2.205;
            printf("The entered value in kgs is %lf\n\n", kgs);
        }
        if(num==5){
            printf("Enter value in inches: ");
            scanf("%lf", &inches);
            metres = inches/39.37;
            printf("The entered value in metres is %lf\n\n", metres);    
        }
        if(num==9){
            printf("The program has been terminated");
            break;
        }
    } 
}