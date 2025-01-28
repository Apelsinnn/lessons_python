from typing import List, Union, Optional, Any


def summ(arg_1: Optional[int or float], arg_2: Union[int, float]) -> Any:
    """
    :param arg_1:
    :param arg_2:
    :return:
    """
    return arg_1 + arg_2


def list_to_int(a_list: list) -> List[int]:
    return [int(e) for e in a_list]


if __name__ == '__main__':
    print(summ(3, 4))
