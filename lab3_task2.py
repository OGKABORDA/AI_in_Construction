def find_common_participants(participants_first_group, participants_second_group, delimiter=','):
    first = set(participants_first_group.split(delimiter))
    second = set(participants_second_group.split(delimiter))
    common_participants = first.intersection(second)
    return sorted(common_participants)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, delimiter = "|"))