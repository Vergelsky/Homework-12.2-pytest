def get_val(collection, key, default='def'):

    """
    Принимает словарь, ключ и опционально значение по умолчанию.
    Возвращает значение по ключу из словаря, либо значение по умолчанию.
    :param collection: Словарь
    :param key: Ключ
    :param default: Значение по умолчанию
    :return:
    """

    if collection == {}:
        return default

    if key in collection:
        return collection[key]
    else: return default