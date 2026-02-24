class BaseScraper:
    def fetch_data(self):
        """Fetch data from the source."""
        raise NotImplementedError("Subclasses must implement this method.")

    def parse_data(self, raw_data):
        """Parse the fetched data into a structured format."""
        raise NotImplementedError("Subclasses must implement this method.")