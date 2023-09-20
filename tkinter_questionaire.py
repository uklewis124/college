import rng_module

def main():
    rng = rng_module.OscarRNG()
    while True:
        dice_type = input("Enter dice type (D4, D6, D12, D20): ")
        if dice_type.upper() == "D4":
            dice_total = rng.next(1,5)
            print(f"D4 {dice_total}")
            continue
        elif dice_type.upper() == "D6":
            dice_total = rng.next(1,7)
            print(f"D6 {dice_total}")
            continue
        elif dice_type.upper() == "D12":
            dice_total = rng.next(1,13)
            print(f"D12 {dice_total}")
            continue
        elif dice_type.upper() == "D20":
            dice_total = rng.next(1,21)
            print(f"D20 {dice_total}")
            continue
        else:
            print("Invalid dice type")
            continue

if __name__ == "__main__":
    main()