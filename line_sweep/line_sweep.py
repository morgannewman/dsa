"""
Given a list of time intervals, find if any of them overlap. Each interval has a start time and a stop time.

Example 1: intervals = [[1, 1.5], [2, 3.5], [3, 3.75], [4, 5.5], [5, 6], [5.2, 5.4]] => True
Example 2: intervals = [[1, 2], [2.5, 3], [4, 7]] => False
"""
class C:
    START = 1
    END = 0

# Divide each pair into a start and end point
# Sort the list of points
# Keep a counter of how much intervals are active at any given time
def line_sweep(intervals):
    points = []
    for start, end in intervals:
        points.append([start, C.START])
        points.append([end, C.END])
    
    points.sort(key=lambda i: i[0])

    active_intervals = 0
    for point in points:
        if point[1] is C.START:
            active_intervals += 1
        else:
            active_intervals -= 1

        if active_intervals > 1:
            return True
    
    return False
    

def max_intervals(intervals):
    points = []
    for start, end in intervals:
        points.append([start, True])
        points.append([end, False])
    
    points.sort(key=lambda i: i[0])

    max_intervals = current_intervals = 0 
    
    for time, is_start in points:
        if is_start:
            current_intervals += 1
        else:
            current_intervals -= 1
        
        max_intervals = max(current_intervals, max_intervals)
    
    return max_intervals

print(max_intervals([[1, 1.5], [2, 3.5], [3, 3.75], [4, 5.5], [5, 6], [5.2, 5.4]]))