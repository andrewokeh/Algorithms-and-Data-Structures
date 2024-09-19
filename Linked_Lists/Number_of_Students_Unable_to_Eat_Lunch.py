class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # First solution that came to mind, but not the "proper" solution
        # while sandwiches and sandwiches[0] in students:
        #     students.remove(sandwiches[0])
        #     sandwiches.pop(0)
        # return len(students)

        result = len(students)
        count = Counter(students)

        for sandwich in sandwiches:
            if count[sandwich] > 0:
                result -= 1
                count[sandwich] -= 1
            else:
                return result

        return result
