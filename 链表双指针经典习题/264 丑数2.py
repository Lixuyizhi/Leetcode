class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 理解为三个指向有序链表头结点的指针
        p2, p3, p5 = 1, 1, 1
        # 理解为三个有序链表的头节点的值
        product2, product3, product5 = 1, 1, 1
        # 理解为最终合并的有序链表（结果链表）
        ugly = [0] * (n + 1)
        # 理解为结果链表上的指针
        p = 1

        # 开始合并三个有序链表，找到第 n 个丑数时结束
        while p <= n:
            # 取三个链表的最小结点
            min_val = min(product2, product3, product5)
            # 将最小节点接到结果链表上
            ugly[p] = min_val
            p += 1
            # 前进对应有序链表上的指针
            if min_val == product2:
                product2 = 2 * ugly[p2]
                p2 += 1
            if min_val == product3:
                product3 = 3 * ugly[p3]
                p3 += 1
            if min_val == product5:
                product5 = 5 * ugly[p5]
                p5 += 1

        # 返回第 n 个丑数
        return ugly[n]

solution = Solution()
print(solution.nthUglyNumber(100))