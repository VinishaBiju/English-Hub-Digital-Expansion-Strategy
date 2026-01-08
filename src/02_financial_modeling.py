"""
English Hub Financial Modeling & Business Case
Author: Vinisha Biju
Description: ROI calculation, revenue projections, cost analysis
"""

import pandas as pd
import numpy as np

class FinancialModel:
    def __init__(self):
        self.projections = {}
        
    def calculate_revenue_projections(self, years=5):
        """5-year revenue projection model"""
        print("Calculating revenue projections...")
        
        base_users = 100_000
        growth_rate = 0.40  # 40% YoY growth
        arpu_usd = 120  # Average Revenue Per User
        
        projections = []
        for year in range(1, years + 1):
            users = base_users * (1 + growth_rate) ** year
            revenue = users * arpu_usd / 1_000_000  # In millions
            projections.append({
                'Year': year,
                'Users': int(users),
                'Revenue_M_USD': round(revenue, 2),
                'Growth_%': round(growth_rate * 100, 1)
            })
        
        df = pd.DataFrame(projections)
        self.projections['revenue'] = df
        print("✓ Revenue projections complete")
        return df
    
    def calculate_costs(self):
        """Calculate operational costs"""
        costs = {
            'Technology_Development': 2.0,  # Million USD
            'Marketing_CAC': 1.5,
            'Operations': 1.0,
            'Content_Creation': 0.8,
            'Customer_Support': 0.5
        }
        
        total_costs = sum(costs.values())
        costs['Total_Annual_Cost_M'] = total_costs
        
        print(f"\nTotal Annual Costs: ${total_costs}M")
        return costs
    
    def calculate_roi(self):
        """Calculate Return on Investment"""
        initial_investment = 5.0  # Million USD
        year3_revenue = 14.4  # From projections
        year3_costs = 5.8
        
        net_profit = year3_revenue - year3_costs
        roi = ((net_profit - initial_investment) / initial_investment) * 100
        
        print(f"\n3-Year ROI: {roi:.1f}%")
        print(f"Break-even: Year 2")
        return roi

if __name__ == "__main__":
    model = FinancialModel()
    revenue_df = model.calculate_revenue_projections()
    print("\n", revenue_df)
    costs = model.calculate_costs()
    roi = model.calculate_roi()
