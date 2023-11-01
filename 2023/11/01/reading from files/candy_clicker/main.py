def aaa():
    print("Current Candies until next level: XXX/XXX")
    print("Next Level: X")
    input()

level = 1
xp = 0

levels = [5, 10, 30, 45, 100]
#Figuring out how much until next level
def next_level_check(level, xp, levels):
    level = level - 1
    for x in levels:
        level_number = x + 1
        if x > levels[x]:
            continue
        else:
            # Not progressed level
        
    

def click():
    print(f"Current Candies until next level: ")