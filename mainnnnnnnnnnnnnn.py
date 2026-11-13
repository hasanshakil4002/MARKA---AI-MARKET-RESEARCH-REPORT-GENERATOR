#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import MarketResearchAi

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")



def run():
    """
    Run the crew.
    """
    product = str(input("Product: ")).strip()
    region = str(input("Region: ")).strip()
    country = str(input("Country: ")).strip()
    inputs = {
        'product': product,
        'region': region,
        'country': country,
        'current_year': str(datetime.now().year)
    }
    try:
        MarketResearchAi().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()





