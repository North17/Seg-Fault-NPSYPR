def get(x, zone):

    if x == 0:
        if zone == 400:
            from data.ages import ages
            return ages
        else:
            # zone = 20(y-1) + (x-1)
            x = zone%20 + 1
            y = zone//20 + 1

            from data.organise_data import get_ages
            ages = get_ages(x,y)

            return ages
