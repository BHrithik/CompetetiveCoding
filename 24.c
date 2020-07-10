/**
 * @input A : Integer
 * 
 * @Output 2D int array. You need to malloc memory. Fill in len1 as row, len2 as columns 
 */
int ** prettyPrint(int A, int *len1, int *len2)
{
int i,j;
int B=2*A-1;
int lim=B;
int tmp=0;
    int **arr=(int **)malloc(B * sizeof(int *));
    for (i=0; i<B; i++)
                arr[i] = (int *)malloc(B * sizeof(int));
    while(A > 0)
    {
        for(i=tmp; i<lim; i++)
        {
            for(j=tmp; j<lim; j++)
            {
                arr[i][j] = A;
            }
        }
        
        A--;
        lim--;
        tmp++;
    }
    return arr;
}
