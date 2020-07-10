/**
 * @input A : Integer
 * 
 * @Output 2D int array. You need to malloc memory. Fill in len1 as row, len2 as columns 
 */
/**
 * @input A : Integer
 * 
 * @Output 2D int array. You need to malloc memory. Fill in len1 as row, len2 as columns 
 */
int ** generateMatrix(int A, int *len1, int *len2) {
    int t=0;
    int b=A-1;
    int l=0;
    int r=A-1;
    int dir=0;
    int c=1;
    int i;
    *len1 = A;
    *len2 = A;
    int **arr = (int **)malloc(A * sizeof(int *));
    for (i=0; i<A; i++)
                arr[i] = (int *)malloc(A * sizeof(int));
    while(t<=b && l<=r)
    {
        if(dir==0)
        {
            for(i=l;i<=r;i++){
                arr[t][i]=c;
                c++;
            }
            t++;
            dir=1;
        }
        else if(dir==1)
        {
            for(i=t;i<=b;++i){
                arr[i][r]=c;
                c++;
            }
            r--;
            dir=2;
        }
        else if(dir==2)
        {
            for(i=r;i<=l;--i){
                arr[b][i]=c;
                c++;
            }
            b--;
            dir=3;
        }
        else if(dir==3)
        {
            for(i=b;i<=t;--i){
                arr[i][l]=c;
                c++;
            }
            l++;
            dir=0;
        }
        
    }
    return arr;

}


