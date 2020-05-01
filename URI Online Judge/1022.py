def get_gcd(a,b):
    if b == 0:
        return a
    return get_gcd(b, a%b)


if __name__ == "__main__":
    try:
        test = int(input())
        
        for i in range(0, test):
            expression = input().replace(" ", "")
            if '+' in expression or '-' in expression or '*' in expression:
                if "+" in expression:
                    numbers = expression.split('+')
                elif "-" in expression:
                    numbers = expression.split('-')
                else:
                    numbers = expression.split('*')       

                n1, d1 = int(numbers[0].split("/")[0]), int(numbers[0].split("/")[1])
                n2, d2 = int(numbers[1].split("/")[0]), int(numbers[1].split("/")[1])
                if "+" in expression:
                    num_res1 = (n1*d2 + n2*d1)
                elif "-" in expression:
                    num_res1 = (n1*d2 - n2*d1)
                else:
                    num_res1 = (n1*n2)
                denum_res1 = d1*d2
                gcd = get_gcd(num_res1, denum_res1)
                num_res2 = num_res1 // gcd
                denum_res2 = denum_res1 // gcd
                print("{0}/{1} = {2}/{3}".format(num_res1, denum_res1, num_res2, denum_res2))
            
            else:
                numbers = expression.split("/")
                n1, d1, n2, d2 = [int(n) for n in expression.split("/")]
                num_res1 = n1*d2
                denum_res1 = n2*d1
                gcd = get_gcd(num_res1, denum_res1)
                num_res2 = num_res1 // gcd
                denum_res2 = denum_res1 // gcd
                print("{0}/{1} = {2}/{3}".format(num_res1, denum_res1, num_res2, denum_res2))
            

    except:
        pass