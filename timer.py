#!/usr/bin/python3
# A simple timer with following features
# 1. It will beep when the timer is done
# 2. Press S to start stopwatch and accumulate time
# 3. Press S again to stop stopwatch and print accumulated time
# 4. Press T to start timer and lose from accumulated time
# 5. Press T again to stop timer and print accumulated time
#
# Author: Bishal Santra (http://bsantraigi.github.io) MIT License

import time

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

def print_menu():
    print()
    print('Press S to start stopwatch and accumulate time')
    print('Press S again to stop stopwatch and print accumulated time')
    print('Press T to start timer and lose from accumulated time')
    print('Press T again to stop timer and print accumulated time')
    print('Press Q to quit')

def main():
    stopwatch = False
    timer = False
    stopwatch_time = 0
    while True:
        print_menu()
        key = input()
        if key == 's' or key == 'S':
            if stopwatch:
                stopwatch = False
            else:
                stopwatch = True
                start_time = time.time()
                # stopwatch_time = 0
        elif key == 't' or key == 'T':
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

        if stopwatch:
            # stopwatch loop, ctrl-c to stop
            print()
            while True:
                try:
                    delta_time = int((time.time() - start_time) * 100)
                    # sleep 10 ms
                    time.sleep(0.05)
                    # Print h:m:s:ms
                    print_time(stopwatch_time + delta_time, "Stopwatch: ")
                except KeyboardInterrupt:
                    # Print h:m:s:ms
                    stopwatch_time += delta_time
                    print_time(stopwatch_time, "Stopwatch stopped. Total Time -->")

                    stopwatch = False
                    break
        if timer:
            print()
            while True:
                try:
                    delta_time = int((time.time() - start_time) * 100)
                    # sleep 10 ms
                    time.sleep(0.01)
                    # Print h:m:s:ms
                    print_time(stopwatch_time - delta_time, "Timer: ")
                    # if stopwatch_time == 0:
                    #     beep()
                    #     print_time(stopwatch_time, "Timer done. Total Time -->")

                    #     timer = False
                    #     break
                except KeyboardInterrupt:
                    # Print h:m:s:ms
                    stopwatch_time -= delta_time
                    print_time(stopwatch_time, "Timer stopped. Total Time Left -->")

                    timer = False
                    break

if __name__ == '__main__':
    main()
