from futu import *

quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)  # 创建行情对象

# 财务条件过滤器 ROE >= 15
roe_finance_filter = FinancialFilter()
roe_finance_filter.stock_field = StockField.RETURN_ON_EQUITY_RATE
roe_finance_filter.filter_min = 15
roe_finance_filter.is_no_filter = True

# 财务条件过滤器 资产负债率 <= 60%
debt_flow_finance_filter = FinancialFilter()
debt_flow_finance_filter.stock_field = StockField.DEBT_ASSET_RATE
debt_flow_finance_filter.filter_max = 60
debt_flow_finance_filter.is_no_filter = True

# 财务条件过滤器 现金流TTM > 0
cash_ttm_flow_finance_filter = FinancialFilter()
cash_ttm_flow_finance_filter.stock_field = StockField.OPERATING_CASH_FLOW_TTM
cash_ttm_flow_finance_filter.filter_min = 0
cash_ttm_flow_finance_filter.is_no_filter = True

print(quote_ctx.get_stock_filter(Market.SZ, [roe_finance_filter, debt_flow_finance_filter, cash_ttm_flow_finance_filter]))
quote_ctx.close()
