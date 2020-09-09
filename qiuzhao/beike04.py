# -*- coding: utf-8 -*-
# @Time : 2020/9/7 2:59 下午
# @Author : ddz

# include<bits/stdc++.h>
# using
# namespace
# std;
# const
# int
# INF = 0x3f3f3f3f;
#
# int
# main()
# {
#     int
# T, n, q, x, y, z, sum;
# cin >> T;
# while (T - -)
#     {
#         cin >> n;
#     vector < int > num;
#     map < int, int > mmp;
#     for (int i=0;i < n;i++)
#     {
#         int tmp;
#     cin >> tmp;
#     num.push_back(tmp);
#     mmp[tmp] = (mmp[tmp] < i & & mmp[tmp] != 0?mmp[tmp]:i);
#
#     }
#     sort(num.begin(), num.end());
#     cin >> q;
#     for (int i=0;i < q;i++)
#     {
#         cin >> x >> y >> z;
#     sum = x * y * z;
#     int pos1=lower_bound(num.begin(), num.end(), sum)-num.begin();
#     pos1--;
#     if (pos1 < 0)
#     {
#     cout << "-1" << endl;
#     continue;
#     }
#     cout << mmp[num[pos1]] + 1 << " " << num[pos1] << endl;
#     }
#
#     }
#     }