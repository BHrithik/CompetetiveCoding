/**
 * @input A : Integer
 * 
 * @Output Integer
 */
int trailingZeroes(int A)
{
    int fives = 0;
    int i,j;
    i = A;
    while(i>4){
        j=i;
        while(j%5==0)
        {
            fives+=1;
            j/=5;
        }
        i--;
    }
    return fives;
}