"""Synthetic Control per la quota salari aggiustata italiana (AMECO ALCD0), trattamento 1992 (§8.6, §8.6.1).
Specificazione del paper: pesi w >= 0, sum w = 1, che minimizzano la distanza euclidea nei predictors
standardizzati (media omega pre-1992, media REER pre-1992, media disoccupazione pre-1992, omega 1965/1980/1991).
Baseline: donor ESP FRA BEL NLD AUT PRT FIN. Estensione: + GRC.
Riproduce il baseline del paper (pesi ESP 43,8 / FRA 22,6 / AUT 27,5 / FIN 6,1; gap -3,53; RMSPE 1,096; p 0,125).
Uso: python scripts/python/scm_greece.py data/ameco_scm_panel.csv data/scm_out
Dati: data/ameco_scm_panel.csv (AMECO via DBnomics: ALCD0, XUNRQ, ZUTN per 14 paesi, 1960-2024).
"""
import sys, numpy as np, pandas as pd
from scipy.optimize import minimize

panel = pd.read_csv(sys.argv[1]); pref = sys.argv[2]
W = panel.pivot_table(index="year", columns=["var", "iso"], values="value")
om, reer, un = W["ALCD0"], W["XUNRQ"], W["ZUTN"]
PRE, POST = list(range(1965, 1992)), list(range(1992, 2025))

def pred(c):
    return np.array([om.loc[PRE, c].mean(), reer.loc[PRE, c].mean(), un.loc[PRE, c].mean(), om.loc[1965, c], om.loc[1980, c], om.loc[1991, c]])

def fit(t, donors):
    X1 = pred(t); X0 = np.column_stack([pred(d) for d in donors])
    sd = np.concatenate([X1[None, :], X0.T]).std(axis=0); sd[sd == 0] = 1
    J = len(donors); f = lambda w: (((X1 - X0 @ w) / sd) ** 2).sum()
    best = None
    for s in range(20):
        w0 = np.random.RandomState(s).dirichlet(np.ones(J))
        r = minimize(f, w0, bounds=[(0, 1)] * J, constraints=({"type": "eq", "fun": lambda w: w.sum() - 1},), method="SLSQP", options=dict(maxiter=1000, ftol=1e-14))
        if best is None or r.fun < best.fun: best = r
    w = best.x; gap = pd.Series(om[t].values - om[donors].values @ w, index=om.index)
    pre = np.sqrt((gap.loc[PRE] ** 2).mean()); post = np.sqrt((gap.loc[POST] ** 2).mean())
    return dict(w=dict(zip(donors, np.round(w, 3))), gap=gap.loc[POST].mean(), g9801=gap.loc[1998:2001].mean(), pre=pre, ratio=post / pre, series=gap)

def run(donors, lab):
    b = fit("ITA", donors)
    print(f"\n== {lab}: donors={donors}"); print("pesi:", {k: v for k, v in b["w"].items() if v > 0.004})
    print(f"gap medio post-1992 {b['gap']:.3f}  gap 1998-2001 {b['g9801']:.3f}  RMSPE pre {b['pre']:.3f}  ratio post/pre {b['ratio']:.2f}")
    ratios = {"ITA": b["ratio"]}
    for d in donors: ratios[d] = fit(d, [x for x in donors if x != d] + ["ITA"])["ratio"]
    rank = sorted(ratios, key=ratios.get, reverse=True).index("ITA") + 1
    print("placebo in-space (RMSPE post/pre):", {k: round(v, 2) for k, v in sorted(ratios.items(), key=lambda kv: -kv[1])})
    print(f"rank Italia {rank}/{len(ratios)}  p one-sided {rank/len(ratios):.3f}")
    loo = [(d, fit("ITA", [x for x in donors if x != d])["gap"]) for d in donors]
    print("leave-one-out:", [(d, round(g, 2)) for d, g in loo])
    b["series"].rename(lab).to_csv(f"{pref}_gap_{lab}.csv")
    return dict(spec=lab, donors=" ".join(donors), weights=str(b["w"]), gap_post1992=round(b["gap"], 3), gap_1998_2001=round(b["g9801"], 3),
                rmspe_pre=round(b["pre"], 3), ratio_post_pre=round(b["ratio"], 2), rank_italy=rank, n_units=len(ratios),
                p_one_sided=round(rank / len(ratios), 3), loo_min=round(min(g for _, g in loo), 2), loo_max=round(max(g for _, g in loo), 2))

res = pd.DataFrame([run(["ESP", "FRA", "BEL", "NLD", "AUT", "PRT", "FIN"], "baseline"),
                    run(["ESP", "FRA", "BEL", "NLD", "AUT", "PRT", "FIN", "GRC"], "with_GRC")])
res.to_csv(f"{pref}_summary.csv", index=False); print(res.T)
