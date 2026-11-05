# [Brian Dobrott] - Assignment 4

    # changed 15 to 30
def check_session(idle_minutes, max_idle=30):
    # TODO: Evaluate idle time against max_idle threshold
    # Note: Check the default parameter value above against what the system requires!

    # changed ">" into ">="
    if idle_minutes >= max_idle:
        return "SESSION_EXPIRED"
    return "SESSION_ACTIVE"