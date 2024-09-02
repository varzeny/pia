# trend/google_trend

# lib
import asyncio
from pytrends.request import TrendReq

# module

# attribute
TREND = TrendReq(hl='ko', tz=0)
COUNTRIES = [
    'south_korea', 'united_states', 'japan', 'united_kingdom'
]

# method
async def get_trends_by_country(contry_name:str)->list:
    try:
        resp = await asyncio.to_thread( TREND.trending_searches, contry_name )
        result = resp[0].values.tolist()
        return result
    except Exception as e:
        print("ERROR from get_trends_by_country : ", e)
        return None
    

async def get_news_by_trend(trend):
    return


if __name__ == "__main__":
    resp = asyncio.run( get_trends_by_country("south_korea") )
    print(resp)