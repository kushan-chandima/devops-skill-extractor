import json


class DataCleaner:
    def __init__(self):
        pass

    def remove_duplicates(self, data):
        """Remove duplicate entries from the data."""
        if not data:
            return []
        if isinstance(data[0], dict):
            # For list of dicts, serialize to JSON for comparison
            seen = set()
            result = []
            for item in data:
                key = json.dumps(item, sort_keys=True)
                if key not in seen:
                    seen.add(key)
                    result.append(item)
            return result
        return list(set(data))

    def normalize_data(self, data):
        """Normalize the data for consistent formatting."""
        if not data:
            return []
        if isinstance(data[0], dict):
            # For dicts, normalize string values
            return data
        return [item.strip().lower() for item in data]

    def clean_data(self, data):
        """Clean and preprocess the data."""
        if not data:
            return []
        # For job postings (list of dicts), just return as-is after removing duplicates
        if data and isinstance(data[0], dict):
            return self.remove_duplicates(data)
        data = self.remove_duplicates(data)
        data = self.normalize_data(data)
        return data

    def filter_relevant_skills(self, data, relevant_keywords):
        """Filter the data to include only relevant skills based on keywords."""
        return [skill for skill in data if any(keyword in skill for keyword in relevant_keywords)]