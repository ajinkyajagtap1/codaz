#include <stdio.h>

int main(int argc, char **argv)
{
	int i;
	for(i=1;i<=20;i++) //for loop for i= 1 to 20
{
	if (i % 2 == 0)              //  if  statment for mod function to differentaite i in even and odd number till 20.
		printf("\033[22;34 # %d :ECE\033[0m\n",i); // print even number value with blue where ANSI evalution is 34m
	else
		printf("\033[22;32 # %d :ECE\033[0m\n",i);// print odd number value with  green where ANSI evalution is 32m
}
	return 0;
}
