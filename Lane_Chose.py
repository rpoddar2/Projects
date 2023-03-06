""" * An area has n lanes.
    * All the n lanes have different types of amenities - hospital,
      pet shop, gym, mall, tea spot, restaurant.
    * Each lane has a minimum of 3 amenities.
    * Requirement of the person(req)."""

import random


def house():
    no_of_lane = int(input("No of lane"))

    # Assigning names to lanes
    lanes = []
    [lanes.append('Lane' + str(i)) for i in range(1, no_of_lane + 1)]
    print("The lanes in this area are", lanes)

    # Taking the input and displaying the options
    available_amenities = ['hospital', 'pet shop', 'gym', 'mall', 'tea spot', 'restaurant']
    no_of_required_amenities = int(input("Enter no of amenities required"))

    x = 'y'
    while x == 'y':
        print("Enter the required amenities from the below options - hospital, pet shop, gym, mall, tea spot, "
              "restaurant")
        # User requirements
        required_amenities = []
        for i in range(no_of_required_amenities):
            ele = [input()]
            required_amenities.append(ele)
        print([item for sublist in required_amenities for item in sublist])

        # Available requirements per lane
        available_amenities_per_lane = {}
        for lane in lanes:
            available_amenities_per_lane[lane] = random.sample(available_amenities, no_of_required_amenities)
        print(available_amenities_per_lane)

        # Checking if there is any match between user req and available req.
        for k, v in available_amenities_per_lane.items():
            if sorted(required_amenities) == sorted(v):
                print("The lane meeting your requirement is", k)
                break
            else:
                print("Try some change")
        x = input("press y to check again or n to exit")
        print('\n')


print(house())
