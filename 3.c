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
 * @Output head pointer of list.
 */
listnode* detectCycle(listnode* A) {
    listnode *L,*S,*T;
    S=A;
    T=A;
    int k=0,i,j;
    for(i=1;;i++)
    {
        if(A->next==NULL)
        {
            return NULL;
        }
        S=T;
        for(j=0;j<i;j++)
        {
            if(S==A->next)
            {
                return S;
            }
            S=S->next;
        }
        
    A=A->next;
    }
}
