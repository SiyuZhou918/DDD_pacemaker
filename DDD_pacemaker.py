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


if __name__ == '__main__':
    DDD_pacemaker()