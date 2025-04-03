from functools import reduce

class MapFilterReduce():
    def mapData(self):
        # syntax - map(function, iterable item)
        print("before map: ", self.mapListValue)
        mappedData = list(map(lambda x: x ** 2, self.listValue)) #square the number and map to list
        print("after map: ", mappedData)

    def filterData(self):
        # syntax - filter(function, iterable item)
        print("before filter: ", self.filterListValue)
        filteredData = list(filter(lambda x: x % 2, self.filterListValue)) # filters based on condition
        print("after filter: ", filteredData)

    def reduceData(self):
        # syntax - reduce(function, iterable, initializer) initializer is optional where we can initialize from where to reduce
        print("before reduce: ", self.reduceListValue)
        reducedData = reduce(lambda x, y: x + y, self.reduceListValue)
        print("after reduce without initializer: ", reducedData)
        reducedDataWithInitializer = reduce(lambda x,y: x + y, self.reduceListValue, 10) # here 10 is first argument and works like 10 + 1 = 11, 11 + 2 = 12 etc
        print("after reduce with initializer: ", reducedDataWithInitializer)


dataToMap = MapFilterReduce()

def switch_case(value):
    match value:
        case 1:
            dataToMap.mapListValue = [1,2,3,4,5,6]
            dataToMap.mapData()

        case 2:
            dataToMap.filterListValue = [1,2,3,4,5,6]
            dataToMap.filterData()

        case 3:
            dataToMap.reduceListValue = [1,2,3,4,5,6]
            dataToMap.reduceData()

getProcessType = int(input("Enter process type: "))      
switch_case(getProcessType)

