# trend/google_trend

# lib
import asyncio
from pytrends.request import TrendReq
from sqlalchemy.ext.asyncio import AsyncSession

# module

# attribute
TREND = TrendReq(hl='ko', tz=0)
COUNTRIES = [
    'south_korea', 'united_states', 'japan', 'united_kingdom'
]

# method
async def get_trends_by_country(contry_name:str, ss:AsyncSession)->list:
    try:
        resp = await asyncio.to_thread( TREND.trending_searches, contry_name )
        result = resp[0].values.tolist()

        # db에 넣기


        return result
    except Exception as e:
        print("ERROR from get_trends_by_country : ", e)
        return None
    

async def get_trends_by_country_all()->dict:
    respData = {}
    try:
        for c in COUNTRIES:
            respData[c] = await get_trends_by_country(c)
        return respData
    except Exception as e:
        print("ERROR form get_trends_by_country_all : ", e)
        return None




if __name__ == "__main__":
    resp = asyncio.run( get_trends_by_country("japan") )
    print(resp)