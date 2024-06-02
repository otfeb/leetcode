class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        setIntervals = []
        for value in intervals:
            if value not in setIntervals:
                setIntervals.append(value)

        if len(setIntervals) == 1:
            return setIntervals
        
        setIntervals.sort()
        result = []
        start = setIntervals[0][0]
        end = setIntervals[0][1]

        for i in range(1, len(setIntervals)):
            if end >= setIntervals[i][0] and end <= setIntervals[i][1]:
                end = setIntervals[i][1]
                if i == (len(setIntervals) - 1):
                    result.append([start,end])
                    return result
            elif end > setIntervals[i][1]:
                if i == (len(setIntervals) - 1):
                    result.append([start,end])
                    return result
            else:
                result.append([start,end])
                start = setIntervals[i][0]
                end = setIntervals[i][1]
                if i == (len(setIntervals) - 1):
                    if start >= result[-1][0] and end == result[-1][1]:
                        return result
                    result.append([setIntervals[i][0],setIntervals[i][1]])
                    return result