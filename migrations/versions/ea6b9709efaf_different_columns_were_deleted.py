"""Different columns were deleted

Revision ID: ea6b9709efaf
Revises: c75e406ff4d0
Create Date: 2021-04-27 12:44:03.564711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea6b9709efaf'
down_revision = 'c75e406ff4d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company_key_metrics', sa.Column('date', sa.Date(), nullable=False))
    op.drop_column('company_key_metrics', 'debt_to_equity')
    op.drop_column('company_key_metrics', 'average_payables')
    op.drop_column('company_key_metrics', 'capex_per_share')
    op.drop_column('company_key_metrics', 'payables_turnover')
    op.drop_column('company_key_metrics', 'receivables_turnover')
    op.drop_column('company_key_metrics', 'roic')
    op.drop_column('company_key_metrics', 'net_income_per_share')
    op.drop_column('company_key_metrics', 'capex_to_depreciation')
    op.drop_column('company_key_metrics', 'payout_ratio')
    op.drop_column('company_key_metrics', 'capex_to_revenue')
    op.drop_column('company_key_metrics', 'debt_to_assets')
    op.drop_column('company_key_metrics', 'earnings_yield')
    op.drop_column('company_key_metrics', 'ev_to_sales')
    op.drop_column('company_key_metrics', 'interest_coverage')
    op.drop_column('company_key_metrics', 'tangible_book_value_per_share')
    op.drop_column('company_key_metrics', 'sales_general_and_administrative_to_revenue')
    op.drop_column('company_key_metrics', 'cash_per_share')
    op.drop_column('company_key_metrics', 'enterprise_value')
    op.drop_column('company_key_metrics', 'inventory_turnover')
    op.drop_column('company_key_metrics', 'revenue_per_share')
    op.drop_column('company_key_metrics', 'net_current_asset_value')
    op.drop_column('company_key_metrics', 'capex_to_operating_cash_flow')
    op.drop_column('company_key_metrics', 'stock_based_compensation_to_revenue')
    op.drop_column('company_key_metrics', 'tangible_asset_value')
    op.drop_column('company_key_metrics', 'working_capital')
    op.drop_column('company_key_metrics', 'free_cash_flow_yield')
    op.drop_column('company_key_metrics', 'invested_capital')
    op.drop_column('company_key_metrics', 'operating_cash_flow_per_share')
    op.drop_column('company_key_metrics', 'pfcf_ratio')
    op.drop_column('company_key_metrics', 'pb_ratio')
    op.drop_column('company_key_metrics', 'days_of_inventory_on_hand')
    op.drop_column('company_key_metrics', 'interest_debt_per_share')
    op.drop_column('company_key_metrics', 'days_payables_outstanding')
    op.drop_column('company_key_metrics', 'ev_to_free_cash_flow')
    op.drop_column('company_key_metrics', 'book_value_per_share')
    op.drop_column('company_key_metrics', 'intangibles_to_total_assets')
    op.drop_column('company_key_metrics', 'dividend_yield')
    op.drop_column('company_key_metrics', 'graham_number')
    op.drop_column('company_key_metrics', 'return_on_tangible_assets')
    op.drop_column('company_key_metrics', 'free_cash_flow_per_share')
    op.drop_column('company_key_metrics', 'average_inventory')
    op.drop_column('company_key_metrics', 'research_and_developement_to_revenue')
    op.drop_column('company_key_metrics', 'shareholders_equity_per_share')
    op.drop_column('company_key_metrics', 'current_ratio')
    op.drop_column('company_key_metrics', 'income_quality')
    op.drop_column('company_key_metrics', 'days_sales_outstanding')
    op.drop_column('company_key_metrics', 'average_receivables')
    op.drop_column('company_key_metrics', 'metrics_date')
    op.drop_column('company_key_metrics', 'pocfratio')
    op.drop_column('company_key_metrics', 'graham_net_net')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company_key_metrics', sa.Column('graham_net_net', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('pocfratio', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('metrics_date', sa.DATE(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('average_receivables', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('days_sales_outstanding', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('income_quality', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('current_ratio', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('shareholders_equity_per_share', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('research_and_developement_to_revenue', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('average_inventory', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('free_cash_flow_per_share', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('return_on_tangible_assets', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('graham_number', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('dividend_yield', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('intangibles_to_total_assets', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('book_value_per_share', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('ev_to_free_cash_flow', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('days_payables_outstanding', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('interest_debt_per_share', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('days_of_inventory_on_hand', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('pb_ratio', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('pfcf_ratio', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('operating_cash_flow_per_share', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('invested_capital', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('free_cash_flow_yield', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('working_capital', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('tangible_asset_value', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('stock_based_compensation_to_revenue', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('capex_to_operating_cash_flow', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('net_current_asset_value', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('revenue_per_share', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('inventory_turnover', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('enterprise_value', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('cash_per_share', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('sales_general_and_administrative_to_revenue', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('tangible_book_value_per_share', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('interest_coverage', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('ev_to_sales', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('earnings_yield', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('debt_to_assets', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('capex_to_revenue', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('payout_ratio', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('capex_to_depreciation', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('net_income_per_share', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('roic', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('receivables_turnover', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('payables_turnover', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('capex_per_share', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('average_payables', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('company_key_metrics', sa.Column('debt_to_equity', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.drop_column('company_key_metrics', 'date')
    # ### end Alembic commands ###
