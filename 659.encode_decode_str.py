"""
Description
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Only $39.9 for the "Twitter Comment System Project Practice" within a limited time of 7 days!

WeChat Notes Twitter for more information（WeChat ID jiuzhangfeifei）


Because the string may contain any of the 256 legal ASCII characters, your algorithm must be able to handle any character that may appear

Do not rely on any libraries, the purpose of this problem is to implement the "encode" and "decode" algorithms on your own

Example
Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
"""


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    time complexity: O(n)
    speace complexity: O(n)
    """

    def encode(self, strs):
        # write your code here
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        # write your code here
        res, i = [], 0  # i: what postion we are at

        while i < len(str):
            j = i
            # print(f"j:{j}, str:{str}")
            # print(f"str[j]:{str[j]}")
            while str[j] != "#":
                j += 1

            # onece we find the #, we know the length of the string
            length = int(
                str[i:j]
            )  # how many following characters we need to read after j inorder to get every character of the str
            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.encode(["lint", "code", "love", "you"]))
    print(s.decode("4#lint4#code4#love3#you"))
    # print(s.encode(["we", "say", ":", "yes"]))
    # print(s.decode("2#we3#say1#:3#yes"))
