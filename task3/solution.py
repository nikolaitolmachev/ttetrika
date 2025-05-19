def appearance(intervals: dict[str, list[int]]) -> int:

    def clip_intervals(intervals_list):
        clipped = []
        for i in range(0, len(intervals_list), 2):
            start = max(intervals_list[i], lesson_start)
            end = min(intervals_list[i + 1], lesson_end)
            if start < end:
                clipped.append((start, end))
        return clipped

    def merge_intervals(intervals):
        if not intervals:
            return []
        intervals.sort()
        merged = [intervals[0]]
        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                merged[-1] = (last[0], max(last[1], current[1]))
            else:
                merged.append(current)
        return merged

    lesson_start, lesson_end = intervals['lesson']

    pupil_intervals = merge_intervals(clip_intervals(intervals['pupil']))
    tutor_intervals = merge_intervals(clip_intervals(intervals['tutor']))

    events = []

    for start, end in pupil_intervals:
        events.append((start, 'pupil_in'))
        events.append((end, 'pupil_out'))

    for start, end in tutor_intervals:
        events.append((start, 'tutor_in'))
        events.append((end, 'tutor_out'))

    events.sort(key=lambda x: x[0])

    pupil_present = False
    tutor_present = False
    last_time = None
    total_time = 0

    for time, event in events:
        if last_time is not None and pupil_present and tutor_present:
            total_time += time - last_time

        if event == 'pupil_in':
            pupil_present = True
        elif event == 'pupil_out':
            pupil_present = False
        elif event == 'tutor_in':
            tutor_present = True
        elif event == 'tutor_out':
            tutor_present = False

        last_time = time

    return total_time


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]


if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
