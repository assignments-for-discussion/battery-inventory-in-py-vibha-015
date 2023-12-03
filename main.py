def count_batteries_by_health(present_capacities):
    #rated_capacity
    rated_capacity = 120
  
    #list to store SOH of all the batteries
    SOH_list=[]
    for i in present_capacities:
      soh = 100 * (i/rated_capcity)
      SOH_list.append(soh)
      
    #create 3 variables to keep count of healthy, exchange and failed batteries and initialise to 0
    healthy_count = exchange_count = failed_count = 0
    for i in SOH_list:
      if(i>80 and <=100):
        healthy_count+=1
      elif(i>=62 and i<=80):
        exchange_count+=1
      else:
        failed_count+=1
        
  #return dictionary of count values
  return {
    "healthy": healthy_count,
    "exchange": exchange_count,
    "failed": failed_count
  }

def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
