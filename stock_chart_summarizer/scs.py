import yfinance as yf
import mplfinance as mpf
from google import genai
from google.genai.errors import APIError
import time, random
from dotenv import load_dotenv

data = yf.Ticker("HDFCBANK.NS")

df = data.history(period='6mo', interval='1d', auto_adjust=True)

mpf.plot(
    df.tail(3),
    type="candle",
    style="yahoo",
    axisoff=True,
    tight_layout=True,
    figsize=(6, 6),
    scale_padding=0.4,
    savefig=dict(fname="charts/HDFCBANK_3d.png", dpi=150, bbox_inches="tight")
)

mpf.plot(
    df.tail(40),
    type="candle",
    style="yahoo",
    axisoff=True,
    tight_layout=True,
    figsize=(18, 10),
    scale_padding=0.4,
    savefig=dict(fname="charts/HDFCBANK_40d.png", dpi=150, bbox_inches="tight")
)

load_dotenv()
client = genai.Client()

uploaded_file1 = client.files.upload(file="charts/HDFCBANK_3d.png")
uploaded_file2 = client.files.upload(file="charts/HDFCBANK_40d.png")

PROMPT = """
You are analysing candlestick charts for an educational project. Describe only what the charts show. Do not give advice, predictions, or recommendations.

IMAGE 1 shows the last 3 daily candles of a stock, numbered 1 (oldest, left) to 3 (most recent, right). A green candle closed above its open; a red candle closed below its open. Judge shapes and proportions visually. Do not rely on axis labels for exact prices.

TASK 1: PATTERN DETECTION
Compare the 3 candles against ONLY the patterns defined below.
- A multi-candle pattern spans 2 or 3 adjacent candles. A single-candle pattern applies to one candle.
- First, check for a multi-candle pattern. If one matches, report the best match only.
- Then check every candle NOT already part of a multi-candle pattern. Report each one that clearly matches a single-candle pattern. If no multi-candle pattern was found, check all 3 candles this way.
- Each candle receives at most one single-candle label. If a candle fits two, choose the closer match.
- Do not force a match. A candle that does not clearly fit a definition gets no label. Fewer patterns is better than a doubtful one.
- List the patterns in order of candle number. If nothing matches, return an empty list.

SINGLE-CANDLE PATTERNS

1) Marubozu: A long candle whose body fills almost its entire range. Each wick must be no more than about 10% of the candle's full range (high to low). A candle with any wick longer than that is NOT a Marubozu.
a) Bullish Marubozu: A long green candle, with Open at or very near the Low and Close at or very near the High.
b) Bearish Marubozu: A long red candle, with Open at or very near the High and Close at or very near the Low.
If both wicks are present, the wick on the close side should be the shorter one.

2) Indecision Candle (Spinning Top or Doji): The real body is no more than about a quarter of the candle's full range (a near-flat body also counts). BOTH wicks are clearly visible, and neither wick is more than about three times the length of the other.

3) Paper Umbrella
a) Bullish Hammer: The lower wick is at least twice the body, the body sits in the upper part of the range, and the upper wick is no longer than the body. The wicks must be clearly unequal.
b) Shooting Star: The upper wick is at least twice the body, the body sits in the lower part of the range, and the lower wick is no longer than the body. The wicks must be clearly unequal.
If a candle has two clearly visible wicks of similar length, it is an Indecision Candle, never a Hammer or Shooting Star.

MULTI-CANDLE PATTERNS (P1 = first candle of the pattern, P2 = second, P3 = third)

4) Engulfing
a) Bullish Engulfing: P1 is a red candle. P2 is a green candle whose body engulfs the body of P1.
b) Bearish Engulfing: P1 is a green candle. P2 is a red candle whose body engulfs the body of P1.

5) Harami
a) Bullish Harami: P1 is a red candle. P2 is a green candle that opens above P1's close and closes below P1's open.
b) Bearish Harami: P1 is a green candle. P2 is a red candle that opens below P1's close and closes above P1's open.

6) Morning Star: P1 is a long red candle closing near its low. P2 is an Indecision Candle, preferably opening with a gap down. P3 is a green candle that gaps up.

7) Evening Star: P1 is a long green candle closing near its high. P2 is an Indecision Candle, preferably opening with a gap up. P3 is a red candle that gaps down.

TASK 2: TREND
IMAGE 2 shows the last 40 daily candles of the same stock, ending with the same 3 candles as Image 1. Judge the GENERAL trend across the WHOLE 40-candle window, from its first candle to its last, as a swing trader would. Do not let the most recent 5 or 6 candles decide the answer: a short recent move inside a longer range does not change the general trend. Classify it as exactly one of:
- Uptrend: across the window, swing highs and swing lows both step upward overall, and price ends well above where it started.
- Downtrend: across the window, swing highs and swing lows both step downward overall, and price ends well below where it started.
- Sideways: price oscillates within a broad band, ends roughly where it started, and swing highs and lows show no sustained rise or fall across the window.
- Unclear: none of the above fits.

OUTPUT
Respond with JSON only, with no extra text and no code fences, in exactly this form:
{
  "patterns": [{"name": "<pattern name>", "candles": [<candle numbers>]}],
  "trend": "<Uptrend | Downtrend | Sideways | Unclear>",
  "trend_reason": "<one sentence describing the whole window>"
}
Use only these pattern names: Bullish Marubozu, Bearish Marubozu, Indecision Candle, Bullish Hammer, Shooting Star, Bullish Engulfing, Bearish Engulfing, Bullish Harami, Bearish Harami, Morning Star, Evening Star."""

retries = 2
for attempt in range(1, retries+2):
    try: 
        interaction = client.interactions.create(
            model="gemini-3.8-flash",
            input=[
                {"type": "text", "text": PROMPT},
                {
                    "type": "image",
                    "uri": uploaded_file1.uri,
                    "mime_type": uploaded_file1.mime_type
                },
                {
                    "type": "image",
                    "uri": uploaded_file2.uri,
                    "mime_type": uploaded_file2.mime_type
                }
            ],
            generation_config={
                    "temperature": 0
                }
        )
        print(interaction.output_text)
        exit()
    except APIError as e:
        print(f'Attempt {attempt}: Gemini call failed -> {e}')
        if e.code in (500, 503):
            if attempt <= retries:
                wait_time = min(5 * (2 ** (attempt - 1)), 30) 
                wait_time += random.uniform(0, 2)
                print(f'Waiting {wait_time:.1f} seconds before retrying...')
                time.sleep(wait_time)
            else:
                print('GIVING UP: Gemini call failed after all retries')
                exit()  
        else:
            print(f"Error {e.code}: {e.message}")
            exit()