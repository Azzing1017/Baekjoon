def solution(n, times):
    answer = 0
    left = 0
    right = max(times) * n
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for val in times:
            people += mid // val
        if people >= n:
            answer = mid
            right = mid - 1
        elif people < n :
            left = mid + 1
    return answer