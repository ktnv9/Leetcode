
def product_except_self(nums):

    # initialize the prefix and suffix products
    num_elements = len(nums)
    prefix_prod_list = [1] * num_elements
    suffix_prod_list = [1] * num_elements

    # first prefix product is the first element of the input list by default.
    prefix_prod_list[0] = nums[0]
    
    # last siffix product is the last element of the input list by default.
    suffix_prod_list[num_elements-1] = nums[num_elements-1]

    for index in range(1,num_elements):

        # compute the prefix product list by multiplicating previous prefix product with current element.
        prefix_prod_list[index] = prefix_prod_list[index-1] * nums[index]

        # compute the suffix product list by multiplicating next suffix product with current element.
        suffix_prod_list[num_elements-1-index] = suffix_prod_list[num_elements-index] * nums[num_elements-1-index]

    # compute the product except self by right-diagonally multiplying the prefix and suffix prod list elements.
    output_list = [1]*num_elements
    for index in range(num_elements):

        # handle index out of range issue for prefix product.
        if index == 0:
            pf_prod = 1
        else:
            pf_prod = prefix_prod_list[index-1]

        # handle index out of range issue for suffix product.
        if index == num_elements-1:
            sf_prod = 1
        else:
            sf_prod = suffix_prod_list[index+1]
        
        output_list[index] = pf_prod * sf_prod

    return output_list

nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
output = product_except_self(nums)

print(output)




