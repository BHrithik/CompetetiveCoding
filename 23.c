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
 * 
 * @Output Integer
 */
int lPalin(listnode* A) {
    listnode *l,*s;
    int f=1;
    int len=0;
    int i;
    l=A;
    s=A;
    while(l!=NULL)
    {
        len++;
        l=l->next;
    }
    int arr[len];
    for(i=0;i<len;i++)
    {
        arr[i]=A->val;
        A=A->next;
    }
    for(i=0;i<len;i++)
    {
        if(arr[i]!=arr[len-i-1])
        {
            f=0;
        }
    }
        return f;
}