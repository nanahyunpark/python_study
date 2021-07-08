# interest rate 최소공배수 단위로 배열 만들어서 계산값 집어넣어놔야함
# (i_r[15] ** y//15 ) * (i_r[y%15])

init_money, fund_year = map(int, input().split())

#print(init_money, fund_year)

dp = [0 for i in range(fund_year+1)]
dp[0] = init_money
#print(dp)

for year in range(1, fund_year+1):
    #print(year)
    print(year, dp)
    dp[year] = dp[year-1] * 1.05
    
    if year >= 3:
        if dp[year] < dp[year-3] * 1.2:
            dp[year] = dp[year-3] * 1.2
        
    
    if year >= 5:
        if dp[year] < dp[year-5] * 1.35:
            dp[year] = dp[year-5] * 1.35
    
    # dp[year] = int(dp[year])

#print(dp)
print(int(dp[fund_year]))
