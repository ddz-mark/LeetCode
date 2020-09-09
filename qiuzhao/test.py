# -*- coding: utf-8 -*-
# @Time : 2020/9/6 8:06 下午
# @Author : ddz

# 1. 链表的公共部分 python
def printCommonPart(head1, head2):
    print("Common Part:")
    while head1 and head2:
        if head1.elem < head2.elem:
            head1 = head1.next
        elif head1.elem > head2.elem:
            head2 = head2.next
        else:
            print(head1.elem, end=" ")
            head1 = head1.next
            head2 = head2.next

# 1. 链表的公共部分 java
# public static void CommonPrint(Node head1,Node head2){
#         System.out.println("Common Part:");
#         while (head1.next != null && head2.next != null) {
#             if (head1.value < head2.value) {
#                 head1 = head1.next;
#             } else if (head2.value < head1.value) {
#                 head2 = head2.next;
#             } else {
#                 System.out.print(head1.value+" ");
#                 head1 = head1.next;
#                 head2 = head2.next;
#             }
#         }
#         System.out.println();
#     }