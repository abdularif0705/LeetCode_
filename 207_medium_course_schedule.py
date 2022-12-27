# https://leetcode.com/problems/course-schedule/description/
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 1) build dictionary that maps course to prerequisite
        # 2) initialize dictionary by creating empty sets for each course from 0...numCourses
        # 3) go through each pair of [ai, bi] in prerequisites and add the prerequisite course (bi) needed to take
        # the course (ai) with d[ai].add(bi).
        # 4) go through all courses and find which courses have empty sets in the dictionary (which means the course
        # has no prerequisites and can be taken) and add these courses to the can_take array/list
        # 5) while can_take has a course inside we'll go through the loop
        # 6) look at the comments I used to explain within while loop below
        d = {}  # or dict() same ting
        can_take = []
        done = set()  # every item is unique so it auto-cleans duplicate values for you

        for i in range(numCourses):
            d[i] = set()  # initializing values in the dictionary by creating an empty set {} for every key

        # prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
        for (course, prerequisite) in prerequisites:  # course = ai && prerequisite = bi
            d[course].add(prerequisite)  # this adds to the empty set we created before - mind blown

        for i in range(numCourses):
            if len(d[i]) == 0:  # sets have lengths as well
                can_take.append(i)  # add courses that can be taken with no prerequisites required
        # print(f"canTake{can_take}")
        while can_take:
            curr_course = can_take.pop()  # course that we'll take rn
            del d[curr_course]  # deleting course from dictionary
            for key in d:  # going through all courses in the dictionary
                # if curr_course is in the set of d[key] we'll remove it because since we're taking the course we
                # have fulfilled the requirement
                if curr_course in d[key]:
                    # since we remove here we avoid adding course 0 and 1 for test case #3 when appending to can_take
                    d[key].remove(curr_course)
                    # if the d[key] course has no prerequisites left then it can be taken, so we'll add it to can_take
                    if len(d[key]) == 0:
                        # since we removed above we avoid adding course 0 and 1 for test case #3, duplicate values
                        # and which we can also solve by using a set()
                        can_take.append(key)

            done.add(curr_course)  # only can add unique value since it's a set

        return len(done) == numCourses  # if done has all courses that means we have taken them all!


def main():
    test = Solution()
    print(test.canFinish(2, [[1, 0]]))
    print(test.canFinish(2, [[1, 0], [0, 1]]))
    print(test.canFinish(2, []))  # Case #3
    print(test.canFinish(2, [[0, 1]]))


main()
