/**
 * @input A : String termination by '\0'
 * 
 * @Output string. Make sure the string ends with null character
 */
char* solve(char* A) 
{
    int l=strlen(A);
    if(l==1)
    {
        return A;
    }
    l=l+1;
    int i,j;
    int k;
    char ans[l];
    int s;
    int e;
    int p=0;
    int B[l+1];
    for(i=0;i<l;i++)
    {
        B[i]=A[i];
    }
    B[l]=' ';
    B[l+1]='\0';
    for(i=0;i<l;i++)
    {
        if(B[i]==' '||i==l-1)
        {
            k=l-i-1;
            ans[k]=B[i];
            k++;
            for(j=s;j<i;j++)
            {
               ans[k]=B[j];
               k++;
            }
            s=i+1;
        }
        if(i==l-1)
        {
            break;
        }
    }
    return ans;
}
