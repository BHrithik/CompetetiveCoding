int Solution::findRank(string A) {
    int ans=0;
    int n=A.size();
    int m=n;
    int mod=1e6+3;
    for(int i=0;i<A.size();i++)
    {
        int count=0;
        for(int j=i+1;j<A.size();j++)
        {
            if(A[i]>A[j])count++;
        }
        ans=((ans*1ll*m)%mod+count)%mod;
        m--;
    }
    ans++;
    return ans;
}
