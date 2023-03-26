#!/usr/bin/python3
# A simple timer with following features
# 1. It will beep when the timer is done
# 2. Press S to start stopwatch and accumulate time
# 3. Press S again to stop stopwatch and print accumulated time
# 4. Press T to start timer and lose from accumulated time
# 5. Press T again to stop timer and print accumulated time
#
# Author: Bishal Santra (http://bsantraigi.github.io) MIT License

import subprocess
import time

time_per_task = 30*60*100 # 30 minutes as 100th of a second
TASKS = [
    {'name': 'Studying', 'credit': 4, 'done': 0, 'timer': time_per_task},
    {'name': 'Coding', 'credit': 2, 'done': 0, 'timer': time_per_task},
    {'name': 'Reading', 'credit': 3, 'done': 0, 'timer': time_per_task},
    {'name': 'Writing', 'credit': 4, 'done': 0, 'timer': time_per_task},
]
CURRENT_TASK = 0

def print_stats_table_border():
    print(''.ljust(10, '-') + '+'.center(3, '-') + ''.rjust(10, '-') + '+'.center(3, '-') + ''.rjust(10, '-'))

    

def print_stats_table_header():
    print_stats_table_border()
    print('Task'.ljust(10) + '|'.center(3) + 'Completed'.rjust(10) + '|'.center(3) + 'Remaining'.rjust(10))
    print_stats_table_border()

def print_stats_table_footer():
    print_stats_table_border()

def print_stats_table():
    print_stats_table_header()
    for task in TASKS:
        timer_state = task['credit'] - task['done'] - 1 + task['timer']/time_per_task
        print(task['name'].ljust(10) + '|'.center(3) + str(task['done']).rjust(10) + '|'.center(3) + f"{timer_state:0.2f}".rjust(10))
    print_stats_table_footer()


def beep():
    print('\a')

def print_time(t, prefix=None):
    print('\r', end='')
    if prefix:
        print(prefix, end=' ')

    if t < 0:
        print('-', end='')
        t = -t
    print('{:02d}:{:02d}:{:02d}.{:1d}'.format(
        t // 360000,
        t // 6000 % 60,
        t // 100 % 60,
        t // 10 % 10), end='')


def find_next_task():
    global CURRENT_TASK
    if TASKS[CURRENT_TASK]['done'] < TASKS[CURRENT_TASK]['credit']:
        return CURRENT_TASK
    else:
        for i in range(len(TASKS)):
            _i = (i + CURRENT_TASK + 1) % len(TASKS)
            if TASKS[_i]['done'] < TASKS[_i]['credit']:
                CURRENT_TASK = _i
                return _i
    return -1

def print_menu():
    print()
    print_welcome_message("~Task Manager~")
    print_stats_table()
    print()
    # Next task
    next_task = find_next_task()
    if next_task >= 0:
        print('Next task: {}'.format(TASKS[next_task]['name']))
        print('Press S to start stopwatch')
    else:
        print('No task left! GET OUT!!!')
        print('Do NOT come back until tomorrow!!!')

def main():
    timer = False
    stopwatch_time = 0

    # S/s: Start/resume timer
    # C: Change task
    
    while True:
        print_menu()
        key = input()
        if key == 's' or key == 'S':
            if timer:
                timer = False
            else:
                timer = True
                start_time = time.time()
                # timer_time = 0
        elif key == 'q' or key == 'Q':
            break
        else:
            print('Invalid key')

        if timer:
            # stopwatch loop, ctrl-c to stop
            print()
            while True:
                try:
                    delta_time = int((time.time() - start_time) * 100)
                    # sleep 10 ms
                    time.sleep(0.01)
                    # Print h:m:s:ms
                    print_time(stopwatch_time - delta_time, f"Timer {TASKS[CURRENT_TASK]['name']} -->")
                    # if stopwatch_time == 0:
                    #     beep()
                    #     print_time(stopwatch_time, "Timer done. Total Time -->")

                    #     timer = False
                    #     break
                except KeyboardInterrupt:
                    # Print h:m:s:ms
                    stopwatch_time -= delta_time
                    TASKS[CURRENT_TASK]['timer'] -= delta_time
                    print_time(stopwatch_time, "Timer stopped. Total Time Left -->")

                    timer = False
                    break

def print_welcome_message(message):
    result = subprocess.run(['figlet', '-c', message], capture_output=True, text=True)
    ascii_art = result.stdout
    magenta_ascii_art = "\033[35m" + ascii_art + "\033[0m";
    print(magenta_ascii_art)

if __name__ == '__main__':
    main()
