import heapq

arr = [1,2,3,4,5,6,7,8,9,10]
# arr = [5,4,3,2,1]
heap = []

for i in arr:
    heapq.heappush(heap, i)
    # print(len(heap))
    if len(heap) > 4:
        heapq._heappop_max(heap)
    print(heap)


print(heapq.heappop(heap))
# for i in arr:
#     print(heapq.heappop(heap))
