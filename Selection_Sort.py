def Selection_Sort(a_list):
    n = len(a_list)

    for i in range(n-1, -1, -1):

        iMin = i

        for j in range(i-1,-1,-1 ):

            if a_list[j] > a_list[iMin]:
                iMin = j

        temp = a_list[i]
        a_list[i] = a_list[iMin]
        a_list[iMin] = temp
        print('รอบที่', len(a_list)-i, a_list)
    return a_list

if __name__ == '__main__':
    a_list = [2, 7, 4, 1, 5, 3]
    print('ข้อมูล', a_list)
    print('หลังจากการจัดเรียง', Selection_Sort(a_list))