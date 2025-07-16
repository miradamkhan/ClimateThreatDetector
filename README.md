# RiskCheck

A Python-based web application that helps homeowners assess climate-related threats for any U.S. address. The application provides a comprehensive risk assessment including flood, wildfire, drought, and sea level rise risks.

## Features

- Address geocoding to get precise location data
- Risk assessment across multiple environmental factors
- Weighted scoring system (0-100)
- Detailed risk explanations for each category
- Simple map visualization of the location
- RESTful API endpoint for easy integration

## Setup

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Flask application:
```bash
python app.py
```

The server will start on `http://localhost:5000`

## API Usage

### Get Risk Assessment

```
GET /risk?address=<address>
```

Example:
```
GET /risk?address=123 Main St, New York, NY 10001
```

Response:
```json
{
    "overall_score": 65,
    "risk_summary": "Flood: Located in FEMA flood zone X (low risk) | Wildfire: Moderate wildfire risk due to nearby forest areas",
    "individual_risks": {
        "flood_risk": {
            "score": 80,
            "explanation": "Located in FEMA flood zone X (low risk)"
        },
        "wildfire_risk": {
            "score": 40,
            "explanation": "Moderate wildfire risk due to nearby forest areas"
        },
        "drought_risk": {
            "score": 30,
            "explanation": "Low drought risk based on historical precipitation data"
        },
        "sea_level_risk": {
            "score": 20,
            "explanation": "No significant sea level rise risk"
        }
    },
    "coordinates": [40.7128, -74.0060],
    "map_image": "base64_encoded_image_data"
}
```

## Project Structure

- `app.py`: Flask application and API endpoints
- `data_fetch.py`: Data fetching and geocoding functionality
- `scoring.py`: Risk scoring and assessment logic
- `requirements.txt`: Project dependencies

## Future Improvements

- Integration with real environmental data APIs (NOAA, FEMA, etc.)
- Enhanced map visualization with proper map tiles
- Additional risk factors and scoring criteria
- User interface for direct interaction
- Historical risk trend analysis
- Machine learning-based risk prediction 