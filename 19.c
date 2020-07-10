/**
 * @input A : Integer
 * @input B : Integer
 * 
 * @Output Integer
 */
int divide(int A, int B) {
    double a=(double)A;
    double b=(double)B;
    double c=sqrt((a/b)*(a/b));
    if(a>0 && b>0)
    return c;
    else if(a<0 && b<0)
    return c;
    else
    return -c;
}
