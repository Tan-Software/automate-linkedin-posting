#!/usr/bin/env python

from libs import welcome, generate_scheduled_post, post_on_linkedin

process_questions = {
    1: generate_scheduled_post,
    2: post_on_linkedin,
    3: post_on_linkedin
}

welcome.presentation()
result = int(welcome.questions())

if result <= len(process_questions) and result > 0:
    if result == 3:
        process_questions[result].send_test()
    else:
        process_questions[result].init()
else:
    print("Mauvais choix, bye.")

