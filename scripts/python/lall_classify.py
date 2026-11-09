"""Classifica gli export SITC a 3 cifre (Rev.3 / Rev.4) secondo la tassonomia tecnologica di Lall (2000),
Oxford Development Studies 28(3), Table 1, definita su SITC Rev.2 a 3 cifre e qui adattata ai codici
introdotti in Rev.3/Rev.4 (elencati separatamente in EXTRA). Produce quote sull'export manifatturiero
(esclusi prodotti primari e 'altre transazioni') per paese e anno.
Uso: python lall_classify.py "data/raw/comtrade/COMTRADE_X_SITC3_*.csv" data/derived/lall   (il pattern tra virgolette)
"""
import sys, pandas as pd

PP = "001 011 022 025 034 036 041 042 043 044 045 054 057 071 072 074 075 081 091 121 211 212 222 223 232 244 245 246 261 263 268 271 273 274 277 278 281 286 287 289 291 292 322 333 341".split()
RB1 = "012 014 023 024 035 037 046 047 048 056 058 061 062 073 098 111 112 122 233 247 248 251 264 265 269 423 424 431 621 625 628 633 634 635 641".split()
RB2 = "282 288 323 334 335 411 511 514 515 516 522 523 531 532 551 592 661 662 663 664 667 681 682 683 684 685 686 687 688 689".split()
LT1 = "611 612 613 651 652 654 655 656 657 658 659 831 842 843 844 845 846 847 848 851".split()
LT2 = "642 665 666 673 674 675 676 677 679 691 692 693 694 695 696 697 699 821 893 894 895 897 898 899".split()
MT1 = "781 782 783 784 785".split()
MT2 = "266 267 512 513 533 553 554 562 572 582 583 584 585 591 598 653 671 672 678 786 791 882".split()
MT3 = "711 713 714 721 722 723 724 725 726 727 728 736 737 741 742 743 744 745 749 762 763 772 773 775 793 812 872 873 884 885 951".split()
HT1 = "716 718 751 752 759 761 764 771 774 776 778".split()
HT2 = "524 541 712 792 871 874 881".split()
OTH = "351 883 892 896 911 931 941 961 971".split()
# Codici presenti in Rev.3/Rev.4 ma non in Rev.2 (o rinumerati): assegnazione per analogia con la voce Rev.2 di origine
EXTRA = {"016": "RB1", "017": "RB1", "059": "RB1", "231": "PP", "272": "PP", "275": "PP", "276": "PP", "283": "PP", "284": "PP", "285": "PP",
         "342": "PP", "343": "PP", "344": "PP", "345": "PP", "421": "RB1", "422": "RB1", "525": "RB2", "542": "HT2", "571": "MT2", "572": "MT2",
         "573": "MT2", "574": "MT2", "575": "MT2", "579": "MT2", "597": "MT2", "811": "LT2", "813": "MT3", "891": "OTH", "899": "LT2",
         "731": "MT3", "733": "MT3", "735": "MT3", "746": "MT3", "747": "MT3", "748": "MT3", "841": "LT1", "629": "RB1", "581": "MT2", "593": "MT2"}

CAT = {}
for name, lst in [("PP", PP), ("RB1", RB1), ("RB2", RB2), ("LT1", LT1), ("LT2", LT2), ("MT1", MT1), ("MT2", MT2), ("MT3", MT3), ("HT1", HT1), ("HT2", HT2), ("OTH", OTH)]:
    for c in lst: CAT[c] = name
CAT.update(EXTRA)
GROUP = {"PP": "primary", "RB1": "resource", "RB2": "resource", "LT1": "low", "LT2": "low", "MT1": "medium", "MT2": "medium", "MT3": "medium", "HT1": "high", "HT2": "high", "OTH": "other"}

import glob
src = sys.argv[1]; pref = sys.argv[2]
files = sorted(glob.glob(src)) if "*" in src else [src]
df = pd.concat([pd.read_csv(f, dtype={"sitc3": str}) for f in files]); print("file letti:", len(files))
df["sitc3"] = df["sitc3"].str.zfill(3)
df["cat"] = df["sitc3"].map(CAT); df["group"] = df["cat"].map(GROUP).fillna("unclassified")
unc = df[df.group == "unclassified"].groupby("sitc3")["value_usd"].sum().sort_values(ascending=False)
tot = df.groupby(["iso", "year"])["value_usd"].sum()
print("quota non classificata sul totale export: %.2f%%" % (100 * df[df.group == "unclassified"].value_usd.sum() / df.value_usd.sum()))
print("codici non classificati (primi 10):", unc.head(10).to_dict())
g = df.groupby(["iso", "year", "group"])["value_usd"].sum().unstack(fill_value=0)
manuf = g[["resource", "low", "medium", "high"]].sum(axis=1)
shares = g[["resource", "low", "medium", "high"]].div(manuf, axis=0) * 100
shares["manuf_share_total"] = manuf / g.sum(axis=1) * 100
shares.round(2).to_csv(f"{pref}_shares.csv")
df.to_csv(f"{pref}_classified.csv", index=False)
# tabella per periodi
per = {"1995-99": (1995, 1999), "2000-07": (2000, 2007), "2008-14": (2008, 2014), "2015-23": (2015, 2023)}
rows = []
for iso in shares.index.get_level_values(0).unique():
    s = shares.loc[iso]
    for lab, (a, b) in per.items():
        m = s.loc[a:b].mean()
        rows.append(dict(iso=iso, period=lab, resource=m["resource"], low=m["low"], medium=m["medium"], high=m["high"]))
tab = pd.DataFrame(rows).round(1)
tab.to_csv(f"{pref}_periods.csv", index=False)
print(tab.pivot(index="iso", columns="period", values=["low", "high"]).round(1))
