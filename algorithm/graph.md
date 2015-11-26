# Graph-Travel

  - 最小生成树
    -  prim
    -  kruscal
  - 最短路径
  	- dijistra： 两点最短路径
  	- floyd:  任意两点最短路径
  - 拓扑排序
  	- DFS
  - 强连通分支
  - 二连通分支
遍历如下


```
深度优先搜索DFS
void DFS(G) {
	//初始化
	for 每个顶点 u in V[G] {
		color[u] = white
		T[u] = Null
	}
	time = 0; //时间戳
	for 每个顶点 v in V[G] {
		if color[v] == white
			DFS_Visit(G,v)
	}
}
void DFS_Visit(G,u) {
	color[u] = gray // 发现一个节点变成灰色
	d[u] = ++time;
	for 每个顶点 v Adj[u]: //u的临接节点
		if color[v] == white
			T[u] = u
			DFS_Visit(G,v)
		if color[v] == gray:
			print 出现环路了
	color[u] = Black
	f[u] = ++time;
}
```
> T[u] 为u的父亲  
> color 三种颜色  white,gray,black  
> d[u] 由白变灰的时间戳
> f[u] 由灰变黑的时间戳