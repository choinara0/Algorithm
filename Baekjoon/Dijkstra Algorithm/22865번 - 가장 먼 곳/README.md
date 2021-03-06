## 가장 먼 곳
 
|시간 제한|	메모리 제한|	제출|	정답|	맞힌 사람|	정답 비율|
|---|---|---|---|---|---|
|1.5 초|	1024 MB|	424|	139|	104|	31.804%|

### 문제
N개의 땅 중에서 한 곳에 자취를 하려고 집을 알아보고 있다. 세 명의 친구 A, B, C가 있는데 이 친구들의 살고 있는 집으로부터 가장 먼 곳에 집을 구하려고 한다.

이때, 가장 먼 곳은 선택할 집에서 거리가 가장 가까운 친구의 집까지의 거리를 기준으로 거리가 가장 먼 곳을 의미한다.

예를 들어, X 위치에 있는 집에서 친구 A, B, C의 집까지의 거리가 각각 3, 5, 4이라 가정하고 Y 위치에 있는 집에서 친구 A, B, C의 집까지의 거리가 각각 5, 7, 2라고 하자.

이때, 친구들의 집으로부터 땅 X와 땅 Y 중 더 먼 곳은 X 위치에 있는 집이 된다. 왜냐하면 X에서 가장 가까운 친구의 집까지의 거리는 3이고, Y에서는 2이기 때문이다.

친구들이 살고 있는 집으로부터 가장 먼 곳을 구해보자.

### 입력
- 첫번째 줄에 자취할 땅 후보의 개수 N이 주어진다.
- 2번째 줄에는 친구 A, B, C가 사는 위치가 공백으로 구분되어 주어진다. 이때 친구들은 N개의 땅 중 하나에 사는 것을 보장한다. (같은 위치에서 살 수 있다.)
- 3번째 줄에는 땅과 땅 사이를 잇는 도로의 개수 M이 주어진다.
- 그 다음줄부터 M+3번째 줄까지 땅 D, 땅 E, 땅 D와 땅 E와 사이를 연결하는 도로의 길이 L이 공백으로 구분되어 주어진다. 이 도로는 양뱡항 통행이 가능하다.

### 출력
- 친구들이 살고 있는 집으로부터 가장 먼 곳의 땅 번호를 출력한다. 만약 가장 먼 곳이 여러 곳이라면 번호가 가장 작은 땅의 번호를 출력한다.

### 제한
- 1 ≤ N ≤ 100,000
- N - 1 ≤ M ≤ 500,000
- 1 ≤ A, B, C, D, E ≤ N
- 1 ≤ L ≤ 10,000
#### 예제 입력 1 
- 6
- 1 2 5
- 8
- 1 2 1
- 2 3 4
- 1 4 2
- 2 5 3
- 1 6 5
- 5 6 2
- 3 4 2
- 4 5 6
#### 예제 출력 1 
- 3

### 문제 출처
[백준](https://www.acmicpc.net/problem/22865)