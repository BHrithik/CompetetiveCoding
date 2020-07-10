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
 * @input B : Head pointer of linked list 
 * 
 * @Output head pointer of list.
 */
listnode* getIntersectionNode(listnode* A, listnode* B) {
    listnode *a,*b;
    int d,i,l1=0,l2=0;
    a=A;
    b=B;
    while(a!=NULL) {
        l1++;
        a=a->next;
    }
    while(b!=NULL) {
        l2++;
        b=b->next;
    }
   // printf("%d %d\n",l1,l2);
    if(l1>l2) {
        for(i=1;i<=(l1-l2);i++)
            A=A->next;
    }
    else if(l1<l2) {
        for(i=1;i<=(l2-l1);i++)
            B=B->next;
    }
    while(A!=B) {
        A=A->next;
        B=B->next;
       // printf("%d\t %d\n", A->val, B->val);
    }
    return A;
}
