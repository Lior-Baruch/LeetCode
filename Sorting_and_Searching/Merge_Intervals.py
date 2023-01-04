# Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals,
# return an array of the non-overlapping intervals that cover all the intervals in the input.
def merge(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    merged_interval = []
    sorted_intervals = intervals.sort(key=lambda x: x[0])
    for interval in intervals:
        start = interval[0]
        end = interval[1]
        if len(merged_interval) == 0:
            merged_interval.append(interval)
            continue
        last_start_in_merged = merged_interval[-1][0]
        last_end_in_merged = merged_interval[-1][1]
        if start <= last_end_in_merged <= end:
            merged_interval[-1][1] = end
        elif start > last_end_in_merged:
            merged_interval.append(interval)

    return merged_interval
