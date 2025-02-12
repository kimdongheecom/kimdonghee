from com.kimdnghee.calculator.grade_model import GradeModel


class GradeService:
    def __init__(self):
        pass

    def execute(self,grade: GradeModel) -> GradeModel :
        name = grade.name
        korean = grade.korean
        english = grade.english
        math = grade.math
        society = grade.society
        math = grade.math
        science =grade.science

        total = korean + english + math + society + science
        avg = total / 5

        if avg >= 90:
            result = "A"
        elif avg >= 80:
            result = "B"
        elif avg >= 70:
            result = "C"
        elif avg >= 60:
            result = "D"
        else:
            result = "F"
        
        grade.result = result #grade라는 상자안에result값을 가져오는데, result값은 total과 average이다.
        grade.name = name

        return grade



