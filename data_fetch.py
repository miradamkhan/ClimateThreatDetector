import requests
import pandas as pd
from geopy.geocoders import Nominatim
from typing import Dict, Tuple, Optional
import json
import os

class DataFetcher:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="riskcheck_app")
        
    def geocode_address(self, address: str) -> Optional[Tuple[float, float]]:
        """
        Convert address to latitude and longitude coordinates.
        
        Args:
            address (str): Full address or zip code
            
        Returns:
            Tuple[float, float]: (latitude, longitude) or None if geocoding fails
        """
        try:
            location = self.geolocator.geocode(address)
            if location:
                return (location.latitude, location.longitude)
            return None
        except Exception as e:
            print(f"Geocoding error: {e}")
            return None

    def fetch_environmental_data(self, lat: float, lon: float) -> Dict:
        """
        Fetch environmental risk data for given coordinates.
        Currently using mock data, but can be extended to use real APIs.
        
        Args:
            lat (float): Latitude
            lon (float): Longitude
            
        Returns:
            Dict: Dictionary containing risk data for different categories
        """
        # Mock data - in production, this would fetch from real APIs
        mock_data = {
            "flood_risk": {
                "score": self._calculate_mock_risk(lat, lon, "flood"),
                "explanation": "Located in FEMA flood zone X (low risk)"
            },
            "wildfire_risk": {
                "score": self._calculate_mock_risk(lat, lon, "fire"),
                "explanation": "Moderate wildfire risk due to nearby forest areas"
            },
            "drought_risk": {
                "score": self._calculate_mock_risk(lat, lon, "drought"),
                "explanation": "Low drought risk based on historical precipitation data"
            },
            "sea_level_risk": {
                "score": self._calculate_mock_risk(lat, lon, "sea"),
                "explanation": "No significant sea level rise risk"
            }
        }
        return mock_data

    def _calculate_mock_risk(self, lat: float, lon: float, risk_type: str) -> int:
        """
        Generate mock risk scores based on coordinates.
        In production, this would use real data and calculations.
        
        Args:
            lat (float): Latitude
            lon (float): Longitude
            risk_type (str): Type of risk to calculate
            
        Returns:
            int: Risk score between 0 and 100
        """
        # Simple hash-based mock scoring
        base_score = abs(hash(f"{lat}{lon}{risk_type}")) % 100
        return min(max(base_score, 0), 100)

    def get_risk_data(self, address: str) -> Optional[Dict]:
        """
        Main method to get risk data for an address.
        
        Args:
            address (str): Full address or zip code
            
        Returns:
            Dict: Complete risk assessment data or None if geocoding fails
        """
        coords = self.geocode_address(address)
        if not coords:
            return None
            
        risk_data = self.fetch_environmental_data(*coords)
        return {
            "coordinates": coords,
            "risks": risk_data
        } 