/**
 * @input A : Integer
 * @input B : Integer
 * 
 * @Output Integer
 */
int uniquePaths(int A, int B) {
    int n;
    int ncr;
    n=(A-1)+(B-1);
    ncr = (fact(n) / (fact(A-1) * fact(n - A-1)))+(fact(n) / (fact(B-1) * fact(n - B-1)));
    return ncr;
}
 
int fact(int z)
{
    int f = 1, i;
    if (z == 0)
    {
        return(f);
    }
    else
    {
        for (i = 1; i <= z; i++)
    {
            f = f * i;
    }
    }
    return(f);
}
