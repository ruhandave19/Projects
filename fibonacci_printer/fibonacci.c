#include <stdio.h>

// When the user enters 8, I need the computer to print 0, 1, 1, 2, 3, 5, 8, 13

int main(){
  int num;
  int i = 0;    
  int j = 1;
  int x;
  printf("Enter a position: ");
  scanf("%d", &num);
  if(num>2){
    printf("The fibonacci series till position %d is ", num); 
    printf("0, 1, ");
    for(int a=1; a<=(num-2); a++){
      x = i+j;
      i = j;
      j = x;
      printf("%d, ", x);
    }
    printf("\b\b ");
  }
  else if(num==1){
    printf("The fibonacci series till position 1 is 0");
  }
  else{
    printf("The fibonacci series till position 2 is 0, 1");
  }
  return 0;
}