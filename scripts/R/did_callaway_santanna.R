# =============================================================================
# DiD STAGGERED MODERNO — Callaway & Sant'Anna (2021)
# Estensione metodologica per §6bis del working paper Italia 1995-2024
# =============================================================================
# Risponde alla raccomandazione ALTA del peer review: applicare stimatori DiD
# staggered moderni (Callaway-Sant'Anna, Sun-Abraham) al posto del TWFE classico,
# che è dimostrato essere distorto con effetti di trattamento eterogenei nel tempo
# (Goodman-Bacon 2021, de Chaisemartin-D'Haultfœuille 2020).
#
# Input: did_eurostat_sectors.csv
#   - sector: codice NACE settore
#   - year: 1995-2024
#   - wage_share: quota salari = D1 / B1G (Eurostat nama_10_a64)
#   - treated: 1 per settori privatizzati/liberalizzati (D, H49, J61), 0 per controllo
#   - year_treat: anno di privatizzazione (0 per controlli)
#   - post: dummy 1 se anno >= year_treat
#
# Pacchetti: did (Callaway-Sant'Anna 2021), fixest (per TWFE confronto), bacondecomp
# =============================================================================

# --- 0. Setup ---------------------------------------------------------------
need <- c("did", "fixest", "bacondecomp", "ggplot2")
for (pkg in need) {
  if (!requireNamespace(pkg, quietly = TRUE)) {
    install.packages(pkg, repos = "https://cloud.r-project.org")
  }
}
suppressPackageStartupMessages({
  library(did)
  library(fixest)
  library(ggplot2)
})

# --- 1. Carica dati ---------------------------------------------------------
csv_path <- "data/did_eurostat_REAL.csv"  # dataset Eurostat reale (209 righe); eseguire dalla radice del repository
if (!file.exists(csv_path)) {
  stop(paste("CSV non trovato:", csv_path,
             "\nMetti il file nella working directory"))
}
df <- read.csv(csv_path)
cat("Dataset:", nrow(df), "righe,", length(unique(df$sector)), "settori,",
    length(unique(df$year)), "anni\n")
cat("Trattati:", paste(unique(df$sector[df$treated==1]), collapse=", "), "\n")
cat("Controllo:", paste(unique(df$sector[df$treated==0]), collapse=", "), "\n\n")

# Sector come ID numerico (richiesto da pkg did)
df$sector_id <- as.numeric(as.factor(df$sector))

# G (first treatment year): per controlli mai-trattati, deve essere 0 (mai trattato)
df$G <- df$year_treat  # già zero per controlli

# =============================================================================
# 2. TWFE classico (confronto, ATT atteso ≈ -0.15)
# =============================================================================
cat("==============================================================================\n")
cat("STEP 1 — TWFE staggered classico (specifica usata nel paper preliminare)\n")
cat("==============================================================================\n")

twfe <- feols(wage_share ~ post | sector + year, data = df, cluster = ~sector)
cat("\nTWFE staggered:\n")
print(summary(twfe))

# =============================================================================
# 3. Goodman-Bacon decomposition (diagnostica del TWFE staggered)
# =============================================================================
cat("\n==============================================================================\n")
cat("STEP 2 — Goodman-Bacon decomposition\n")
cat("==============================================================================\n")
cat("(quantifica quanto del coefficiente TWFE viene da confronti 'cattivi'\n")
cat(" — già-trattati come controlli di nuovi-trattati)\n\n")

df_bacon <- df  # bacondecomp richiede pannello bilanciato
bd <- tryCatch({
  bacondecomp::bacon(wage_share ~ post,
                     data = df_bacon,
                     id_var = "sector_id",
                     time_var = "year")
}, error = function(e) {
  cat("bacondecomp error:", e$message, "\n")
  NULL
})
if (!is.null(bd)) {
  print(bd)
  cat("\nInterpretazione: se 'Earlier vs Later Treated' ha peso significativo\n")
  cat("e ATT eterogeneo nel tempo, TWFE classico è distorto.\n")
}

# =============================================================================
# 4. Callaway-Sant'Anna ATT(g,t) — stimatore CORRETTO
# =============================================================================
cat("\n==============================================================================\n")
cat("STEP 3 — Callaway-Sant'Anna ATT(g,t)\n")
cat("==============================================================================\n")

# att_gt: stima ATT per ogni coorte g (year_treat) e ogni anno t
# control_group = "notyettreated" usa controlli + non-ancora-trattati
# Per pochi controlli, "nevertreated" è più conservativo
cs_att <- att_gt(
  yname = "wage_share",
  tname = "year",
  idname = "sector_id",
  gname = "G",
  data = df,
  control_group = "nevertreated",
  bstrap = TRUE,
  cband = TRUE,
  biters = 1000
)

cat("\nATT(g,t) — Stime per coorte e tempo:\n")
print(summary(cs_att))

# --- Aggregazioni di Callaway-Sant'Anna ---

cat("\n--- Aggregazione 'simple' (ATT medio post-trattamento) ---\n")
agg_simple <- aggte(cs_att, type = "simple")
print(summary(agg_simple))

cat("\n--- Aggregazione 'group' (ATT per coorte di trattamento) ---\n")
agg_group <- aggte(cs_att, type = "group")
print(summary(agg_group))

cat("\n--- Aggregazione 'dynamic' (event-study) ---\n")
agg_dynamic <- aggte(cs_att, type = "dynamic")
print(summary(agg_dynamic))

cat("\n--- Aggregazione 'calendar' (ATT per anno calendario) ---\n")
agg_calendar <- aggte(cs_att, type = "calendar")
print(summary(agg_calendar))

# =============================================================================
# 5. Confronto sintetico
# =============================================================================
cat("\n==============================================================================\n")
cat("TABELLA SINTESI — TWFE classico vs Callaway-Sant'Anna\n")
cat("==============================================================================\n\n")

twfe_est <- coef(twfe)["post"]
twfe_se  <- se(twfe)["post"]
cs_est   <- agg_simple$overall.att
cs_se    <- agg_simple$overall.se

cat(sprintf("%-30s %12s %12s %12s\n", "Stimatore", "ATT", "SE", "CI 95%"))
cat(rep("-", 70), "\n", sep="")
cat(sprintf("%-30s %+12.4f %12.4f [%+.3f, %+.3f]\n",
            "TWFE staggered (paper prelim)",
            twfe_est, twfe_se, twfe_est - 1.96*twfe_se, twfe_est + 1.96*twfe_se))
cat(sprintf("%-30s %+12.4f %12.4f [%+.3f, %+.3f]\n",
            "Callaway-Sant'Anna (simple)",
            cs_est, cs_se, cs_est - 1.96*cs_se, cs_est + 1.96*cs_se))

# Differenza
diff <- abs(twfe_est - cs_est)
cat(sprintf("\nDifferenza |TWFE - C-S|: %.4f (%.1f%%)\n",
            diff, 100 * diff / abs(cs_est)))

if (diff < 0.02) {
  cat("\n=> Differenza modesta: TWFE staggered e Callaway-Sant'Anna producono stime simili.\n")
  cat("   Eterogeneità degli effetti di trattamento moderata.\n")
} else {
  cat("\n=> Differenza significativa: gli stimatori divergono, suggerendo eterogeneità\n")
  cat("   degli effetti di trattamento. C-S è il riferimento corretto.\n")
}

# =============================================================================
# 6. Salvataggio risultati
# =============================================================================
results <- data.frame(
  estimator = c("TWFE staggered", "C-S simple", "C-S group avg", "C-S dynamic avg"),
  att = c(twfe_est, agg_simple$overall.att, mean(agg_group$att.egt),
          mean(agg_dynamic$att.egt[agg_dynamic$egt >= 0])),
  se  = c(twfe_se, agg_simple$overall.se, NA, NA)
)
write.csv(results, "did_results_CS.csv", row.names = FALSE)

# Tabella ATT(g,t) completa
gt_table <- data.frame(
  group = cs_att$group,
  time = cs_att$t,
  att = cs_att$att,
  se = cs_att$se
)
write.csv(gt_table, "did_att_gt.csv", row.names = FALSE)

cat("\nFile salvati:\n")
cat("  - did_results_CS.csv (sintesi)\n")
cat("  - did_att_gt.csv (ATT per coorte e tempo)\n\n")

# Plot event-study (se ggplot2 disponibile)
tryCatch({
  p <- ggdid(agg_dynamic) +
    labs(title = "Event-study: ATT per anni dal trattamento",
         subtitle = "Callaway-Sant'Anna staggered DiD",
         x = "Anni dal trattamento (privatizzazione/liberalizzazione)",
         y = "ATT su quota salari (pp)") +
    theme_minimal()
  ggsave("did_event_study.png", p, width = 8, height = 5, dpi = 150)
  cat("Plot event-study salvato: did_event_study.png\n")
}, error = function(e) {
  cat("Plot non generato:", e$message, "\n")
})

cat("\n============= FINE =============\n")
cat("Riferimenti:\n")
cat("  Callaway B. & Sant'Anna P.H.C. (2021) JoE 225(2): 200-230.\n")
cat("  Goodman-Bacon A. (2021) JoE 225(2): 254-277.\n")
cat("  Bertaud E. & Sant'Anna P.H.C. (2024) Stata Journal, did package R.\n")
