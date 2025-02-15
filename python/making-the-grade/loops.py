"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    new_scores = []

    for score in student_scores:
        new_scores.append(round(score))
    
    return new_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    failed = 0

    for score in round_scores(student_scores):
        if score <= 40:
            failed += 1

    return failed


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    best = []

    for score in round_scores(student_scores):
        if score >= threshold:
            best.append(score)

    return best


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    start_threshold = 41
    increment = (highest - 40) / 4

    thresholds = []

    for marks in range(4):
        thresholds.append(int(start_threshold + marks * increment))

    return thresholds


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    results = []

    for i_idex, score in enumerate(student_scores):
        for j_index, name in enumerate(student_names):
            if i_idex == j_index:
                results.append(f"{i_idex+1}. {name}: {score}")

    return results


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    results = []

    for student in student_info:
        if student[1] == 100:
            results.append(student)
            break
    
    return results[0] if len(results) == 1 else results
