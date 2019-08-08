"""
Given a list of intervals, merge all overlapping intervals. At the end of the merge, there should be no overlapping intervals

Example:
Input = [[1,3], [3,5], [6,8], [7,9]]
Output = [[1,5], [6,9]]
"""

def merge_intervals(intervals):
    points = []

    for start, end in intervals:
        points.append([start, True])
        points.append([end, False])
    
    points.sort(key=lambda i: i[0])

    active_intervals = 0
    interval_builder = []
    result = []
    for i in range(len(points)):
        time, is_start = points[i]

        if len(interval_builder) is 0:
            interval_builder.append(time)

        if is_start:
            active_intervals += 1
        else:
            active_intervals -= 1
        
        if active_intervals is 0:
            if i + 1 < len(points):
                next_time, next_is_start = points[i+1]
                if next_time == time and next_is_start:
                    continue

            interval_builder.append(time)
            result.append(interval_builder)
            interval_builder = []
    return result
        
        
print(merge_intervals([[1,3], [3,5], [6,8], [7,9]]))
