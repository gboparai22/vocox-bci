# Market Sentinel Quant POC

**Strategy:** mean-reversion on SPY futures (10 min return > 1 σ of 30 min volatility)

**Workflow:**
1. Ingest live ticks (Polygon)
2. Compute z-score & backtest on 6 mo historical data
3. On live trigger:  
   • NeoPixel flash  
   • e-Ink “BUY SPY”/“SELL SPY”  
   • TTS “Sell SPY: 1σ reversion” + headline  