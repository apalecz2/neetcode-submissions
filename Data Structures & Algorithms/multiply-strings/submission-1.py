class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        # hashmap for char to int
        # modulo and x 10 ops for conversion

        mapping = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        mapping_r = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}

        int1 = 0
        for i in range(len(num1)):
            v = num1[i]

            vi = mapping[v]

            dec_place = len(num1) - 1 - i
            
            int1 += (10 ** dec_place) * vi
        
        int2 = 0
        for i in range(len(num2)):
            v = num2[i]

            vi = mapping[v]

            dec_place = len(num2) - 1 - i
            
            int2 += (10 ** dec_place) * vi

        print(int1)

        product = int1 * int2

        str_prod = ""

        while product:
            digit = product % 10
            product = product // 10
            str_prod += mapping_r[digit]

        if str_prod == "":
            return "0"

        return str_prod[::-1]
        