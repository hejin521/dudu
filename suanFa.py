class Solution:
    def twoSum(self, nums, target):
        """
        数组的和
        :param nums:
        :param target:
        :return:
        """
        lenth = len(nums)
        for i in range(lenth):
            for j in range(i + 1, lenth):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def reversedList(self, head):
        '''
        反转链表
        :param head:
        :return:
        '''
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    def invaildStr(self, str):
        '''
        有效的括号
        :param str:
        :return:
        '''
        if len(str)%2 == 1:
            return False
        char = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack = list()
        for s in str:
            if s in char:
                if not stack or stack[-1] != char[s]:
                    return False
                stack.pop()
            else:
                stack.append(s)
        return not stack


    def huiWen(self,shuzi):
        '''
        回文数字
        :param shuzi:
        :return:
        '''
        strshuzi = str(shuzi)
        count = False
        i = 0
        l = len(strshuzi)
        while i <= l/2:
            if strshuzi[i] == strshuzi[l-i-1]:
                count = True
                i+=1
            else:
                return False
                break
        return count

    def kuaimanzhizhen(self, list1):
        '''
        删除有序数组的重复数字，并返回新长度
        :param list1:
        :return:
        '''
        if not list1:
            return 0
        fast = slow =1
        lenth1 = len(list1)
        while fast < lenth1:
            if list1[fast] != list1[fast-1]:
                list1[slow] = list1[fast]
                slow += 1
            fast += 1
        return slow


    def kuaimanzhizhen2(self, list2, num1):
        '''
        删除数组中包含某个数的部分，并返回新长度
        :param list2:
        :return:
        :num1:
        '''
        if not list2:
            return 0
        fast1 = slow1 =0
        lenth1 = len(list2)
        while fast1 < lenth1:
            if list2[fast1] != num1:
                list2[slow1] = list2[fast1]
                slow1 += 1
            fast1 += 1
        return slow1

    def charushuzi(self, list3, num3):
        '''
        查找 num3 在排序数组的位置，如果不在，则返回插入位置
        :param list3:
        :param num3:
        :return:
        '''
        for i in range(len(list3)):
            if list3[i] >= num3:
                return i
        return len(list3)

    def liebiaoSum(self,digits):
        '''
        给一个数组，加1后返回数组
        :param list4:
        :return:
        '''
        list5 =list()
        for i in digits:
            list5.append(str(i))
        int1 = int(''.join(list5))+1
        string3 = str(int1)
        liststring = list(string3)
        listint = list()
        for j in liststring:
            listint.append(int(j))
        return list(listint)


    def luomashuzi(self, strxila):
        '''
        罗马字符转成数字
        :param strxila:
        :return:
        '''
        end = 0
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        if 'IV' in strxila:
            strxila = strxila.replace('IV', '')
            end += 4
        if 'IX' in strxila:
            strxila = strxila.replace('IX', '')
            end += 9
        if 'XL' in strxila:
            strxila = strxila.replace('XL', '')
            end += 40
        if 'XC' in strxila:
            strxila = strxila.replace('XC', '')
            end += 90
        if 'CD' in strxila:
            strxila = strxila.replace('CD', '')
            end += 400
        if  'CM' in strxila:
            strxila = strxila.replace('CM', '')
            end += 900
        for i in strxila:
            end+=dic[i]
        return end

    def paixu(self, shuzu):
        '''
        冒泡排序从大到小
        :param shuzu:
        :return:
        '''
        l =len(shuzu)
        for i in range(l):
            for j in range(0,l-i-1):
                if shuzu[j] < shuzu[j+1]:
                    shuzu[j],shuzu[j+1]=shuzu[j+1],shuzu[j]
        return shuzu


    def paolouti(self, num):
        '''
        爬楼梯，一次爬1或者2个，给一个阶梯数，几种爬法
        :param num:
        :return:
        '''
        s=[1,2]
        if num <=2:
            return s[num-1]
        while len(s) < num:
            s.append(s[-1]+s[-2])
        return s[-1]



solution = Solution()
# print(solution.twoSum([2, 4, 5, 6], 10))
# print(solution.invaildStr("()[]{}"))
# print(solution.huiWen(21212))
# print(solution.kuaimanzhizhen2([0,1,3,3,4,5],0))
# print(solution.charushuzi([1,3,5,6],9))
# print(solution.liebiaoSum([2,4,9]))
# print(solution.luomashuzi('DCLXXVI'))
# print(solution.paixu([9,0,0,0,8,1]))
print(solution.paolouti(6))