import yfinance as yf
import mplfinance as mpf

data = yf.Ticker("HDFCBANK.NS")

df = data.history(period='6mo', interval='1d', auto_adjust=True)

mpf.plot(
    df.head(3),
    type="candle",
    tight_layout=True,
    figsize=(6, 6),
    scale_padding=0.4,
    savefig=dict(fname="charts/HDFCBANK_3d.png", dpi=150, bbox_inches="tight")
)

mpf.plot(
    df,
    type="candle",
    tight_layout=True,
    figsize=(18, 10),
    scale_padding=0.4,
    savefig=dict(fname="charts/HDFCBANK_1y.png", dpi=150, bbox_inches="tight")
)