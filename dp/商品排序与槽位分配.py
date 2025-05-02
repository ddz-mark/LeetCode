# -*- coding: utf-8 -*-
# @Time : 2025/5/2 17:11
# @Author : ddz

def max_exposure_score(products, exposure_rates):
    # Sort products by price descending, then by score descending
    products_sorted = sorted(products, key=lambda x: (-x[0], -x[1]))
    n_products = len(products_sorted)
    n_slots = len(exposure_rates)

    # dp[i][j]：表示前 i 个槽位中，最后一个选择的商品是第 j 个商品时的最大得分。
    dp = [[-float('inf')] * n_products for _ in range(n_slots)]
    parent = [[-1] * n_products for _ in range(n_slots)]

    # Initialize the first slot
    for j in range(n_products):
        dp[0][j] = exposure_rates[0] * products_sorted[j][1]

    # Fill the DP table
    # dp[i][j]= max (dp[i−1][k]+exposure_rates[i]×products_sorted[j][1]), k<=j, price[k]>=price[j]
    for i in range(1, n_slots):
        for j in range(n_products):
            # We can only choose products k where price[k] >= price[j], i.e., k <= j since sorted
            max_prev = -float('inf')
            best_k = -1
            for k in range(j + 1):
                if dp[i - 1][k] > max_prev:
                    max_prev = dp[i - 1][k]
                    best_k = k
            if best_k != -1:
                dp[i][j] = max_prev + exposure_rates[i] * products_sorted[j][1]
                parent[i][j] = best_k

    # Find the maximum score in the last slot
    max_score = -float('inf')
    last_product = -1
    for j in range(n_products):
        if dp[n_slots - 1][j] > max_score:
            max_score = dp[n_slots - 1][j]
            last_product = j

    # Reconstruct the sequence
    sequence = []
    current = last_product
    for i in range(n_slots - 1, -1, -1):
        sequence.append(products_sorted[current])
        current = parent[i][current]
    sequence.reverse()

    return max_score, sequence


# Example usage:
products = [(10, 5), (8, 3), (8, 4), (5, 2), (5, 3), (3, 1)]  # Example products
exposure_rates = [0.9, 0.8, 0.7, 0.6]  # Example exposure rates
max_score, sequence = max_exposure_score(products, exposure_rates)
print("Maximum Exposure Score:", max_score)
print("Optimal Product Sequence:")
for idx, (price, score) in enumerate(sequence):
    print(f"Slot {idx + 1}: Price = {price}, Score = {score}, Exposure = {exposure_rates[idx]}")