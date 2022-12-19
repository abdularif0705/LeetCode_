# https://leetcode.com/problems/course-schedule/description/
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # build dictionary that maps course to prerequisite
        # collect all courses u can take
        d = {} # or dict() same ting
        can_take = []
        done = set() # every item is unique so it auto-cleans duplicate values for you

        for i in range(numCourses):
            d[i] = set() # make an empty set {}
        for (course, prereq) in prerequisites:
            d[course].add(prereq) # this adds to the empty set we created before mind blown

        for i in range(numCourses):
            if len(d[i]) == 0: # sets have lengths as well
                can_take.append(i)
        # print(f"canTake{can_take}")
        while can_take:
            curr_course = can_take.pop()
            del d[curr_course] # deleting course from dictionary
            for key in d:
                if curr_course in d[key]:
                    d[key].remove(curr_course) # since we remove here we avoid duplicate values when appending to can_take
                    if len(d[key]) == 0:
                        can_take.append(key) # since we removed above we avoid duplicate values which we can also solve by using a set()

            done.add(curr_course) # only can add unique val

        return len(done) == numCourses # if done has all courses

def main():
    test = Solution()
    print(test.canFinish(2, [[1,0]]))
    print(test.canFinish(2, [[1,0],[0,1]]))
    print(test.canFinish(2, []))
    print(test.canFinish(2, [[0,1]]))

main()