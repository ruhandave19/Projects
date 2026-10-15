import yfinance as yf
import mplfinance as mpf

data = yf.Ticker("HDFCBANK.NS")

df = data.history(period='1y', interval='1d', auto_adjust=True)

df_last3 = df.head(3)

mpf.plot(
    df_last3,
    type="candle",
    volume=True,
    tight_layout=True,
    figsize=(14, 6),
    scale_padding=0.4,
    title="HDFCBANK.NS - 3d Candlestick Chart",
    savefig=dict(fname="charts/HDFCBANK_3d.png", dpi=150, bbox_inches="tight")
)

mpf.plot(
    df,
    type="candle",
    volume = True,
    tight_layout=True,
    figsize=(14, 6),
    scale_padding=0.4,
    title="HDFCBANK.NS - 1y Candlestick Chart",
    savefig=dict(fname="charts/HDFCBANK_1y.png", dpi=150, bbox_inches="tight")
)