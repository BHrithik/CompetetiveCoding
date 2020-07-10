/**
 * @input A : Read only ( DON'T MODIFY ) String termination by '\0'
 * @input B : Read only ( DON'T MODIFY ) String termination by '\0'
 * 
 * @Output Integer
 */
int strStr(const char* A, const char* B) {
    
    int pos=A.find(B);
    return pos;
    /*
    int la=strlen(A);
    int lb=strlen(B);
    int s=99999999;
    int i,j;
    int flag;
    if(lb>la)
    {
        return -1;
    }
    else
    {
        for(i=0;i<la;i++)
        {
            for(j=0;j<lb;j++)
            {
                if(A[i]==B[j])
                {   
                    if(i<s)
                    {
                        s=i;
                    }
                    flag=0;
                    i++;
                    if(j==lb-1)
                    {
                        break;
                    }
                }
                else
                {
                    s=99999999;
                    flag=1;
                    break;
                }
            }
        }
        if(flag==1)
        {
            return -1;
        }
        else if(flag==0)
        {
            return s;
        }
    }
    */
}
