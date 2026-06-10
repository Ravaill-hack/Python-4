def ft_mean(args: list) -> float:
    """A function that calculates the mean of a numbers list
    """

    assert args
    tot_sum = 0
    for arg in args:
        tot_sum += arg
    return (float(tot_sum) / len(args))


"""FAUX IL N  A PAS DE I MEDIAN SI JE SUIS SUR UN NOMBRE PAIR"""
def i_median(nb_args: int) -> int:
    if (nb_args % 2 == 0):
        return (((nb_args / 2) + (nb_args / 2 - 1)) / 2)
    else :
        return (int(nb_args / 2))


def ft_median(args: list) -> float:
    """A function that calculates the median of a numbers list
    """

    assert args
    nb_args = len(args)
    sorted_args = sorted(args)
    return (sorted_args[i_median(nb_args)])

def ft_quartile(args: list) -> list:
    """A function that calculates the quartiles of a numbers list
    """
    assert args
    i_median = i_median(len(args))

    return [12, 12]


def perform_kwarg(args: list, kwarg: str):
    """A function that performs the calcul asked
    """
    if (kwarg == 'toto'):
        print(f"mean: {ft_mean(args)}")
    elif (kwarg == 'tutu'):
        print(f"median: {ft_median(args)}")
    elif (kwarg == 'tata'):
        print(f"quartile: {ft_quartile(args)}")
    elif (kwarg == 'hello'):
        print(f"std: ft_std(args)")
    elif (kwarg == 'world'):
        print(f"var: ft_var(args)")
    else:
        return


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Takes an unknown quantity of numbers and performs several
    calculations depending on what is asked in the kwargs
    """

    list_args = list(args)
    list_kwargs = list(kwargs)
    assert list_kwargs

    for kwarg in kwargs:
        try:
            perform_kwarg(list_args, kwarg)
        except AssertionError:
            print(f"ERROR")
    # quartile_25, quartile_75 = ft_quartile(list_args)