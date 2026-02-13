def mergeSort(array, key=None, reverse=False):
  if len(array) <= 1:
    return array
  mid = len(array) // 2
  leftHalf = array[:mid]
  rightHalf = array[mid:]
  sortedLeft = mergeSort(leftHalf, key, reverse)
  sortedRight = mergeSort(rightHalf, key, reverse)
  return merge(sortedLeft, sortedRight, key, reverse)

def merge(left, right, key=None, reverse=False):
  result = []
  i = 0
  j = 0
  while i < len(left) and j < len(right):
    if key is None:
      if left[i] < right[j] if not reverse else left[i] > right[j]:
        result.append(left[i])
        i += 1
      else:
        result.append(right[j])
        j += 1
    else:
      if key(left[i]) < key(right[j]) if not reverse else key(left[i]) > key(right[j]):
        result.append(left[i])
        i += 1
      else:
        result.append(right[j])
        j += 1
  result.extend(left[i:])
  result.extend(right[j:])
  return result