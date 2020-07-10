/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 * 
 * typedef struct TreeNode treenode;
 * 
 * treenode* treenode_new(int val) {
 *     treenode* node = (treenode *) malloc(sizeof(treenode));
 *     node->val = val;
 *     node->left = NULL;
 *     node->right = NULL;
 *     return node;
 * }
 */
/**
 * @input A : Root pointer of the tree 
 * @input B : Integer
 * 
 * @Output root pointer of tree.
 */
treenode *Find(treenode *root, int data)
 {
    if(root==NULL)
     return NULL;
    treenode *found=root;
    if(data==root->val)
     return found;
    if(data<root->val)
     Find(found->left, data);
    else
     Find(found->right, data);
 }
treenode* getSuccessor(treenode* A, int B) {
    treenode *current=Find(A,B);
    if(current==NULL)
     return NULL;
    if(current->right!=NULL)
     {
        treenode *temp=current->right; 
        while(temp->left!=NULL)
         temp=temp->left;
        return temp; 
     }
    else
     {
        treenode *successor=NULL;
        treenode *ancestor=A;
        while(ancestor!=current)
         {
            if(current->val<ancestor->val)
             {
              successor=ancestor;
              ancestor=ancestor->left;
             }
            else
             ancestor=ancestor->right;
         }
        return successor; 
     }
}
