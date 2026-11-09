"""Bai-Perron (1998, 2003) via programmazione dinamica, selezione del numero di break con BIC,
trimming h = 0.15, massimo 5 break. Due specificazioni per segmento: 'mean' (sola intercetta, 1 parametro)
e 'trend' (intercetta + trend lineare, 2 parametri). Replica la logica di strucchange::breakpoints.
Uso: python bai_perron.py series.csv   (colonne: year, <nomi serie>)
"""
import sys, numpy as np, pandas as pd

def seg_ssr(y, t, a, b, spec):
    yy = y[a:b]
    if spec == "mean":
        return ((yy - yy.mean()) ** 2).sum()
    X = np.column_stack([np.ones(b - a), t[a:b]])
    beta, *_ = np.linalg.lstsq(X, yy, rcond=None)
    return ((yy - X @ beta) ** 2).sum()

def bai_perron(y, spec, h=0.15, maxb=5):
    y = np.asarray(y, float); T = len(y); t = np.arange(T, dtype=float); hmin = int(np.floor(h * T))
    k = 1 if spec == "mean" else 2
    SSR = np.full((T + 1, T + 1), np.inf)
    for a in range(T):
        for b in range(a + hmin, T + 1):
            SSR[a, b] = seg_ssr(y, t, a, b, spec)
    # dp[m][b] = min SSR of first b obs with m breaks (m+1 segments), with last segment ending at b
    best = {0: {b: (SSR[0, b], []) for b in range(hmin, T + 1)}}
    for m in range(1, maxb + 1):
        best[m] = {}
        for b in range((m + 1) * hmin, T + 1):
            cand = min(((best[m - 1][j][0] + SSR[j, b], best[m - 1][j][1] + [j]) for j in range(m * hmin, b - hmin + 1) if j in best[m - 1]), key=lambda x: x[0], default=None)
            if cand: best[m][b] = cand
    out = []
    for m in range(0, maxb + 1):
        if T in best[m]:
            ssr, brk = best[m][T]
            npar = (m + 1) * k + m  # coefficienti + date di break (come strucchange)
            bic = T * np.log(ssr / T) + npar * np.log(T)
            out.append((m, bic, brk))
    return out

if __name__ == "__main__":
    df = pd.read_csv(sys.argv[1], index_col=0)
    rows = []
    for col in df.columns:
        s = df[col].dropna()
        for spec in ("mean", "trend"):
            res = bai_perron(s.values, spec)
            m, bic, brk = min(res, key=lambda x: x[1])
            dates = [int(s.index[j - 1]) for j in brk]  # ultimo anno del segmento precedente (convenzione strucchange)
            rows.append(dict(serie=col, spec=spec, n_break_BIC=m, break_dates=", ".join(map(str, dates)), bic_by_m=" | ".join(f"{mm}:{b:.1f}" for mm, b, _ in res)))
            print(col, spec, m, dates)
    pd.DataFrame(rows).to_csv("bai_perron_two_specs.csv", index=False)
