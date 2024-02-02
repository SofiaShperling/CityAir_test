def work_time_prediction(data) -> [int, int]:
  """This function predict the hours of the beggining and the end of the workday
    
    data should be a pandas table whith colums co2, pm10, pm25, humidity and only_hour
  
  Return: the hour of the start (int) and the hour of the end (int)"""

  average_min_co2 = data.groupby('only_hour')['co2'].mean().min()

  co2_indexes = []
  marks_co2 = data.groupby('only_hour')['co2'].mean()
  for index in range(len(marks_co2) - 1):
      if marks_co2[index] > 1.2*average_min_co2:
          co2_indexes.append(index)

  average_max_pm10 = data.groupby('only_hour')['pm10'].mean().max()

  pm10_indexes = []
  marks_pm10 = data.groupby('only_hour')['pm10'].mean()
  for index in range(len(marks_pm10) - 1):
      if marks_pm10[index] < 0.8*average_max_pm10:
          pm10_indexes.append(index)


  average_max_pm25 = data.groupby('only_hour')['pm25'].mean().max()

  pm25_indexes = []
  marks_pm25 = data.groupby('only_hour')['pm25'].mean()
  for index in range(len(marks_pm25) - 1):
      if marks_pm25[index] < 0.8*average_max_pm25:
          pm25_indexes.append(index)

  average_max_hum = data.groupby('only_hour')['humidity'].mean().max()

  hum_indexes = []
  marks_hum = data.groupby('only_hour')['humidity'].mean()
  for index in range(len(marks_hum) - 1):
      if marks_hum[index] < 0.97*average_max_hum:
          hum_indexes.append(index)

  day_start = round((co2_indexes[0] + pm10_indexes[0] + pm25_indexes[0] + hum_indexes[0])/4)


  day_end = round((co2_indexes[-1] + pm10_indexes[-1] + pm25_indexes[-1] + hum_indexes[-1])/4)

  return [day_start, day_end]