# Sort

|排序方法| 最好时间 | 平均时间 | 最坏时间 | 辅助空间 | 稳定性 | 
|--------|----------|----------|----------|----------|--------|
|插入排序|O(N)|O(N2)|O(N2)|O(1)|稳定|
|冒泡排序|O(N)|O(N2)|O(N2)|O(1)|稳定|
|简单选择|O(N2)|O(N2)|O(N2)|O(1)|不稳定|
|快速排序|O(NlogN)|O(NlogN)|O(N2)|O(NlogN)|不稳定|
|堆排序  |O(NlogN)|O(NlogN)|O(NlogN)|O(1)|不稳定|
|归并排序|O(NlogN)|O(NlogN)|O(NlogN)|O(N)|稳定|
|基数排序|O(d(n+rd))|O(d(n+rd))|O(d(n+rd))|O(d(n+rd))|稳定|


##### 冒泡排序优化
> 第i趟排序应该是从R[1] - R[n-i+1]中依次比较相邻两个就的关键字， 并在逆序时交换相邻记录，其结果是这n-i+1个记录中关键字最大的记录被交换到第n-i+1的位置上  
> 判别起泡排序结束的条件应该是 **在一趟排序过程中没有进行过交换记录的操作**
```
# Sample code
numPairs = n-1
didSwitch = true
while(didSwitch) {
    didSwitch = false
    for (j = 0;j < numPairs; j++) {
        if (E[j] < E[j+1]) {
            exchange(E[j],E[j+1])
            didSwitch = True
        }
    }
}
```
> 最好情况，比较n-1次，交换0次， 正序  
> 最坏情况， 比较0.5*n*(n-1) 次， 交换0.5*n*(n-1)*3次操作， 逆序  
> 平均情况， O(N2)  

**改进算法!**  
> 每趟扫描记录最后一次发生交换位置，则在该位置之后次序有序
```
void bubbleSort(Element[] E, int n) {
    int numPairs, last, j;
    last = n-1;
    while (last > 0) {
        numPairs = last;
        for (j = 0;j < numPairs; j++) {
            if (E[j] < E[j+1]) {
                exchange(E[j],E[j+1]);
                last = j; //记录最后交换位置
            }
    }
}
```

##### 直接插入排序优化
> 直接插入排序适用于个数比较少， 随机性强的情况  
> 插入排序实现时，也不是相邻元素交换，而是使用监视哨实现，减少交换次数  
> 以相邻元素比较，交换的方式排序 (n*n)/4是最好的，即插入排序是最好的： 证明： 逆序个数。。

插入排序改进
 - 二分查找插入位置
 - 链表插入， 这样减少移动次数
   - 单链表： 插入R[i]时， 记录R[0] --R[i-1] 有序，将R[i]脱链，在采用顺序比较的方法，找到R[i]应该插入位置，
   - 第i趟排序， 最多比较i次， 最少1次
   - n-1趟总比较次数， 最多n*(n-1)/2,最少n-1次
   - 记录移动0次，时间效率O(N2)，辅助空间O(N)


##### 判定树
> 解释为什么快速排序，归并排序，堆排序的最坏复杂度是O(NlogN)    
> 排序算法最好能做到O(NlogN)  
> 判定树最多N!个叶子， 高度logN! -- NlogN  


##### 堆排序
> 建堆和调整堆，具体参看代码  
```python
class HeapMin(object):
  def __init__(self, s=[], capacity = 5):
    self.s = s
    self.c = capacity
    self._adjust()
  def judge(self, a, b):
    return True if a > b else False
  def _adjustHeap(self, s, m, lens): # 堆一次调整过程
    p = m
    j = 2*m + 1
    while j < lens:
      if self.judge(s[j], s[j+1]): j+=1  # 左右孩子中得到较大的，第一次比较
      if self.judge(s[j], s[p]): break   # 较大者跟父亲比较， 第二次比较
      s[j],s[p] = s[p],s[j]
      p = j
      j = 2*p + 1
  def _adjust(self):
    i = len(self.s)/2
    while i >= 0:
      self._adjustHeap(self.s, i, len(self.s))  # 从下往上调整堆
      i -= 1
    while len(self.s) > self.c:
      self.s.pop()
  def add(self, v):
    self.s.append(v)
    idx = len(self.s) - 1
    p = (idx+1)/2 - 1
    while p >= 0:
      if self.judge(self.s[idx],self.s[p]):break
      self.s[p],self.s[idx] = self.s[idx],self.s[p]
      idx = p
      p = (idx+1)/2 - 1
    if len(self.s) > self.c:
      self.s.pop()
  def top(self):
    if not self.s: return 0
    return self.s[0]
class HeapMax(HeapMin):
  def judge(self, a, b):
    return True if a < b else False
```
**堆排序优化**
> 当堆很大时，主要时间花在了排序过程的调整堆（比较两次，左右一次， 大者跟父亲一次）  
>修改成：仅比较两个孩子节点，到了1/2的节点后，check是否出错， 出错则回退，否则继续  
> 复杂度会变成logn + loglogN


##### 归并排序优化
  - 归并排序的问题在于移动较多， 空间需求大
  - 改进方法1： 奇数次 A->B, 偶数次 B->A， 不写回的归并排序
  - 改进方法2： 无逆序， 一开始分成无逆序的小组， 减少分组次数
  - 改进方法3： 插入和归并排序结合
    - 输入相对有序，则与无逆序结合
    - 输入相对随机， 则与插入排序结合
      - 先用插入排序方法将20个左右元素做成有序集合，然后再归并

```C
// 归并排序的非递归实现
void Merge(RedType SR[], RedType TR[], int i, int m, int n) {
    // 将有序的SR[i] - SR[m] 和SR[m+1] - SR[n] 合并到TR
    int j,k,l;
    for (j = m+1, k=1; i <= m && j <= n;++k){
        if (SR[i].key <= SR[j].key)
            TR[k] = SR[i++]
        else
            TR[k] = SR[j++]
    }
    if (i <= m) for (l=0;l <= m-i;l++) TR[k+l]=SR[i+l]
    if (j <= n) for (l=0;l <= n-j;l++) TR[k+l]=SR[j+l]
}
void MergePass(RedType R[], RedType R1[], int length) {
    // 一趟归并排序，一趟合并， length为子序长度
    int i=0,j;
    while (i + 2*length -1 < n){
        Merge(R,R1,i,i+length-1,i+2*length-1);
        i = i+2*length
    }
    if (i + length - 1 < n-1) {
        Merge(R,R1,i,i+length-1,n-1)
    }else{
        for (j = i;j < n;j++) R1[j] = R[j]
    }
}
void MergeSort(RedType R[]) {
    // 不回写的归并排序
    int length = 1;
    while (length < n) {
        MergePass(R,R1,length)
        length = 2*length
        MergePass(R1,R,length);
        length = 2*length
    }
}
```


##### 快速排序优化
 - 改进方法： 找到合适的枢轴
 - 改进方法： 和插入排序结合

> 递归版本实现  
> 先从数列中取出一个数作为基准数。  
> 分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边  
> 再对左右区间重复第二步，直到各区间只有一个数。

```python
def sub_sort(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        while low < high and array[high] < key:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
    array[low] = key
    return low


def quick_sort(array,low,high):
     if low < high:
        key_index = sub_sort(array,low,high)
        quick_sort(array,low,key_index)
        quick_sort(array,key_index+1,high)


if __name__ == '__main__':
    array = [8,10,9,6,4,16,5,13,26,18,2,45,34,23,1,7,3]
```

##### 基数排序
 - 必须知道取值范围
 - N个元素，M个桶

##### 排序算法比较
 - 在输入完全随机情况下  快速排序较快
 - 归并排序在于移动较多 - 缺点
 - 堆， 缺点在比较较多， 左右孩子，父亲， 两次比较，并且地址要除2， 出发代价较高
 - 在元素相对有序时， 插入排序O(N)级别，， 比如数据库更新
 - N较小时， 插入排序页最好， 因n <= 16是， n*n/4 <= NlogN

