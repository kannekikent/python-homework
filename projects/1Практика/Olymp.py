def check_winners(scores, student_score):
    """Проверяет, входит ли результат студента в тройку лучших"""
    wins = sorted(scores)[-3:]
    if student_score in wins:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")
scores = [20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28]
student_score = 48
check_winners(scores, student_score)