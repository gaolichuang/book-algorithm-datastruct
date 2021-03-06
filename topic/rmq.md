# Range Minimum/Maximum Query

如果用线段树求解不能保证任何时候都最优  
理解： 不能全计算完， 这样空间浪费；  不能每次都从新计算， 这样时间浪费。 介于中间的logN是更好的选择， 可以logN的： 树 or 引入2^i

Reference : http://blog.csdn.net/niushuai666/article/details/6624672/

  - 数据结构  
我们把F[i，j]平均分成两段（因为f[i，j]一定是偶数个数字），从 i 到i + 2 ^ (j - 1) - 1为一段，i + 2 ^ (j - 1)到i + 2 ^ j - 1为一段(长度都为2 ^ (j - 1))。用上例说明，当i=1，j=3时就是3,2,4,5 和 6,8,1,2这两段。F[i，j]就是这两段各自最大值中的最大值。于是我们得到了状态转移方程F[i, j]=max（F[i，j-1], F[i + 2^(j-1)，j-1]）。

  - 然后是查询。  
假如我们需要查询的区间为(i,j)，那么我们需要找到覆盖这个闭区间(左边界取i，右边界取j)的最小幂（可以重复，比如查询5，6，7，8，9，我们可以查询5678和6789）。
因为这个区间的长度为j - i + 1,所以我们可以取k=log2( j - i + 1)，则有：RMQ(A, i, j)=max{F[i , k], F[ j - 2 ^ k + 1, k]}。
举例说明，要求区间[2，8]的最大值，k = log2（8 - 2 + 1）= 2，即求max(F[2, 2]，F[8 - 2 ^ 2 + 1, 2]) = max(F[2, 2]，F[5, 2])；
