team1_num = 5
team2_num = 6
print('В команде Мастера кода участников:',team1_num, '!')
print('Итого сегодня в командах участников:',team1_num, 'и', team2_num, '!')
score_2 = 42
score_1 = 40
team1_time = 18015.2
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Команда Волшебники данных решила задачи за {} с.:'.format(team1_time))
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')
print(f'Результат битвы: {challenge_result}')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    print('Победа команды Мастера кода!')
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    print('Победа команды Волшебники Данных!')
else:
    print('Ничья!')

