def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]

    def format_rods():
        return f"{rods[0]} {rods[1]} {rods[2]}"

    states = [format_rods()]

    def move(num, source, target, auxiliary):
        if num == 1:
            rods[target].append(rods[source].pop())
            states.append(format_rods())
            return

        move(num - 1, source, auxiliary, target)
        rods[target].append(rods[source].pop())
        states.append(format_rods())
        move(num - 1, auxiliary, target, source)

    move(n, 0, 2, 1)

    return "\n".join(states)