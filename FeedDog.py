def feedDog(hunger_level, biscuit_size):
    hunger_level.sort()
    biscuit_size.sort()

    dogs_fed = 0
    for i in hunger_level:
        for biscuit in biscuit_size:
            if biscuit_size[biscuit] >= hunger_level[i]:
                dogs_fed += 1
                biscuit_size.remove(biscuit_size[biscuit])
                break
    return dogs_fed

# print(feedDog([2, 1],[1,3,2]))