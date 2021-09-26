def get_event_date(event):
    return event.date

def current_user(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in events:
            machines[event.machine] = set()
        if event.machine == "Login":
            machines[event.machine].add(event.user)
        elif event.machine == "Logout":
            machines[event.machine].remove(event.user)

    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ",".join(users)
            print("{}: {}".format(machine, user_list))


