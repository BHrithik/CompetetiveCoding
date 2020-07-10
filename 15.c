/**
 * @input A : Integer array
 * @input n1 : Integer array's ( A ) length
 * 
 * @Output Integer
 */
int removeDuplicates(int* A, int n1) {
    int i;
    int a=n1;
    int B[n1];
    int j;
    int k=0;
    for(i=2;i<n1;i++)
    {
        if(A[i]==A[i-2])
        {
            for(j=i;j<n1;j++)
            {
             A[j]=A[j+1];
             n1--;
            }
            a--;
        }
    }
    
    return a;
}
