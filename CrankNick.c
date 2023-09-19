
#include <complex.h>
#include <stdio.h>
#include <math.h>


//define necessary constants here
double sigma;
void Dot(double complex* a, double complex* b, double complex* c, double complex* d, int N,double complex* rhs);
void TMDA(double complex* a, double complex* b, double complex* c, double complex* d, int n);

int  main(){
    //establishing time grid variables
    int tFinal = 200;
    double dt = .001;
    int tSteps = (int) tFinal / dt;
    //establishing spatial grid variables
    double xWidth = 10;
    double dx = .0001;
    int xSteps = (int) xWidth / dx;
    printf("%d\n", xSteps);
    
    //creating variables for constants
    double sigma = 1;
    //declaring static diagonal variables
    double complex aUpper[xSteps];
    double complex aLower[xSteps];
    double complex bUpper[xSteps];
    double complex bLower[xSteps];
    double complex aMid[xSteps];
    double complex bMid[xSteps];
    double complex rightVec[xSteps];
    //matrix off diagonals
    for(int i = 0; i <= xSteps - 1; i++){
        if(i == 0){
            aUpper[i] = 0  - sigma*I;
            aLower[i] = 0 - 0*I;
            bUpper[i] = 0 + sigma*I;
            bLower[i] = 0;
        }
        else if(i < xSteps-1){
            aUpper[i] = 0 - sigma*I;
            aLower[i] = 0 - sigma*I;
            bUpper[i]  = 0 + sigma*I;
            bLower[i] = 0 + sigma*I;
        }
        else{
            aUpper[i] = 0 - 0*I;
            aLower[i] = 0 - sigma*I;
            bUpper[i] = 0 + 0*I;
            bLower[i] = 0 + sigma*I; 
        }
    }
    
    int rightvecsize = (int)sizeof(rightVec)/sizeof(double complex);
    printf("%d\n",rightvecsize);
    
    //printf("%f %f\n",creal(aLower[1]), cimag(aLower[1])); debugging print

    /*
    for(int i = 1; i <= xSteps - 1; i++){
        rightVec[i] = exp( -1.0 * pow((i - 5.0), 2) / 10 ) + 0.0 *I;
        printf("rightVec[%d] = %lf + %lfi\n", i, creal(rightVec[i]), cimag(rightVec[i]));
    }
    double complex rhs[xSteps];
    /*
 
    
    for(int i = 0; i <= tSteps; i++){
    //generate time dependent diagonals
        for(int j = 0; j <= xSteps - 1; j++){
        aMid[j] = 1 + 2 * sigma*I;
        bMid[j] = 1 - 2 * sigma*I;
        Dot(&bUpper[0], &bMid[0], &bLower[0], &rightVec[0], xSteps, &rhs[0]); 
        TMDA(&aUpper[0], &aMid[0], &aLower[0], &rightVec[0], xSteps);
    

        }
    }
    */
    
   return 0;


}

void Dot(double complex* a, double complex* b, double complex* c, double complex* d, int N,double complex* rhs){
    for(int i = 0; i <= N -1;i++){
            rhs[0] = b[0] * d[0] + c[0] + d[1];
        if(i < N -1){
            rhs [i] = a[i] * d[i-1] + b[i] * d[i] + c[i] * d[i + 1];    
        }
        else {
            rhs [i] = a[i] * d[i-1] + b[i] * d[i];
        }
        }
    }

void TMDA(double complex* a, double complex* b, double complex* c, double complex* d, int n){
    /*a is lower diag
    b is middle diag
    c is upper diag
    n is step size*/
    n--; //C is an index 0 language
    c[0] /= b[0];
    d[0] /= b[0];

    //forward sweep
    for (int  i = 1; i < n; i++) {
        c[i] /= b[i] - a[i]*c[i-1];
        d[i] = (d[i] - a[i]*d[i-1] /  (b[i] - a[i]*c[i-1]));
    } 

    d[n] = (d[n] - a[n]*d[n-1]) /(b[n] - a[n]*c[n-1]);

    //back substitution
    for ( int i = n; i-- > 0;){
        d[i] -= c[i]*d[i+1];
    }

}