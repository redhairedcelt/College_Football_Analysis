stats <- read.csv('all_stats.csv')
colnames(stats)
stats_clean <- stats %>% select(-school_name, -year, -Unnamed..0, -conf_abbr, -losses, -losses_conf, -notes, -rank_min, -rank_pre, -sos, -srs, -win_loss_pct, -win_loss_pct_conf, -wins, -wins_conf)

