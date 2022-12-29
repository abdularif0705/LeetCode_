# https://leetcode.com/problems/course-schedule-ii/
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """
        :type numCourses: int
        :type prerequisites: list[list[int]]
        :rtype: list[int]
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
        can_take = [] # array of all courses we can take
        order = [] # order classes can be taken, has to be a list because set makes things in order and LeetCode wants it in the correct order not from smallest to biggest numbers
        done = set()

        for i in range(numCourses):
            d[i] = set() # creating empty set for all courses
        for (ai, bi) in prerequisites:
            d[ai].add(bi) # adding all the prerequisites the course needs
        for i in range(numCourses):
            if len(d[i]) == 0:  # sets have lengths as well
                can_take.append(i)  # add courses that can be taken with no prerequisites required
        
        while can_take:
            order.append(can_take[len(can_take)-1])
            # print(can_take)
            # print(order)
            curr_course = can_take.pop() #TODO: if it pops off the top then what'll happen after we add the other courses to can_take? Pretty sure we should use a queue for LIFO
            del d[curr_course]  # deleting course from dictionary
            for key in d:  # going through all courses in the dictionary
                # if curr_course is in the set of d[key] we'll remove it because since we're taking the course we
                # have fulfilled the requirement
                if curr_course in d[key]:
                    d[key].remove(curr_course)
                    # if the d[key] course has no prerequisites left then it can be taken, so we'll add it to can_take
                    if len(d[key]) == 0:
                        can_take.append(key)

            done.add(curr_course)  # only can add unique value since it's a set

        if len(done) != numCourses:  # if it's a fail then return empty list
            order = []

        return order

def main():
    test = Solution()
    print(test.findOrder(2, [[1, 0]]))
    print(test.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
    print(test.findOrder(1, []))
    print(test.findOrder(2, [[0, 1]]))


main()
