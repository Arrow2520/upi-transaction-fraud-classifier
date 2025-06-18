# The following functions are used to find the longest common sequence

# 1. Using Recursion
def lcs_recursive(seq1, seq2, idx1=0, idx2=0):
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0
    elif seq1[idx1] == seq2[idx2]:
        return 1 + lcs_recursive(seq1, seq2, idx1 + 1, idx2 + 1)
    else:
        option1 = lcs_recursive(seq1, seq2, idx1 + 1, idx2)
        option2 = lcs_recursive(seq1, seq2, idx1, idx2 + 1)
        return max(option1, option2)


# 2. Using Memorization
def lcs_memo(seq1, seq2):
    memo = {}

    def recurse(idx1=0, idx2=0):
        key = (idx1, idx2)
        if key in memo:
            return memo[key]
        elif idx1 == len(seq1) or idx2 == len(seq2):
            memo[key] = 0
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recurse(idx1 + 1, idx2 + 1)
        else:
            memo[key] = max(recurse(idx1+1, idx2), recurse(idx1, idx2+1))
        return memo[key]
    return recurse(0, 0)


# 3. Using Dynamic Programming
def lcs_dp(seq1, seq2):
    n1, n2 = len(seq1), len(seq2)
    table = [[0 for x in range(n2 + 1)] for x in range(n1 + 1)]
    for i in range(n1):
        for j in range(n2):
            if seq1[i] == seq2[j]:
                table[i+1][j+1] = 1 + table[i][j]
            else:
                table[i+1][j+1] = max(table[i][j+1], table[i+1][j])
    return table[-1][-1]


# Following functions are for Knapsack Problem

# 1. Recursion
def max_profits_recur(weights, profits, capacity, idx=0):
    if idx == len(weights):
        return 0
    elif weights[idx] > capacity:
        return max_profits_recur(weights, profits, capacity, idx + 1)
    else:
        return max(max_profits_recur(weights, profits, capacity, idx + 1), (profits[idx+1] + max_profits_recur(weights, profits, capacity - weights[idx], idx + 1)))


# 2. Memorization
def max_profits_memo(weights, profits, capacity):
    memo = {}

    def recurse(remaining, idx=0):
        key = (idx, remaining)
        if key in memo:
            return memo[key]
        elif idx == len(weights):
            memo[key] = 0
        elif weights[idx] > remaining:
            memo[key] = recurse(remaining, idx+1)
        else:
            memo[key] = max(recurse(remaining, idx+1), profits[idx] + recurse(remaining - weights[idx], idx+1))
        return memo[key]
    return recurse(capacity, 0)


# 3. Dynamic Programming
def max_profits_dp(weights, profits, capacity):
    n = len(weights)
    table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(n):
        for c in range(1, capacity + 1):
            if weights[i] > c:
                table[i + 1][c + 1] = table[i][c]
            else:
                table[i + 1][c] = max(table[i][c], profits[i] + table[i][c - weights[i]])
    return table[-1][-1]