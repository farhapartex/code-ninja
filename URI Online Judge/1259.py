if __name__ == "__main__":
    try:
      test = int(input())
      even, odd = [], []

      for i in range(0, test):
          n = int(input())
          odd.append(n) if n&1 else even.append(n)
      even = sorted(even)
      odd = sorted(odd, reverse=True)
      even.extend(odd)
      for n in even:
        print(n)
    except:
      pass