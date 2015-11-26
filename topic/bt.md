# Binary Tree


## Question
###### 1.flatten it to a linked list in-place
```
         1
        / \
       2   5
      / \   \
     3   4   6
==》 
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
```

前序遍历，在加上个队尾指针。
```
    TreeNode* Tail;
    void preOrder(TreeNode* root)
    {
        if(root != NULL)
        {
            TreeNode* left = root->left;
            TreeNode* right = root->right;
            if(Tail == NULL){
                Tail = root;
            }
            else{
                if(Tail->right != root)
                    Tail->right = root;
                Tail->left = NULL;
                Tail = root;
            }
            preOrder(left);
            preOrder(right);
        }
    }
```
###### 2.输出一棵树各种组合形式
```
  def dfs(self, begin, end):
    '''
    return root list
    '''
    if begin > end:
      return [None]
    ret = []
    for i in range(begin, end+1):
      left = self.dfs(begin,i-1)
      right = self.dfs(i+1,end)
      for j in left:
        for k in right:
          root = TreeNode(i)
          root.left,root.right = j,k
          ret.append(root)
    return ret
 ```