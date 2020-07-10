/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::insertionSortList(ListNode* A) {
    ListNode *h,*c,*s,*p;
    p=A;
    s=A;
    h=A;
    int len=0;
    int i;
    while(p!=NULL)
    {
        len++;
        p=p->next;
    }
    if(len==1)
    {
        return A;
    }
    int arr[len];
    for(i=0;i<len;i++)
    {
        arr[i]=A->val;
        A=A->next;
    }
    int j,temp;
    for (i = 1 ; i < len; i++)
    {
        j = i;
            while ( j > 0 && arr[j-1] > arr[j])
            {            
                temp     = arr[j];
                arr[j]   = arr[j-1];
                arr[j-1] = temp;
                j--;
            }
    }
    for(i=0;i<len;i++)
    {
        s->val=arr[i];
        s=s->next;
    }
    s=h;
    return s;
    
}
