import rng_module

def main():
    rng = rng_module.OscarRNG()
    dice_total = rng.next(1,7)
    print(f"D6 {dice_total}")
    dice_total = rng.next(1,7) + rng.next(1,7)
    print(f"2D6 {dice_total}")
    

if __name__ == "__main__":
    main()