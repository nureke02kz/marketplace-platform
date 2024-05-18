def recommend(items):
    # Пример простого рекомендательного алгоритма
    return sorted(items, key=lambda x: x['rating'], reverse=True)
