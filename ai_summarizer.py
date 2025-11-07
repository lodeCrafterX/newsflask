def summarize_data(data):
    if not isinstance(data, dict) or not data:
        return {}

    summary = {
        'title': data.get('title', 'No Title'),
        'summary': (data.get('explanation', 'No details available.')[:300] + '...'),
        'date': data.get('date', 'Unknown'),
        'image': data.get('url') or data.get('hdurl')
    }

    return summary
