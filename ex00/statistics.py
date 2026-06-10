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
    if (nb_args % 2 == 0):
        return (sorted_args[((nb_args / 2) + (nb_args / 2 - 1)) / 2])
    else :
        return (sorted_args[int(nb_args / 2)])

def ft_quartile(args: list) -> list:
    """A function that calculates the mquartiles of a numbers list
    """

    return [12, 12]


def perform_kwarg(args: list, kwarg: str):
    print(kwarg)
    if (kwarg == 'mean'):
        print(f"mean: {ft_mean(args)}")
    elif (kwarg == 'median'):
        print(f"median: {ft_median(args)}")
    elif (kwarg == 'quartile'):
        print(f"quartile: {ft_quartile(args)}")
    else:
        return


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Takes an unknown quantity of numbers and performs several
    calculations depending on what is asked in the kwargs
    """

    try:
        list_args = list(args)
        list_kwargs = list(kwargs)
        assert list_kwargs

        for kwarg in kwargs:
            perform_kwarg(list_args, kwarg)

    except AssertionError:
        print(f"ERROR")
    # quartile_25, quartile_75 = ft_quartile(list_args)