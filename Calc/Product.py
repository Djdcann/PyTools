def get_products_of_all_ints_except_at_index(the_list):
    result = [None] * len(the_list)

    #loop thru forwards
    prod = 1
    for i in xrange(len(the_list)):
        result[i] = prod
        prod *= the_list[i]

    #loop thru backwards
    prod = 1
    for i in xrange(len(the_list)-1, -1, -1):
        result[i] *= prod
        prod *= the_list[i]

    print result

    return result


if __name__ == '__main__':
    get_products_of_all_ints_except_at_index([1, 7, 3, 4])
