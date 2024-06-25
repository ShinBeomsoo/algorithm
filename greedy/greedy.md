footer: Leo
slidenumbers: true
autoscale: true
slide-transition: true

# Greedy Algorithm

---

# Greedy 알고리즘

**최적의 해를 구하는데에 사용되는 근사적인 방법**으로, 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행하여 최종적인 해답에 도달한다.

- Greedy choice property (탐욕 선택 조건)
  - 앞의 선택이 이후의 선택에 영향을 주지 않는다.
- Optimal Substructure (최적 부분 구조 조건)
  - 문제에 대한 최적해가 부분문제에 대해서도 역시 최적해이다.



----

## [백준 14916 거스름돈](https://www.acmicpc.net/problem/14916)



 춘향이는 편의점 카운터에서 일한다.

손님이 2원짜리와 5원짜리로만 거스름돈을 달라고 한다. 2원짜리 동전과 5원짜리 동전은 무한정 많이 가지고 있다. 동전의 개수가 최소가 되도록 거슬러 주어야 한다. 거스름돈이 n인 경우, 최소 동전의 개수가 몇 개인지 알려주는 프로그램을 작성하시오.

예를 들어, 거스름돈이 15원이면 5원짜리 3개를, 거스름돈이 14원이면 5원짜리 2개와 2원짜리 2개로 총 4개를, 거스름돈이 13원이면 5원짜리 1개와 2원짜리 4개로 총 5개를 주어야 동전의 개수가 최소가 된다.

---

## Step 1

```python
def main(money):
    if money % 2 == 0: # 짝수
        coin_5 = money // 5
        coin_2 = money % 5 // 2
    else: # 홀수
        coin_5 = money // 5 - 1
        coin_2 = (money - coin_5*5) // 2
    return coin_5 + coin_2



if __name__ == "__main__":
    money = int(input())
    result = main(money)
    print(result)
```

error의 원인: 10보다 작은 수에 대한 처리가 안된다.

---

## Step 2

```python

```



