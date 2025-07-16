from flask import Flask, request, jsonify, render_template
from data_fetch import DataFetcher
from scoring import RiskScorer
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
data_fetcher = DataFetcher()
risk_scorer = RiskScorer()

@app.route('/risk', methods=['GET'])
def get_risk_assessment():
    """
    Risk assessment endpoint that accepts an address parameter.
    Returns a JSON response with risk scores and summary, or HTML if browser.
    """
    address = request.args.get('address')
    
    if not address:
        return jsonify({
            "error": "Address parameter is required"
        }), 400
        
    # Get risk data
    risk_data = data_fetcher.get_risk_data(address)
    
    if not risk_data:
        return jsonify({
            "error": "Could not process address"
        }), 400
        
    # Generate risk assessment
    assessment = risk_scorer.get_risk_assessment(risk_data)
    
    # Generate visualization if coordinates are available
    if "coordinates" in assessment:
        try:
            map_image = generate_risk_map(assessment)
            assessment["map_image"] = map_image
        except Exception as e:
            print(f"Error generating map: {e}")
    
    # If browser (accepts html), render template
    if 'text/html' in request.headers.get('Accept', ''):
        return render_template(
            'risk_report.html',
            overall_score=assessment.get('overall_score'),
            risk_summary=assessment.get('risk_summary'),
            individual_risks=assessment.get('individual_risks'),
            coordinates=assessment.get('coordinates'),
            map_image=assessment.get('map_image')
        )
    # Otherwise, return JSON
    return jsonify(assessment)

def generate_risk_map(assessment: dict) -> str:
    """
    Generate a simple risk map visualization.
    In production, this would use proper map tiles and risk zone overlays.
    
    Args:
        assessment (dict): Risk assessment data
        
    Returns:
        str: Base64 encoded image
    """
    lat, lon = assessment["coordinates"]
    
    # Create a simple scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(lon, lat, c='red', s=100)
    plt.title("Risk Location")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    
    # Convert plot to base64 string
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    
    return base64.b64encode(img.getvalue()).decode()

if __name__ == '__main__':
    app.run(debug=True) 