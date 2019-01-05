"""
Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.
"""


def triple_steps(step_size):
    if step_size == 1 or step_size == 0:
        return 1
    elif step_size == 2:
        return 2
    else:
        return triple_steps(step_size-1) + triple_steps(step_size-2) + triple_steps(step_size-3)

