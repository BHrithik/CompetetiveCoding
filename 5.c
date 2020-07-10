/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 * 
 * typedef struct ListNode listnode;
 * 
 * listnode* listnode_new(int val) {
 *     listnode* node = (listnode *) malloc(sizeof(listnode));
 *     node->val = val;
 *     node->next = NULL;
 *     return node;
 * }
 */
/**
 * @input A : Head pointer of linked list 
 * @input B : Integer
 * @input C : Integer
 * 
 * @Output head pointer of list.
 */
listnode* reverseBetween(listnode* A, int B, int C) {
    if(B==C)
    {
        return A;
    }
    listnode *S,*L,*T;
    L=A;
    S=A;
    T=A;
    int len=0;
    int i,y,x;
    x=B-1;
    y=C-1;
    int k=0;
    while(L!=NULL)
    {
        len++;
        L=L->next;
    }
    int arr1[len];
    int arr2[len];
    for(i=0;i<len;i++)
    {
        arr1[i]=A->val;
        A=A->next;
    }
    for(i=0;i<len;i++)
    {
        arr2[i]=arr1[i];
    }
    for(i=x;i<=y;i++)
    {
        arr1[i]=arr2[y-k];
        k++;
    }
    for(i=0;i<len;i++)
    {
        S->val=arr1[i];
        S=S->next;
    }
    S=T;
    return S;
}
