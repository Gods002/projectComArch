def numToBinary(n,rangeOffbit):
    result = ''
    for x in range(rangeOffbit):
        r = n % 2
        n = n // 2
        result += str(r)
    result = result[::-1]
    return result

# ---------------- Error check ------------------
# not complete all
def error_detect(mchcodee):
    listop = ['000','001','010','011','100','101','110','111']

    if len(mchcodee)!= 32:
        print('ERROR Machinecode out of bound!!!')
    elif mchcodee[22:25] not in listop: # opcode check
        print('ERROR Opcode not found!!!')
    elif mchcodee[25:32] != '0000000': # bit 25-31 is 0
        print('ERROR syntax error!!!!')
    else: print('Anything is pass!!!')