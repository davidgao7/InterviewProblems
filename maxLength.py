class A:
    def maxLength(self, arr):
        # write code here
        res = 0
        l = list()
        for i in arr:
            while i in l:  # 如果一直有，就把在重复
                l.pop(0)
                print(l)
            l.append(i)  # 剔除之后再加上一个保底
            print(l)
            res = max(res, len(l))  # 一直保留最大的
        return res
a = A()
arr = [10174, 22971, 3540, 589, 26054, 24343, 5283, 10613, 15564, 30419, 28743, 16962, 12924, 3002, 11504, 623, 22203,
       6892, 3276, 14022, 18747, 29478, 23093, 7301, 15692, 31043, 10793, 27142, 28661, 5635, 8954, 19103, 17475, 12556,
       6982, 20936, 31201, 23854, 9514, 10619, 12777, 6635, 22963, 32737, 13818, 20023, 30869, 30762, 13707, 24700,
       12320, 8892, 28030, 4065, 8559, 16529, 28152, 29388, 29923, 21978, 29297, 16037, 4816, 20457, 7, 15582, 21621,
       16973, 15896, 4400, 16690, 32575, 15631, 13607, 11253, 3901, 8062, 19680, 17654, 19444, 22894, 14610, 29604,
       8803, 31219, 2635, 3294, 16446, 13059, 14716, 14695, 12432, 4999, 18872, 8340, 11173, 10163, 14137, 11080, 7719,
       29587, 22436, 29474, 11143, 31719, 3981, 12789, 12190, 20785, 318, 17785, 917, 20748, 6324, 6976, 2562, 4543,
       6379, 6379, 18003, 11282, 3676, 21661, 880, 22369, 19139, 12720, 19868, 3054, 20005, 13735, 17308, 8059, 16658,
       10596, 796, 4121, 25640, 23196, 13390, 28987, 6360, 4487, 30932, 12046, 26477, 3804, 16864, 7181, 9801, 9724,
       20890, 31952, 9842, 18285, 27586, 1572, 2382, 3979, 31126, 353, 9131, 11642, 9462, 2808, 4610, 13919, 11974,
       8012, 25085, 14544, 1172, 27075, 30006, 9353, 22906, 2588, 322, 23136, 17990, 17411, 20718, 30843, 13529, 19682,
       10952, 14016, 6861, 11259, 226, 26509, 18267, 24756, 19922, 28841, 18555, 17201, 17149, 20603, 11084, 21288,
       11286, 890, 7095, 26865, 11233, 24037, 10063, 31965, 13885, 11700, 10108, 30921, 27489, 14542, 5849, 18419,
       14438, 27516, 21978, 6412, 24838, 19230, 8882, 1678, 22179, 285, 18548, 6479, 138, 4640, 18808, 22871, 22906,
       5507, 2304, 24814, 1632, 261, 14363, 9722, 19045, 23744, 2506, 28040, 31786, 29535, 29282, 7593, 24658, 21131,
       30257, 24959, 3394, 12198, 19300, 21399, 15396, 1212, 21288, 8825, 11058, 31158, 11792, 25470, 30001, 28113,
       28599, 2018, 571, 13647, 13734, 10266, 30146, 24429, 9592, 6504, 15826, 6292, 5692, 428, 10134, 31955, 26906,
       23933, 7454, 28301, 21818, 11384, 28767, 17775, 10977, 14296, 22396, 27045, 20957, 10056, 32324, 12110, 1828,
       22517, 20731, 1581, 7608, 10726, 25693, 20897, 18125, 14224, 7904, 31959, 9518, 11173, 1850, 7998, 12253, 10542,
       23587, 17723, 10233, 31193, 22876, 12575, 9701, 30356, 19952, 10326, 423, 24154, 26554, 8416, 6798, 3917, 22567,
       25350, 16920, 22022, 13885, 29509, 19986, 18217, 16860, 22671, 5633, 22332, 27716, 4787, 24513, 9401, 18904,
       21785, 32620, 10337, 20770, 2]
print("arr length: %d" % (len(arr)))
ans = s.maxLength(arr)
print(ans)
ans1 = a.maxLength(arr)
print(ans1)
