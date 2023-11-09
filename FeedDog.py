def feedDog(hunger_level, biscuit_size):
    hunger_level.sort()
    biscuit_size.sort()

    dogs_fed = 0
    for i in range(len(hunger_level)):
        for b in range(len(biscuit_size)):
            if biscuit_size[b] >= hunger_level[i]:
                dogs_fed += 1
                biscuit_size.remove(biscuit_size[b])
                break
    return dogs_fed


#bprint(feedDog([2, 1],[1,3,2]))