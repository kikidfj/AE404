def testCallByRef(ref):
    ref[0] = ref[0] + 1
    return 0
    
def testCallByVal(val):
    val += 1
    return 0

if __name__ == '__main__':
    ref = [3]
    val = 3
    testCallByRef(ref)
    testCallByVal(val)
    print("val = " + str(val))
    print("ref = " + str(ref[0]))