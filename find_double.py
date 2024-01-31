def find_doubles_in_list(values):
    """
    n integeres, find all elements of the list
    there eixists exactly one element of the list
    which is twice that number

    e.g.
    1 1 2 -> 1 1
    explain: 1 and 1 both have their double 2 present, and 2 is present in the list
    only once
    """
    # test case 9: [0... and then 0~999] exitst (999+1)/2
    # Write your code here
    # drop duplicates
    import pandas as pd
    import numpy as np

    value_counts_dict = pd.DataFrame(np.array(values)).value_counts()
    result = []
    for number, occurance in value_counts_dict.items():
        if (
            number[0] * 2 in value_counts_dict.keys()
            and value_counts_dict[number[0] * 2] == 1
        ):
            result+=[number[0]]*occurance

    result.sort()
    ans = ""
    
    for i in range(0, len(result)):
        if i < len(result) - 1:
            ans += str(result[i])
            ans += " "
        else:
            ans += str(result[i])
    print(ans)


if __name__ == "__main__":
    values =[3,1,1,2]
    print(
        find_doubles_in_list(values)
    )  # [0, 1,2,3]  8 is 4*2 but 8 appear twice, 0 is its own double, so in result
