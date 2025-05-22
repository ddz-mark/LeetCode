

def test(nums, k):


    #

    nums = sorted(nums, lambda key: -key if key<0 else key, reverse=True)

    sum = 1
    for i in range(k):
        sum *= nums[i]

    if sum > 0:
        return sum
    else:
        for v in nums[:k][::-1]:
            if v < 0:
                min_x = v
                break
        for v in nums[:k][::-1]:
            if v > 0:
                min_y = v
                break

        for v in nums[k:]:
            if v > 0:
                max_x = v
                break
        for v in nums[k:]:
            if v < 0:
                max_y = v
                break


        sum = max(sum/min_x * max_x, sum/min_y * max_y)

    return sum



