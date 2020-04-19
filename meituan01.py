# 题目描述：
# 有一个很经典的问题是，当前时间是aa:bb,请问若干分钟后是什么时间？我们今天的问题是一个相反的问题。
#
# 已知现在的时刻是星期x的yy:zz时刻，请问n分钟前是周几，时间是多少。
#
# 例如现在是周三，02:10,则200分钟之前，应该是周二，22:50。
#
# 输入
# 输入包含三行
#
# 第一行一个正整数x，表示今天是周x。(1<=x<=7)
#
# 第二行是一个24小时制的时间表示，时和分均含前导0，例如，1时1分表示为01:01。保证时间格式是合法的。
#
# 第三行是一个正整数n，表示要求的是n分钟之前的时间。(1<=n<=10^9)
#
# 输出
# 输出同样包含两行，第一行仅包含一个正整数，表示n分钟之前是周几。
#
# 一个24小时制的时间表示，时和分均含前导0，例如，1时1分表示为01:01。表示n分钟之前的时刻。
#
#
# 样例输入
# 3
# 02:10
# 200
# 样例输出
# 2
# 22:50


def test(x, time, n):
    hour, minute = map(int, str(time).split(":"))
    minute_temp = (n - (hour * 60 + minute))

    if minute_temp > 0:  # 超过一天了
        # x = (x - (minute_temp // (60 * 24) + 1))
        if minute_temp % (60 * 24) == 0:
            temp = minute_temp // (60 * 24)
        else:
            temp = (minute_temp // (60 * 24)) + 1

        if x - temp > 0:
            x = (x - temp)
        elif x - temp == 0:
            x = 7
        else:
            x = 7 - (temp % 7) + 1
        minute_temp = minute_temp % (60 * 24)

        hour_new = (24 * 60 - minute_temp) // 60 % 24
        minute_new = (24 * 60 - minute_temp) % 60

    else:
        hour_new = ((hour * 60 + minute) - n) // 60 % 24
        minute_new = ((hour * 60 + minute) - n) % 60
    print(x)
    if hour_new < 10:
        hour_new = "0" + str(hour_new)
    if minute_new < 10:
        minute_new = "0" + str(minute_new)
    print(str(hour_new) + ":" + str(minute_new))


if __name__ == '__main__':
    x = int(input())
    time = input()
    n = int(input())

    test(x, time, n)
