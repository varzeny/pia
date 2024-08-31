# trend/google_trend

# lib
from pytrends.request import TrendReq

# module

# attribute
TREND = TrendReq(hl='ko', tz=0)

# method

def get_trends(contry_name:str)->list:
    resp = TREND.trending_searches(pn=contry_name)
    result = resp[0].values.tolist()
    print(result)
    return result



if __name__ == "__main__":
    get_trends("japan")