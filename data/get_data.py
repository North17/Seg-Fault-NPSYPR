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

    elif x == 1:
        if zone == 400:
            from data.time_infected import time_infected
            return time_infected
        else:
            x = zone%20 + 1
            y = zone//20 + 1

            from data.organise_data import get_time_infected
            time_infected = get_time_infected(x,y)
            
            return time_infected

    elif x == 2:
        from data.population_density import population_density
        return population_density
    

