from timeit import default_timer as timer


def bottles(number):
    for count in range(number, 0, -1):
        print(f"{count} Green Bottles, standing on the wall,\n{count} Green Bottles, "
              f"standing on the wall,\nand if one green bottle should accidently fall,"
              f"\nthey'll be {count-1} Green Bottles, standing on the wall.")

start = timer()
bottles(10000)
end = timer()
print("Time taken to execute (seconds):", end - start)
# Time in seconds, e.g. 5.38091952400282