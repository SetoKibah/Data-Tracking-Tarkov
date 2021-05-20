def pre_raid():
    pass
    gear_cost = int(input('Enter initial gear cost: '))
    map = input('Enter map raiding on: ')
    return gear_cost, map
    
def post_raid():
    profit = int(input('Total Rouble Gain: '))
    cost = int(input('Enter total re-arming cost: '))
    total = (profit - cost)
    return int(profit - cost)

# End of program save session positive or negative to a file?
def export_results():
    pass

def main():
    list_of_gains = []
    map_list = []
    end_of_session_gains = 0
    maps_ran = 0

    while True:
        gear_cost, map = pre_raid()
        post_raid_gain = post_raid()
        map_list.append(map)
        end_gain = post_raid_gain - gear_cost
        end_of_session_gains += end_gain
        maps_ran += 1

        list_of_gains.append(end_gain)

        print('\n\nGains for the session so far: ')
        for gain, current_map in zip(list_of_gains, map_list):
            print(f'₽{gain} on {current_map}.')

        response = input("\nAnother raid? (y/n): ")
        if response == 'y':
            continue
        elif response == 'n':
            print(f'----------------------------------------------\nTotal gains for the session: ₽{end_of_session_gains}.\nTotal Maps Raided: {maps_ran}.\n----------------------------------------------')
            break
        else:
            print('You did not give a valid response, program will end.')
            break
main()