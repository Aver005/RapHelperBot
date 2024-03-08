import re


def extract_hashtags(text):
    if text is None or "#" not in text:
        return "Тэгов нет"
    
    hashtags = re.findall(r'#\w+', text)
    formatted_hashtags = [' #' + hashtag[1:] for hashtag in hashtags]
    result = ''.join(formatted_hashtags)
    
    return result


def extract_status(text):
    statuses = ["Не вышел", "На площадках", "Только ВК", "Сведение", "Демо"]
    icons = ["🟦", "🟩", "🔵", "🟨", "🔶"]
    result = statuses[0]
    index = 0
    
    if text is None or len(text) == 0:
        return result
    
    for status in statuses:
        if status.lower() in text:
            result = f"{status} {icons[index]}"
        index += 1
    
    return result