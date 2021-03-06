"""new table Company_key_metrics

Revision ID: 5d46756d53f2
Revises: 5002a6cd089c
Create Date: 2020-08-01 11:38:41.171654

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d46756d53f2'
down_revision = '5002a6cd089c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company_key_metrics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('revenuePerShare', sa.Numeric(), nullable=True),
    sa.Column('netIncomePerShare', sa.Numeric(), nullable=True),
    sa.Column('operatingCashFlowPerShare', sa.Numeric(), nullable=True),
    sa.Column('freeCashFlowPerShare', sa.Numeric(), nullable=True),
    sa.Column('cashPerShare', sa.Numeric(), nullable=True),
    sa.Column('bookValuePerShare', sa.Numeric(), nullable=True),
    sa.Column('tangibleBookValuePerShare', sa.Numeric(), nullable=True),
    sa.Column('shareholdersEquityPerShare', sa.Numeric(), nullable=True),
    sa.Column('interestDebtPerShare', sa.Numeric(), nullable=True),
    sa.Column('marketCap', sa.Numeric(), nullable=True),
    sa.Column('enterpriseValue', sa.Numeric(), nullable=True),
    sa.Column('peRatio', sa.Numeric(), nullable=True),
    sa.Column('priceToSalesRatio', sa.Numeric(), nullable=True),
    sa.Column('pocfratio', sa.Numeric(), nullable=True),
    sa.Column('pfcfRatio', sa.Numeric(), nullable=True),
    sa.Column('pbRatio', sa.Numeric(), nullable=True),
    sa.Column('ptbRatio', sa.Numeric(), nullable=True),
    sa.Column('evToSales', sa.Numeric(), nullable=True),
    sa.Column('enterpriseValueOverEBITDA', sa.Numeric(), nullable=True),
    sa.Column('evToOperatingCashFlow', sa.Numeric(), nullable=True),
    sa.Column('evToFreeCashFlow', sa.Numeric(), nullable=True),
    sa.Column('earningsYield', sa.Numeric(), nullable=True),
    sa.Column('freeCashFlowYield', sa.Numeric(), nullable=True),
    sa.Column('debtToEquity', sa.Numeric(), nullable=True),
    sa.Column('debtToAssets', sa.Numeric(), nullable=True),
    sa.Column('netDebtToEBITDA', sa.Numeric(), nullable=True),
    sa.Column('currentRatio', sa.Numeric(), nullable=True),
    sa.Column('interestCoverage', sa.Numeric(), nullable=True),
    sa.Column('incomeQuality', sa.Numeric(), nullable=True),
    sa.Column('dividendYield', sa.Numeric(), nullable=True),
    sa.Column('payoutRatio', sa.Numeric(), nullable=True),
    sa.Column('salesGeneralAndAdministrativeToRevenue', sa.Numeric(), nullable=True),
    sa.Column('researchAndDdevelopementToRevenue', sa.Numeric(), nullable=True),
    sa.Column('intangiblesToTotalAssets', sa.Numeric(), nullable=True),
    sa.Column('capexToOperatingCashFlow', sa.Numeric(), nullable=True),
    sa.Column('capexToRevenue', sa.Numeric(), nullable=True),
    sa.Column('capexToDepreciation', sa.Numeric(), nullable=True),
    sa.Column('stockBasedCompensationToRevenue', sa.Numeric(), nullable=True),
    sa.Column('grahamNumber', sa.Numeric(), nullable=True),
    sa.Column('roic', sa.Numeric(), nullable=True),
    sa.Column('returnOnTangibleAssets', sa.Numeric(), nullable=True),
    sa.Column('grahamNetNet', sa.Numeric(), nullable=True),
    sa.Column('workingCapital', sa.Numeric(), nullable=True),
    sa.Column('tangibleAssetValue', sa.Numeric(), nullable=True),
    sa.Column('netCurrentAssetValue', sa.Numeric(), nullable=True),
    sa.Column('investedCapital', sa.Numeric(), nullable=True),
    sa.Column('averageReceivables', sa.Numeric(), nullable=True),
    sa.Column('averagePayables', sa.Numeric(), nullable=True),
    sa.Column('averageInventory', sa.Numeric(), nullable=True),
    sa.Column('daysSalesOutstanding', sa.Numeric(), nullable=True),
    sa.Column('daysPayablesOutstanding', sa.Numeric(), nullable=True),
    sa.Column('daysOfInventoryOnHand', sa.Numeric(), nullable=True),
    sa.Column('receivablesTurnover', sa.Numeric(), nullable=True),
    sa.Column('payablesTurnover', sa.Numeric(), nullable=True),
    sa.Column('inventoryTurnover', sa.Numeric(), nullable=True),
    sa.Column('roe', sa.Numeric(), nullable=True),
    sa.Column('capexPerShare', sa.Numeric(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('company_key_metrics')
    # ### end Alembic commands ###
