import yfinance as yf
import mplfinance as mpf

data = yf.Ticker("HDFCBANK.NS")

df = data.history(period='6mo', interval='1d', auto_adjust=True)

mpf.plot(
    df.tail(3),
    type="candle",
    style="yahoo",
    tight_layout=True,
    figsize=(6, 6),
    scale_padding=0.4,
    savefig=dict(fname="charts/HDFCBANK_3d.png", dpi=150, bbox_inches="tight")
)

mpf.plot(
    df.tail(40),
    type="candle",
    style="yahoo",
    tight_layout=True,
    figsize=(18, 10),
    scale_padding=0.4,
    savefig=dict(fname="charts/HDFCBANK_40d.png", dpi=150, bbox_inches="tight")
)