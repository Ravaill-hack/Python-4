def ft_mean(args: list) -> float:
    """A function that calculates the mean of a numbers list
    """

    assert args
    tot_sum = 0
    for arg in args:
        tot_sum += arg
    return (float(tot_sum) / len(args))


def ft_median(args: list) -> float:
    """A function that calculates the median of a numbers list
    """

    assert args
    nb_args = len(args)
    sorted_args = sorted(args)
    i_median = nb_args // 2
    if (nb_args % 2 == 0):
        return ((sorted_args[i_median - 1] + sorted_args[i_median]) / 2)
    else:
        return (sorted_args[i_median])
    return (sorted_args[i_median(nb_args)])


def ft_quartile(args: list) -> list:
    """A function that calculates the quartiles of a numbers list
    """
    assert args
    sorted_args = sorted(args)
    nb_args = len(args)
    q1 = 0
    q2 = 0
    i_q1 = (nb_args + 3) / 4 - 1
    i_q2 = (3 * nb_args + 1) / 4 - 1

    if ((nb_args + 3) % 4 == 0):
        q1 = sorted_args[int(i_q1)]
        q2 = sorted_args[int(i_q2)]
    else:
        inf1 = sorted_args[int(i_q1 // 1)]
        sup1 = sorted_args[int(i_q1 // 1 + 1)]
        if (i_q1 % 1 == 0.25):
            q1 = ((3 * inf1 + sup1) / 4)
        elif (i_q1 % 1 == 0.5):
            q1 = ((inf1 + sup1) / 2)
        else:
            q1 = ((inf1 + 3 * sup1) / 4)
        inf2 = sorted_args[int(i_q2 // 1)]
        sup2 = sorted_args[int(i_q2 // 1 + 1)]
        if (i_q2 % 1 == 0.25):
            q2 = ((3 * inf2 + sup2) / 4)
        elif (i_q2 % 1 == 0.5):
            q2 = ((inf2 + sup2) / 2)
        else:
            q2 = ((inf2 + 3 * sup2) / 4)
    return [float(q1), float(q2)]


def ft_var(args: list, mean: float) -> float:
    """A function that calculates the variance of a numbers list
    """

    assert args
    nb_args = len(args)
    variance = 0
    for item in args:
        variance += (item - mean) ** 2
    variance = variance / nb_args
    return (variance)


def perform_kwarg(args: list, kwarg: str):
    """A function that performs the calcul asked
    """
    if (kwarg == 'mean'):
        print(f"mean: {ft_mean(args)}")
    elif (kwarg == 'median'):
        print(f"median: {ft_median(args)}")
    elif (kwarg == 'quartile'):
        print(f"quartile: {ft_quartile(args)}")
    elif (kwarg == 'std'):
        print(f"std: {ft_var(args, ft_mean(args)) ** 0.5}")
    elif (kwarg == 'var'):
        print(f"var: {ft_var(args, ft_mean(args))}")
    else:
        return


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Takes an unknown quantity of numbers and performs several
    calculations depending on what is asked in the kwargs
    """

    list_args = list(args)
    assert kwargs

    for kwar_key, kwarg_value in kwargs.items():
        try:
            perform_kwarg(list_args, kwarg_value)
        except AssertionError:
            print("ERROR")
