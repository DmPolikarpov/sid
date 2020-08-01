from sid.db import db

class Company_key_metrics(db.Model):
    """the model to describe key metrics of some company"""
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    revenuePerShare = db.Column(db.Numeric, nullable = True)
    netIncomePerShare = db.Column(db.Numeric, nullable = True)
    operatingCashFlowPerShare = db.Column(db.Numeric, nullable = True)
    freeCashFlowPerShare = db.Column(db.Numeric, nullable = True)
    cashPerShare = db.Column(db.Numeric, nullable = True)
    bookValuePerShare = db.Column(db.Numeric, nullable = True)
    tangibleBookValuePerShare = db.Column(db.Numeric, nullable = True)
    shareholdersEquityPerShare = db.Column(db.Numeric, nullable = True)
    interestDebtPerShare = db.Column(db.Numeric, nullable = True)
    marketCap = db.Column(db.Numeric, nullable = True)
    enterpriseValue = db.Column(db.Numeric, nullable = True)
    peRatio = db.Column(db.Numeric, nullable = True)
    priceToSalesRatio = db.Column(db.Numeric, nullable = True)
    pocfratio = db.Column(db.Numeric, nullable = True)
    pfcfRatio = db.Column(db.Numeric, nullable = True)
    pbRatio = db.Column(db.Numeric, nullable = True)
    ptbRatio = db.Column(db.Numeric, nullable = True)
    evToSales = db.Column(db.Numeric, nullable = True)
    enterpriseValueOverEBITDA = db.Column(db.Numeric, nullable = True)
    evToOperatingCashFlow = db.Column(db.Numeric, nullable = True)
    evToFreeCashFlow = db.Column(db.Numeric, nullable = True)
    earningsYield = db.Column(db.Numeric, nullable = True)
    freeCashFlowYield = db.Column(db.Numeric, nullable = True)
    debtToEquity = db.Column(db.Numeric, nullable = True)
    debtToAssets = db.Column(db.Numeric, nullable = True)
    netDebtToEBITDA = db.Column(db.Numeric, nullable = True)
    currentRatio = db.Column(db.Numeric, nullable = True)
    interestCoverage = db.Column(db.Numeric, nullable = True)
    incomeQuality = db.Column(db.Numeric, nullable = True)
    dividendYield = db.Column(db.Numeric, nullable = True)
    payoutRatio = db.Column(db.Numeric, nullable = True)
    salesGeneralAndAdministrativeToRevenue = db.Column(db.Numeric, nullable = True)
    researchAndDdevelopementToRevenue = db.Column(db.Numeric, nullable = True)
    intangiblesToTotalAssets = db.Column(db.Numeric, nullable = True)
    capexToOperatingCashFlow = db.Column(db.Numeric, nullable = True)
    capexToRevenue = db.Column(db.Numeric, nullable = True)
    capexToDepreciation = db.Column(db.Numeric, nullable = True)
    stockBasedCompensationToRevenue = db.Column(db.Numeric, nullable = True)
    grahamNumber = db.Column(db.Numeric, nullable = True)
    roic = db.Column(db.Numeric, nullable = True)
    returnOnTangibleAssets = db.Column(db.Numeric, nullable = True)
    grahamNetNet = db.Column(db.Numeric, nullable = True)
    workingCapital = db.Column(db.Numeric, nullable = True)
    tangibleAssetValue = db.Column(db.Numeric, nullable = True)
    netCurrentAssetValue = db.Column(db.Numeric, nullable = True)
    investedCapital = db.Column(db.Numeric, nullable = True)
    averageReceivables = db.Column(db.Numeric, nullable = True)
    averagePayables = db.Column(db.Numeric, nullable = True)
    averageInventory = db.Column(db.Numeric, nullable = True)
    daysSalesOutstanding = db.Column(db.Numeric, nullable = True)
    daysPayablesOutstanding = db.Column(db.Numeric, nullable = True)
    daysOfInventoryOnHand = db.Column(db.Numeric, nullable = True)
    receivablesTurnover = db.Column(db.Numeric, nullable = True)
    payablesTurnover = db.Column(db.Numeric, nullable = True)
    inventoryTurnover = db.Column(db.Numeric, nullable = True)
    roe = db.Column(db.Numeric, nullable = True)
    capexPerShare = db.Column(db.Numeric, nullable = True)

    def __repr__(self):
        return f'Company key metrics {self.company_id}'