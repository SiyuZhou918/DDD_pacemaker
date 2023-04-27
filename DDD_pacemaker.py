import datetime

def DDD_pacemaker():
    init_time = 0
    pstate = LRLONLY
    while True:
        if pstate == LRLONLY:
            process_LRLONLY()
            break
        elif pstate == APACE:
            process_APACE()
            break
        elif pstate == AB:
            process_APACE()
            break
        elif pstate == ARP:
            process_APACE()
            break
        elif pstate == APACE:
            process_APACE()
            break
        elif pstate == AVIONLY:
            process_APACE()
            break
        elif pstate == VPACE:
            process_APACE()
            break
        elif pstate == VB:
            process_APACE()
            break
        elif pstate == VRP:
            process_APACE()
            break
        else:
            print("Illegal state\n")
            break
        time += 1

def process_LRLONLY():
    expired_time = 1  # 1 second
    if check_LRL_timer == LRL_expired_time:
        reset_LRL_timer()
        pstate = APACE
        print("APACE")
    print("LRLONLY")

if __name__ == '__main__':
    DDD_pacemaker()
