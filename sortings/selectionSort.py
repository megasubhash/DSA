def selectionSort(arr):
    for i in range(0,len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if  arr[j] < arr[min]:
                min=j

        temp=arr[i]
        arr[i]=arr[min]
        arr[min]=temp        
    return arr


def main():
    arr=[5,4,6,1,9,2,0,67,77,12,11,44]
    arr=selectionSort(arr)
    for i in arr:
        print(i)
  
if __name__== "__main__":
  main()

