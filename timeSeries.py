'''
Given a timeseries print number of users logged in at a given time
'''

class Solution:

    def analyzeActivity(self, ts):
        start = 0
        end = 0
        num_users = 0
        output = []


        while start < len(ts) and end < len(ts):
            session_start = ts[start][1]
            session_end = ts[end][2]

            if session_start < session_end:
                num_users += 1
                start += 1
                output.append([session_start, num_users])

                if start == len(ts):
                    output.append([session_end, num_users - 1])

            elif session_start >= session_end:
                num_users -= 1
                end += 1
                output.append([session_end, num_users])

        #output = sorted(l, key=lambda x: x[2])
        return sorted(output, key=lambda x: x[0])

ts = [
("September", 1.2, 4.5),
("June", 3.1, 6.7),
("August", 8.9, 10.3)]

print Solution().analyzeActivity(ts)