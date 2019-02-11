def hotel_cost(nights):
  return 140*nights
print hotel_cost(3)
def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
def rental_car_cost(days):
  cost = 40*days
  if days >= 7:
    cost -= 50
  elif days>=3:
    cost-=20
  return cost
def trip_cost(city,days,spending_money):
  total_cost = hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money
  print total_cost
  return total_cost
trip_cost("Los Angeles",5,600)
  