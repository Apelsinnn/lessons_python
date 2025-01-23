from singleton_module_two import two, data


def one():
    return data * 100


if __name__ == '__main__':
    result = one() + two()
    print(result)
