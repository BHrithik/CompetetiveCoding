int c=0;
int k;
int m=0;
int l=INT_MAX;
int t=0;
int** HH;
void init(int capacity) {
    k=capacity;
    int H[capacity-1][3];
    int i;
    for(i=0;i<capacity;i++)
        H[i][2]=0;
    HH=H;
}

int get(int key) {
    int a;
    a=find(key);
    if(a!=-1)
    {
        t++;
        HH[a][2]=HH[a][2]+1+t;
        return HH[a][1];
    }
    else
    return -1;

}
int find(int key)
{
    int i;
    for(i=0;i<k;i++)
    {
        if(HH[i][0]==key)
        {
            return i;
        }
        else
        {
            return -1;
        }
    }
}

void set(int key, int value) {
    int i;
    if(c<k)
    {
        HH[m][0]=key;
        HH[m][1]=value;
        c++;
        m++;
    }
    else
    {
        for(i=0;i<k;i++)
        {
            if(HH[i][2]<l)
            {
                l=HH[i][2];
                m=i;
            }
        }
        HH[m][0]=key;
        HH[m][1]=value;
    }
}
