### 1初级排序

##### a 选择排序

- **简单原理**

  找出序列中最小元素重新排列成一个新序列

  1. 找到列表中最小的元素
  2. 和列表第一个元素交换位置，即把最小元素放到第一位
  3. 从剩下的列表中继续找到最小的元素，和列表第二个元素交换位置，即放到第二位
  4. 以此类推，直到遍历完成整个列表，得到一个从小到大排列的列表

- python算法实现

  ```python
  def findSmallest(attr):
      '''
      找出最小值
      :param attr:
      :return:
      '''
      smallIndex = 0
      smallAttr = attr[smallIndex]
  
      for itemIndex in range(len(attr)):
          if attr[itemIndex] < smallAttr:
              smallAttr = attr[itemIndex]
              smallIndex = itemIndex
      return smallIndex
  
  
  def selectSort1(sortList):
      '''
      选择排序方法1
      :param sortList:
      :return:
      '''
      newList = []
      for i in range(len(sortList)):
          smallIndex = findSmallest(sortList)
          newList.append(sortList.pop(smallIndex))
      return newList
  
  
  def selectSort2(sortList):
      '''
      选择排序方法2
      :param sortList:
      :return:
      '''
      for i in range(len(sortList)):
          smallIndex = findSmallest(sortList[i:])
          sortList[i], sortList[i + smallIndex] = sortList[i:][smallIndex], sortList[i]
      return sortList
  
  
  if __name__ == '__main__':
      srcList = [4, 2, 5, 3, 9, 1, 6]
      print(selectSort1(srcList))
      srcList = [4, 2, 5, 3, 9, 1, 6]
      selectSort2(srcList)
      print(srcList)
  ```

- 性能分析

  1. 对于长度为N的列表，执行一遍排序需要进行N次交换以及(N-1)+(N-2)+...+2+1=N(N-1)/2~N2/2次笔记
  2. 选择排序运行时间和输入无关，不论输入的列表是否有序，都需要挨个遍历
  3. 每次扫描都会交换一次元素，一共交换N次，和列表长度是线性关系

##### b 插入排序

- **简单原理**

  将一个元素插入到一个已经有序的列表中，方法如下

1. 从左到右遍历列表
2. 当前元素左边的子序列都是有序的
3. 用当前元素与左边子序列元素挨个比较，与比当前元素大的元素互换位置，或者把比当前元素大的元素右移，直到找到正确的插入位置，再插入当前元素
4. 取下一个元素重复上一步操作
5. 遍历到最右侧元素后排序完成

- **python代码实现**

  ```python
  def insertsort1(srcList):
      '''
      插入排序
      :param srcList:
      :return:
      '''
      for i in range(len(srcList)):
          key = srcList[i]
          j = i - 1
          while j >= 0:
              if srcList[j] > key:
                  srcList[j + 1], srcList[j] = srcList[j], key
              j = j - 1
      return srcList
  
  
  def insertsort2(srcList):
      '''
      插入排序实现2，相比实现1减少了元素互换，提高处理效率
      :param srcList:
      :return:
      '''
      for i in range(len(srcList)):
          key = srcList[i]
          j = i - 1
          while j >= 0 and srcList[j] > key:
              srcList[j + 1] = srcList[j]
              j = j - 1
          srcList[j + 1] = key
      return srcList
  
  
  if __name__ == '__main__':
      print(insertsort2([5, 3, 6, 1, 8, 7, 4]))     
  ```

  - **性能分析**

    插入排序时间复杂度为O(n2),，但是比较次数取决于列表中倒置的元素数量，对于部分有序的列表，插入排序效率很高 

  ##### c 希尔排序

  - **简单原理**

    希尔排序是基于插入排序改进的一种快速排序方法，适用于大规模乱序序列的排序，插入排序每次只能移动一位数据，在处理大量乱序数据时效率低下，希尔排序则使用分组对各个分组使用插入排序，随着分组的调整完成整个序列的排序，方法如下：

    1. 构造一个有序序列，h1...h2...h3.....hn，取一个小于序列长度的整数hn做为初始间隔
    2. 把序列中相同hn间隔的数据算作一组进行插入排序
    3. 第一组插入排序完成后，按hn-1继续进行分组插入排序
    4. 间隔降为1后相当于一个基本有序的插入排序，执行插入排序后完成排序

  - **python代码实现**

  ```python
  def shellsort(srclist):
      lenth = len(srclist)
      h = 1
      while h < lenth // 3:
          h = 3 * h + 1
      while h >= 1:
          index= h
          while index < lenth:
              jindex = index
              while jindex >= h and srclist[jindex] < srclist[jindex - h]:
                  exch(srclist, jindex, jindex - h)
                  jindex -= h
              index+=1
          h = h // 3
      return srclist
  
  
  def exch(alist, srcindex, destindex):
      temp, alist[srcindex] = alist[srcindex], alist[destindex]
      alist[destindex] = temp
  
  
  if __name__ == '__main__':
      print(shellsort([4, 2, 5, 7, 2, 6, 8, 5, 1, 4, 8, 5, 7, 1, 8, 3, 1, 5, 7, 8, 2, 1]))
  ```

  - 性能分析

    希尔排序的性能与选取的间隔序列有关，好的增量序列有如下特点：

    1. 最后一个增量必须为1
    2. 避免序列中的值(尤其时临近的值)互为倍数的情况出现

    希尔排序的时间性能优于插入排序，原因主要为：

    1. 当序列初始状态较为有序时插入排序比较和移动次数少，执行效率高，而希尔排序前期的大间隔排序相当于数据预处理，使无序序列越来越有序
    2. 希尔排序前期大间隔排序时，由于分组较少，排序效率也不会低

    希尔排序时间复杂读大于O(n2)，但是具体时间复杂度取决于序列和间隔，理论上最好的复杂度为O(nlog2n)，适用于中等规模序列排序

  ##### d 归并排序

  - **简单原理**

    ​	把需要排序的序列分成两半分别排序，然后再把两个有序序列归并成一个有序序列，分开的子序列的排序方法可以是递归调用归并排序的方法来实现，也可以使用其他排序方法实现

    ​	实现归并排序首先需要实现的是一个归并方法，把两个有序子序列归并为一个有序序列，有两种实现方法：

    ​	第一种方法接受两个有序子序列做参数，返回一个归并后的新序列，参见下面的merge_tow_sublist(first_sub_list, second_sub_list)方法，这种方法的缺陷在于每次递归都要有新序列占用空间，空间复杂度较高，优化后可以采用第二种实现方法，参见inner_list_merge(src_list, lo, mid, hi)方法，直接对传入的列表进行本地归并排序，方法中要指明待排序的子列表起始序列和中间索引

    ​	实现归并方法后，就可以使用递归调用的方法实现排序 

  - **python代码实现**

    ```python
    def merge_tow_sublist(first_sub_list, second_sub_list):
        '''
        输入两个有序子序列进行归并排序,实现方法1
        :param first_sub_list:
        :param second_sub_list:
        :return:
        '''
        temp_list = []
        first_list_index = 0
        first_list_lenth = len(first_sub_list)
        second_list_lenth = len(second_sub_list)
        second_list_index = 0
        for k in range(len(first_sub_list) + len(second_sub_list)):
            if first_list_index >= first_list_lenth:  # 左半部分的序列元素已经取尽,取右半部分下一个元素
                temp_list.append(second_sub_list[second_list_index])
                second_list_index += 1
            elif second_list_index >= second_list_lenth:  # 右半部分的序列元素已经取尽，取左半部分的下一个元素
                temp_list.append(first_sub_list[first_list_index])
                first_list_index += 1
    
            elif first_sub_list[first_list_index] >= second_sub_list[second_list_index]:  # 左右各取一个元素比较，取较小的元素
                temp_list.append(second_sub_list[second_list_index])
                second_list_index += 1
            else:
                temp_list.append(first_sub_list[first_list_index])
                first_list_index += 1
        return temp_list
    
    
    def merge_tow_sublist_n(first_sub_list, second_sub_list):
        '''
        输入两个有序子序列进行归并排序,实现方法2
        :param first_sub_list:
        :param second_sub_list:
        :return:
        '''
        temp_list = []
        first_list_index = second_list_index = 0
        while second_list_index < len(first_sub_list) and first_list_index < len(second_sub_list):
            if first_sub_list[second_list_index] < second_sub_list[first_list_index]:
                temp_list.append(first_sub_list[second_list_index])
                second_list_index += 1
            else:
                temp_list.append(second_sub_list[first_list_index])
                first_list_index += 1
    
        if second_list_index == len(first_sub_list):
            for element in second_sub_list[first_list_index:]:
                temp_list.append(element)
        else:
            for element in first_sub_list[second_list_index:]:
                temp_list.append(element)
    
        return temp_list
    
    
    def inner_list_merge(src_list, lo, mid, hi):
        '''
        对列表指定子序列原地归并排序
        :param src_list: 需要排序的数组
        :param lo: 子序列起始索引
        :param mid: 子序列中间索引，左右都是有序数组
        :param hi: 子序列结尾索引
        :return:
        '''
        first_list_index = lo
        second_list_index = mid + 1
        temp_list = src_list[:]  # 使用临时变量保存列表内容
        k=lo
        while k < len(temp_list):
            if first_list_index > mid:  # 左半部分的序列元素已经取尽,取右半部分下一个元素
                src_list[k] = temp_list[second_list_index]
                second_list_index += 1
            elif second_list_index > hi:  # 右半部分的序列元素已经取尽，取左半部分的下一个元素
                src_list[k] = temp_list[first_list_index]
                first_list_index += 1
            elif temp_list[first_list_index] >= temp_list[second_list_index]:  # 左右各取一个元素比较，取较小的元素
                src_list[k] = temp_list[second_list_index]
                second_list_index += 1
            else:
                src_list[k] = temp_list[first_list_index]
                first_list_index += 1
            k+=1
    
    
    def merge_sort(src_list):
        '''
        普通归并排序
        :param src_list:
        :return:
        '''
        if len(src_list) <= 1:  # 不需要再拆分排序，直接返回
            return src_list
        mid = len(src_list) // 2
        left = merge_sort(src_list[:mid])  # 左半部分递归调用排序
        right = merge_sort(src_list[mid:])  # 右半部分递归调用排序
        return merge_tow_sublist(left, right)  # 将左右两个有序序列归并为一个有序序列
    
    
    def merge_sort_inner(src_list, lo, hi):
        '''
        原地归并排序，不用每次递归都产生一个新的列表
        :param src_list: 需要排序的列表
        :param lo: 需要排序的子列表起始元素序号
        :param hi: 需要排序的子列表终点元素序号
        :return:
        '''
        if lo >= hi:  # 不需要再拆分排序，直接返回
            return
        mid = lo + (hi - lo) // 2
        merge_sort_inner(srcList, lo, mid)  # 左半部分递归调用原地排序
        merge_sort_inner(srcList, mid + 1, hi)  # 右半部分递归调用原地排序
        inner_list_merge(srcList, lo, mid, hi)  # 将左右两个有序序列原地归并为一个有序序列
    
    
    if __name__ == '__main__':
        srcList = [1, 3, 6, 7, 9, 2, 4, 7, 8, 10, 12]
        inner_list_merge(srcList, 0, 4, 9)
        print(srcList)
        srcList = [1,4,2,6,3,6,9,2,1,7,9]
        merge_sort_inner(srcList,0,10)
        print(srcList)
        subList1 = [1, 3, 6, 7, 9]
        subList2 = [2, 4, 7, 8, 10, 12]
        print(merge_tow_sublist(subList1, subList2))
        sort_list = [3, 5, 2, 4]
        merge_sort(sort_list)
        print(merge_sort(sort_list))
    ```

    - 性能分析

      归并排序速度远大于选择排序和插入排序，对于长度为N的数组，自顶向下的排序最多需要进行NlogN次比较。最多访问数组6NlgN次

    - 算法优化

      1 对于小规模数组使用插入排序

      - 优化点

        ​	归并排序采用的递归调用，对于小规模问题存在递归调用过于频繁的问题，对这一点，可以使用插入排序替代，降低过多的递归开销

      - python实现

        ```python
        def merge_sort_inner_with_insert(src_list, lo, hi):
            '''
            原地归并排序，不用每次递归都产生一个新的列表,数组长度小于4时使用插入排序
            :param src_list: 需要排序的列表
            :param lo: 需要排序的子列表起始元素序号
            :param hi: 需要排序的子列表终点元素序号
            :return:
            '''
            if hi - lo <= 4:  # 不需要再拆分排序，直接返回
                insertsort.insertsort2(srcList[lo:hi])
            mid = lo + (hi - lo) // 2
            merge_sort_inner(srcList, lo, mid)  # 左半部分递归调用原地排序
            merge_sort_inner(srcList, mid + 1, hi)  # 右半部分递归调用原地排序
            inner_list_merge(srcList, lo, mid, hi)  # 将左右两个有序序列原地归并为一个有序序列
        ```

      2 测试数组是否有序

      - 优化点

        同样为了降低递归次数，由于每次递归时，左右两个子数组都是有序，所以可以通过判断左数组最后一个值和右数组第一个值是否有序，如果有序可以直接返回，不需要再递归归并

      - python实现

        ```python
        def merge_sort_inner_with_insert(src_list, lo, hi):
            '''
            原地归并排序，不用每次递归都产生一个新的列表,数组长度小于4时使用插入排序
            :param src_list: 需要排序的列表
            :param lo: 需要排序的子列表起始元素序号
            :param hi: 需要排序的子列表终点元素序号
            :return:
            '''
            if hi - lo <= 4:  # 不需要再拆分排序，直接返回
                insertsort.insertsort2(srcList[lo:hi])
                return
            mid = lo + (hi - lo) // 2
            merge_sort_inner(srcList, lo, mid)  # 左半部分递归调用原地排序
            merge_sort_inner(srcList, mid + 1, hi)  # 右半部分递归调用原地排序
            if srcList[mid] <= srcList[mid+1]:  #分别有序的子数组如果已经彼此有序，可以直接返回
                return 
            inner_list_merge(srcList, lo, mid, hi)  # 将左右两个有序序列原地归并为一个有序序列
        ```

        

      3 不将元素复制到辅助数组

      - 优化点

        每次原地归并都要将数组复制到辅助数组，可以考虑优化这个时间开销

      - python代码实现

        ```python
        
        ```

  - 自顶向下的归并排序

