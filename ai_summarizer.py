def summarize_data(data):
    summary = {}
    summary['title'] = data.get('title', 'No Title')
    explanation = data.get('explanation', 'No details available.')
    summary['summary'] = explanation[:300] + '...'  # Short summary
    summary['date'] = data.get('date', 'Unknown')
    summary['image'] = data.get('url', None)
    return summary
