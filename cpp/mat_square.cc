#include<iostream>

using namespace std;

int main() {
   int A[3][3];
   int B[3][3];


   // Initialize A matrix
   for(int i=0;i<3;i++)
     for(int j=0;j<3;j++)
		A[i][j] = i+j;
 
  // Print A matrix

   for(int i=0;i<3;i++){
     for(int j=0;j<3;j++)
		cout<<A[i][j]<<" ";
     cout<<endl; 
   } 


   // Square A matrix elementwise and save in B matrix
   for(int i=0; i<3; i++){
    for(int j=0; j<3; j++)
    B[i][j]=A[i][j]*A[i][j];
}

   // Print B matrix
    for(int i=0;i<3;i++){
     for(int j=0;j<3;j++)
		cout<<B[i][j]<<" ";
     cout<<endl; 
   } 


  return 0;

}
