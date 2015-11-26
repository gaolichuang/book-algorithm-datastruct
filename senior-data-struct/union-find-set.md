# Union Find

资料来源 [Union Find Set]

   [Union Find Set]: <http://www.cnblogs.com/cherish_yimi/archive/2009/10/11/1580839.html>

一种简单的用途广泛的集合. 并查集是若干个不相交集合，能够实现较快的合并和判断元素所在集合的操作，应用很多，如其求无向图的连通分量个数等。最完美的应用当属：实现Kruskar算法求最小生成树

##### 基本操作
1、Make_Set(x) 把每一个元素初始化为一个集合

初始化后每一个元素的父亲节点是它本身，每一个元素的祖先节点也是它本身（也可以根据情况而变）。

2、Find_Set(x) 查找一个元素所在的集合

查找一个元素所在的集合，其精髓是找到这个元素所在集合的祖先！这个才是并查集判断和合并的最终依据。
判断两个元素是否属于同一集合，只要看他们所在集合的祖先是否相同即可。
合并两个集合，也是使一个集合的祖先成为另一个集合的祖先，具体见示意图

3、Union(x,y) 合并x,y所在的两个集合

合并两个不相交集合操作很简单：
利用Find_Set找到其中两个集合的祖先，将一个集合的祖先指向另一个集合的祖先。如图

###### 优化
1、Find_Set(x)时 路径压缩
寻找祖先时我们一般采用递归查找，但是当元素很多亦或是整棵树变为一条链时，每次Find_Set(x)都是O(n)的复杂度，有没有办法减小这个复杂度呢？
答案是肯定的，这就是路径压缩，即当我们经过"递推"找到祖先节点后，"回溯"的时候顺便将它的子孙节点都直接指向祖先，这样以后再次Find_Set(x)时复杂度就变成O(1)了，如下图所示；可见，路径压缩方便了以后的查找。

2、Union(x,y)时 按秩合并
即合并的时候将元素少的集合合并到元素多的集合中，这样合并之后树的高度会相对较小。

```C
int father[MAX];   /* father[x]表示x的父节点*/
int rank[MAX];     /* rank[x]表示x的秩*/

/* 初始化集合*/
void Make_Set(int x)
{
    father[x] = x; //根据实际情况指定的父节点可变化
    rank[x] = 0;   //根据实际情况初始化秩也有所变化
}

/* 查找x元素所在的集合,回溯时压缩路径*/
int Find_Set(int x)
{
    if (x != father[x])
    {
        father[x] = Find_Set(father[x]); //这个回溯时的压缩路径是精华
    }
    return father[x];
}


/* 
   按秩合并x,y所在的集合
   下面的那个if else结构不是绝对的，具体根据情况变化
  但是，宗旨是不变的即，按秩合并，实时更新秩。
*/
void Union(int x, int y)
{
    x = Find_Set(x);
    y = Find_Set(y);
    if (x == y) return;
    if (rank[x] > rank[y]) 
    {
        father[y] = x;
    }
    else
    {
        if (rank[x] == rank[y])
        {
            rank[y]++;
        }
        father[x] = y;
    }
}
```


### Question

###### 1.[leetcode][hard]Longest Consecutive Sequence
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.


问题分析：
  - 通过hash， 前一个和后一个，将集合合并起来。。。。 并查集
```
public class Solution {
    public int longestConsecutive(int[] num) {
        if(num==null || num.length<1 ) return 0;
        int longest = 1;
        
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        Set<Integer> set = new HashSet<Integer>();
        
        for(int i=0; i<num.length; i++) {
            int x = num[i];
            if(set.contains(x) ) continue;
            set.add(x);
            int min = x, max = x;
            
            if( map.containsKey(x+1) ) {
                max  = map.get(x+1);
                map.remove(map.get(x+1) );
                map.remove(x+1);
            }
            
            if( map.containsKey(x-1) ) {
                min = map.get(x-1);
                map.remove(map.get(x-1) );
                map.remove(x-1);
            } 
            map.put(min, max);
            map.put(max, min);
            longest = longest > max-min+1 ? longest : max-min+1;
        }
        return longest;
    }
}
```
